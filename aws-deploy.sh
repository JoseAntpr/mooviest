# Creates a new branch only to perform the deployment
git branch aws-deploy
git checkout aws-deploy

# Sets deployment flag to true
sed -i -- 's/DEPLOYMENT = False/DEPLOYMENT = True/g' mooviest/settings.py
rm mooviest/settings.py--

# Replaces "settings_develop" to "settings" in wsgi.py y manage.py
sed -i -- 's/settings_develop/settings/g' mooviest/wsgi.py
sed -i -- 's/settings_develop/settings/g' manage.py
rm mooviest/wsgi.py--
rm manage.py--

echo "Reemplazados 'settings_develop' por 'settings' en wsgi.py y manage.py"
seq  -f "-" -s '' "$(tput cols)";

# Commit changes to deploy
git add .
git commit -m "Changed settings paths for aws-deploy"
seq  -f "-" -s '' "$(tput cols)";

# Deploy to Amazon Web Services
echo "Desplegando en Elastic Beanstalk de Amazon..."
seq  -f "-" -s '' "$(tput cols)";

if eb deploy test; then (
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
