#!/usr/bin/env python3
"""
Gera NOTEBOOKS_KNOWLEDGE_BASE.md

Objetivo:
- Catalogar notebooks
- Reconstruir roadmap
- Extrair markdowns principais
- Extrair bibliotecas utilizadas
"""

import ast
import re
from datetime import datetime
from pathlib import Path

import nbformat
import pathspec

# =============================================================================
# CONFIG
# =============================================================================

ROOT = Path(__file__).resolve().parents[1]

NOTEBOOKS_DIR = ROOT / "notebooks"

OUTPUT = ROOT / "docs" / "_NOTEBOOKS_KNOWLEDGE_BASE.md"


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


def is_ignored(path):

    if GIT_SPEC is None:
        return False

    try:
        rel = path.relative_to(ROOT).as_posix()
        return GIT_SPEC.match_file(rel)

    except Exception:
        return False


# =============================================================================
# NOTEBOOKS
# =============================================================================


def notebook_files():

    files = []

    for file in NOTEBOOKS_DIR.rglob("*.ipynb"):

        if is_ignored(file):
            continue

        files.append(file)

    return sorted(files)


def load_notebook(path):

    return nbformat.read(
        path,
        as_version=4,
    )


# =============================================================================
# EXTRAÇÃO
# =============================================================================


def get_title_candidates(markdowns):

    titles = []

    for text in markdowns:

        found = re.findall(
            r"^#+\s+(.*)",
            text,
            re.MULTILINE,
        )

        for item in found:

            item = item.strip()

            if item:
                titles.append(item)

    return titles


def get_markdowns(nb):

    return [cell.source for cell in nb.cells if cell.cell_type == "markdown"]


def first_markdown(markdowns):

    if not markdowns:
        return ""

    text = markdowns[0]

    return text[:1500]


def detect_imports(nb):

    libs = set()

    for cell in nb.cells:

        if cell.cell_type != "code":
            continue

        try:

            tree = ast.parse(cell.source)

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for n in node.names:
                        libs.add(n.name.split(".")[0])

                elif isinstance(node, ast.ImportFrom):

                    if node.module:
                        libs.add(node.module.split(".")[0])

        except Exception:
            continue

    return sorted(libs)


def summarize_notebook(path):

    nb = load_notebook(path)

    markdowns = get_markdowns(nb)

    code_cells = [c for c in nb.cells if c.cell_type == "code"]

    return {
        "path": path,
        "total_cells": len(nb.cells),
        "markdown_cells": len(markdowns),
        "code_cells": len(code_cells),
        "titles": get_title_candidates(markdowns),
        "imports": detect_imports(nb),
        "preview": first_markdown(markdowns),
    }


# =============================================================================
# ROADMAP
# =============================================================================


def split_roadmap(notebooks):

    main = []
    future = []

    for nb in notebooks:

        rel = nb.relative_to(ROOT)

        if "off" in rel.parts:
            future.append(rel)
        else:
            main.append(rel)

    return main, future


# =============================================================================
# REPORT
# =============================================================================


def write_report():

    notebooks = notebook_files()

    main, future = split_roadmap(notebooks)

    summaries = [summarize_notebook(nb) for nb in notebooks]

    with open(OUTPUT, "w", encoding="utf-8") as f:

        f.write("# NOTEBOOKS KNOWLEDGE BASE\n\n")

        f.write(f"Gerado em: " f"{datetime.now():%Y-%m-%d %H:%M:%S}\n\n")

        f.write("---\n\n")

        f.write("## Estatísticas\n\n")

        f.write(f"- Notebooks encontrados: " f"{len(notebooks)}\n")

        f.write(f"- Roadmap principal: " f"{len(main)}\n")

        f.write(f"- Roadmap futuro: " f"{len(future)}\n\n")

        f.write("---\n\n")

        #
        # ROADMAP PRINCIPAL
        #

        f.write("## Roadmap Principal\n\n")

        for nb in main:

            f.write(f"- `{nb}`\n")

        f.write("\n---\n\n")

        #
        # ROADMAP FUTURO
        #

        f.write("## Roadmap Futuro (OFF)\n\n")

        for nb in future:

            f.write(f"- `{nb}`\n")

        f.write("\n---\n\n")

        #
        # DETALHAMENTO
        #

        f.write("# Catálogo de Notebooks\n\n")

        for item in summaries:

            rel = item["path"].relative_to(ROOT)

            f.write(f"## {rel}\n\n")

            f.write(f"- Total de células: " f"{item['total_cells']}\n")

            f.write(f"- Markdown: " f"{item['markdown_cells']}\n")

            f.write(f"- Código: " f"{item['code_cells']}\n\n")

            #
            # TÍTULOS
            #

            if item["titles"]:

                f.write("### Títulos Detectados\n\n")

                for title in item["titles"][:20]:

                    f.write(f"- {title}\n")

                f.write("\n")

            #
            # IMPORTS
            #

            if item["imports"]:

                f.write("### Bibliotecas\n\n")

                for lib in item["imports"]:

                    f.write(f"- {lib}\n")

                f.write("\n")

            #
            # PREVIEW
            #

            if item["preview"]:

                f.write("### Primeira Célula Markdown\n\n")

                f.write("```markdown\n")

                f.write(item["preview"])

                f.write("\n```\n\n")

            f.write("---\n\n")

    print(f"\nArquivo gerado:\n{OUTPUT}\n")


if __name__ == "__main__":
    write_report()
