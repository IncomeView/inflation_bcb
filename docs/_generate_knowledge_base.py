#!/usr/bin/env python3
"""
Gera PROJECT_KNOWLEDGE_BASE.md

Objetivo:
- Documentar arquitetura do projeto
- Catalogar classes
- Catalogar funções
- Catalogar imports
- Mostrar dependências internas
- Ignorar tudo que estiver no .gitignore
"""

import ast
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import pathspec

# =============================================================================
# CONFIG
# =============================================================================

ROOT = Path(__file__).resolve().parents[1]

OUTPUT = ROOT / "docs" / "_PROJECT_KNOWLEDGE_BASE.md"

INCLUDED_ROOTS = [
    "src",
    "tests",
    "docs",
]

CONFIG_FILES = [
    "pyproject.toml",
    "requirements.txt",
    "Dockerfile",
    "docker-compose.yml",
    "Makefile",
    "README.md",
]

DOCS_FILES = [
    "architecture.md",
    "business_rules.md",
    "data_dictionary.md",
    "pipeline.md",
    "runbook.md",
]

ALWAYS_IGNORE = {
    "__pycache__",
    ".ipynb_checkpoints",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
}


# =============================================================================
# GITIGNORE
# =============================================================================


def load_gitignore():

    gitignore = ROOT / ".gitignore"

    if not gitignore.exists():
        return None

    patterns = gitignore.read_text(encoding="utf-8").splitlines()

    return pathspec.PathSpec.from_lines(
        pathspec.patterns.GitWildMatchPattern,
        patterns,
    )


GIT_SPEC = load_gitignore()
PARSE_ERRORS = []


def is_ignored(path: Path):

    for part in path.parts:

        if part in ALWAYS_IGNORE:
            return True

    if GIT_SPEC is None:
        return False

    try:

        rel = path.relative_to(ROOT).as_posix()

        return GIT_SPEC.match_file(rel)

    except Exception:

        return False


# =============================================================================
# TREE
# =============================================================================


def build_tree():

    lines = [ROOT.name, ""]

    for section in INCLUDED_ROOTS:

        folder = ROOT / section

        if not folder.exists():
            continue

        lines.append(f"{section}/")

        def walk(path, prefix=""):

            entries = []

            for item in sorted(
                path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())
            ):

                if is_ignored(item):
                    continue

                entries.append(item)

            for idx, item in enumerate(entries):

                last = idx == len(entries) - 1

                connector = "└── " if last else "├── "

                lines.append(f"{prefix}{connector}{item.name}")

                if item.is_dir():

                    extension = "    " if last else "│   "

                    walk(item, prefix + extension)

        walk(folder)

        lines.append("")

    return "\n".join(lines)


# =============================================================================
# PYTHON METADATA
# =============================================================================


def extract_metadata(file_path):

    result = {
        "classes": [],
        "functions": [],
        "imports": [],
        "module_doc": None,
    }

    try:

        source = file_path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        tree = ast.parse(source)

        result["module_doc"] = ast.get_docstring(tree)

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for name in node.names:

                    result["imports"].append(name.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:

                    result["imports"].append(node.module)

            elif isinstance(node, ast.ClassDef):

                result["classes"].append(
                    {
                        "name": node.name,
                        "doc": ast.get_docstring(node),
                    }
                )

            elif isinstance(node, ast.FunctionDef):

                result["functions"].append(
                    {
                        "name": node.name,
                        "doc": ast.get_docstring(node),
                    }
                )

    except Exception as e:
        result["error"] = str(e)
        try:
            PARSE_ERRORS.append((str(file_path.relative_to(ROOT)), str(e)))
        except Exception:
            pass

    result["imports"] = sorted(set(result["imports"]))

    return result


# =============================================================================
# FILE DISCOVERY
# =============================================================================


def get_python_files():

    files = []

    for root_name in INCLUDED_ROOTS:

        root = ROOT / root_name

        if not root.exists():
            continue

        for file in root.rglob("*.py"):

            if is_ignored(file):
                continue

            files.append(file)

    return sorted(files)


# =============================================================================
# DEPENDENCIES
# =============================================================================


def build_dependency_map(files):

    deps = defaultdict(list)

    for file in files:

        rel = file.relative_to(ROOT)

        meta = extract_metadata(file)

        for imp in meta["imports"]:

            if imp.startswith("src."):

                deps[str(rel)].append(imp)

    return deps


# =============================================================================
# CONFIG FILES
# =============================================================================


def existing_configs():

    result = []

    for name in CONFIG_FILES:

        path = ROOT / name

        if path.exists():
            result.append(path)

    return result


# =============================================================================
# REPORT
# =============================================================================


def write_report():

    py_files = get_python_files()
    deps = build_dependency_map(py_files)
    tree = build_tree()
    stats = project_stats(py_files)
    business_docs = read_docs()

    dependency_count = sum(len(v) for v in deps.values())

    with open(
        OUTPUT,
        "w",
        encoding="utf-8",
    ) as f:

        f.write("# PROJECT KNOWLEDGE BASE\n\n")

        f.write(f"Gerado em: " f"{datetime.now():%Y-%m-%d %H:%M:%S}\n\n")

        f.write("---\n\n")

        f.write("## Estatísticas\n\n")

        f.write(f"- Scripts Python: {len(py_files)}\n")

        f.write(f"- Classes: {stats['classes']}\n")

        f.write(f"- Funções: {stats['functions']}\n")

        f.write(f"- Dependências internas: " f"{dependency_count}\n")

        f.write(f"- Arquivos de configuração: " f"{len(existing_configs())}\n\n")

        f.write("---\n\n")

        f.write("## Estrutura do Projeto\n\n")

        f.write("```text\n")
        f.write(tree)
        f.write("\n```\n\n")

        f.write("---\n\n")

        f.write("## Arquivos de Configuração\n\n")

        for cfg in existing_configs():
            f.write(f"- {cfg.relative_to(ROOT)}\n")

        f.write("\n---\n\n")

        f.write("## Visão Arquitetural\n\n")

        f.write("### APIs\n\n")
        f.write("- src/api/bcb_client.py\n")
        f.write("- src/api/sidra_client.py\n")
        f.write("- src/api/sgs_series.py\n\n")

        f.write("\n---\n\n")

        f.write("## Fluxo de Dados\n\n")

        f.write("## Mapa de Dependências\n\n")

        for file, imports in sorted(deps.items()):

            f.write(f"### {file}\n\n")

            if not imports:

                f.write("Sem dependências internas.\n\n")
                continue

            for imp in imports:

                f.write(f"- {imp}\n")

            f.write("\n")

        f.write("---\n\n")

        f.write("## Documentação Funcional\n\n")

        for doc in business_docs:

            f.write(f"### {doc['name']}\n\n")

            f.write("```markdown\n")

            f.write(doc["content"])

            f.write("\n```\n\n")

        f.write("---\n\n")

        f.write("## Catálogo de Scripts\n\n")

        for py in py_files:

            rel = py.relative_to(ROOT)

            meta = extract_metadata(py)

            f.write(f"# {rel}\n\n")

            if meta.get("module_doc"):

                f.write("## Descrição\n\n")

                f.write(meta["module_doc"])

                f.write("\n\n")

            if meta["imports"]:

                f.write("## Imports\n\n")

                for imp in meta["imports"]:

                    f.write(f"- {imp}\n")

                f.write("\n")

            if meta["classes"]:

                f.write("## Classes\n\n")

                for cls in meta["classes"]:

                    f.write(f"### {cls['name']}\n\n")

                    if cls["doc"]:
                        f.write(cls["doc"] + "\n\n")

            if meta["functions"]:

                f.write("## Funções\n\n")

                for fn in meta["functions"]:

                    f.write(f"### {fn['name']}()\n\n")

                    if fn["doc"]:
                        f.write(fn["doc"] + "\n\n")

            f.write("---\n\n")

        if PARSE_ERRORS:
            f.write("## Erros de Parsing\n\n")

            for file, err in PARSE_ERRORS:
                f.write(f"- {file}: {err}\n")
            f.write("\n")

    print(f"\nArquivo gerado:\n{OUTPUT}\n")


# =============================================================================
# métricas
# =============================================================================


def project_stats(py_files):

    stats = {
        "classes": 0,
        "functions": 0,
    }

    for py in py_files:

        meta = extract_metadata(py)

        stats["classes"] += len(meta["classes"])

        stats["functions"] += len(meta["functions"])

    return stats


# =============================================================================
# read_docs
# =============================================================================


def read_docs():

    docs = []

    for name in DOCS_FILES:

        path = ROOT / "docs" / name

        if not path.exists():
            continue

        text = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        docs.append(
            {
                "name": name,
                "content": text[:3000],
            }
        )

    return docs


if __name__ == "__main__":
    write_report()
