#!/bin/bash
set -e

echo "=============================================="
echo "🚀 Iniciando configuração automática do Superset"
echo "=============================================="

# ---------------------------------------------------------
# 1. Aguarda o Superset iniciar completamente
# ---------------------------------------------------------
echo "⏳ Aguardando Superset iniciar..."
sleep 10

# ---------------------------------------------------------
# 2. Aplica roles e permissões
# ---------------------------------------------------------

# ---------------------------------------------------------
# 3. Importa conexões de banco (PostgreSQL)
# ---------------------------------------------------------
if [ -f /app/init/databases.yaml ]; then
    echo "🗄  Importando conexões de banco..."
    superset import-datasources -p /app/init/databases.yaml
else
    echo "⚠️ databases.yaml não encontrado, pulando..."
fi

# ---------------------------------------------------------
# 4. Importa dashboards (JSON)
# ---------------------------------------------------------
if [ -d /app/init/dashboards ]; then
    echo "📊 Importando dashboards..."
    for file in /app/init/dashboards/*.json; do
        if [ -f "$file" ]; then
            echo "   → Dashboard: $file"
            superset import-dashboards -p "$file"
        fi
    done
else
    echo "⚠️ Diretório dashboards/ não encontrado, pulando..."
fi

# ---------------------------------------------------------
# 5. Recarrega metadados
# ---------------------------------------------------------
echo "🔄 Atualizando metadados..."
superset refresh-datasources-cache

# ---------------------------------------------------------
# 6. Finalização
# ---------------------------------------------------------
echo "=============================================="
echo "✅ Superset configurado com sucesso!"
echo "=============================================="
