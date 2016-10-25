# Replaces "mooviest.settings_develop" to "mooviest_settings_deploy" in all .config files
./replace-string-subfolders-extension.sh config mooviest.settings_develop mooviest.settings_deploy
echo "Reemplazados 'mooviest.settings_develop' por 'mooviest_deploy' en archivos .config"
echo "---------------------------------------------"

# Replaces "mooviest.settings_develop" to "mooviest_settings_deploy" in all .py files
./replace-string-subfolders-extension.sh py mooviest.settings_develop mooviest.settings_deploy
echo "Reemplazados 'mooviest.settings_develop' por 'mooviest_deploy' en archivos .py"
echo "---------------------------------------------"

# Commit changes to deploy
git add .
git commit -m "Changed settings paths for aws-deploy"

# Deploy to Amazon Web Services
echo "Desplegando en Elastic Beanstalk de Amazon..."
echo "---------------------------------------------"
if eb deploy test; then (

    # Replaces "mooviest.settings_deploy" to "mooviest_settings_develop" in all .config files
    ./replace-string-subfolders-extension.sh config mooviest.settings_deploy mooviest.settings_develop

    # Replaces "mooviest.settings_deploy" to "mooviest_settings_develop" in all .py files
    ./replace-string-subfolders-extension.sh py mooviest.settings_deploy mooviest.settings_develop

    # Commit changes to previous state
    git add .
    git commit -m "Changed to previous settings paths"
    )
else
    echo "Despliegue fallido. Las cadenas reemplazadas de settings no se restauraron al estado previo"
    echo "Solucionar problemas de despliegue y ejecutar aws-deploy de nuevo"
fi
