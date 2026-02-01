#!/bin/bash

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Actualizador de Menú Diario ===${NC}"
echo "Este script subirá los cambios que hayas hecho en index.html a Internet."
echo ""

# Ir al directorio correcto
cd /home/joel/Documentos/anti/restaurante

# Verificar si hay cambios
if [[ -z $(git status -s) ]]; then
    echo "No hay cambios pendientes para subir."
    echo "Asegúrate de haber guardado el archivo index.html antes de ejecutar esto."
    exit 0
fi

# Mostrar cambios
echo -e "${GREEN}Se detectaron cambios en los siguientes archivos:${NC}"
git status -s
echo ""

# Confirmar
read -p "¿Quieres publicar estos cambios ahora? (s/n): " confirm
if [[ $confirm != "s" && $confirm != "S" ]]; then
    echo "Cancelado."
    exit 0
fi

echo ""
echo "Subiendo cambios a GitHub..."

# Comandos de Git
git add .
git commit -m "Actualización del menú: $(date '+%Y-%m-%d %H:%M')"
git push

echo ""
echo -e "${GREEN}¡Éxito! Los cambios se han subido.${NC}"
echo "Tu menú se actualizará en unos instantes en:"
echo "https://a242844jr-joel.github.io/restaurante-menu/"
echo ""
read -p "Presiona Enter para salir..."
