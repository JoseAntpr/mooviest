# Creates a new branch only to perform the deployment
git branch aws-deploy

# Sets Debug to false
./replace-string-subfolders-extension.sh py "DEBUG = True" "DEBUG = False"

# Replaces "mooviest.settings_develop" to "mooviest_settings_deploy" in all .py files
./replace-string-subfolders-extension.sh py mooviest.settings_develop mooviest.settings
echo "Reemplazados 'mooviest.settings_develop' por 'mooviest.settings' en archivos .py"
seq  -f "-" -s '' "$(tput cols)";

# Commit changes to deploy
git add .
git commit -m "Changed settings paths for aws-deploy"
seq  -f "-" -s '' "$(tput cols)";

# Deploy to Amazon Web Services
echo "Desplegando en Elastic Beanstalk de Amazon..."
seq  -f "-" -s '' "$(tput cols)";

if eb deploy test; then (

    # Replaces "mooviest.settings" to "mooviest.settings_develop" in all .py files
    ./replace-string-subfolders-extension.sh py mooviest.settings mooviest.settings_develop

    # Commit changes to previous state
    git add .
    git commit -m "Changed to previous settings paths"
    seq  -f "-" -s '' "$(tput cols)";
    echo "Cadenas de settings reestablecidas al estado previo"
    echo "Despliegue en Amazon EB completado"
    echo "Volviendo a la rama develop"
    git checkout develop
    git branch -D aws-deploy
    )
else
    seq  -f "!" -s '' "$(tput cols)";
    echo "Despliegue fallido. Las cadenas reemplazadas de settings no se restauraron al estado previo"
    echo "Solucionar problemas de despliegue y ejecutar aws-deploy de nuevo"
    seq  -f "¡" -s '' "$(tput cols)";
fi
