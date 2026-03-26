#!/bin/bash
#Script de deploiement - Environnoment ML/DL - Debian/Linux
#==========================================================
 
echo "Deploiement de l'environnement ML/DL"
echo"======================================"
#Vérification python
echo"[1/4] Vérification de python..."
if! command -v python3 &> /dev/null; then
    echo"ERRREUR : Python3 non trouvé. Installaton.."
    sudo apt install -y python3 python3-pip python3-venv
fi
echo "OK: $(python3 --version)"
#Vérification Git 
echo"[2/4] Vérification de Git..."
if! command -v git &> /dev/null; then
   echo "Installation de Git..."
   sudo apt install -y git
fi 
echo "OK: $(git --version)"
#Vérification Docker 
echo "[3/4] Vérification de Docker ..."
if ! command -v docker &> /dev/numm; then 
    echo"Installation de Docker ..."
    sudo apt install -y docker.io docker-compose
    sudo usermod -aG docker $USER
fi
echo " OK: $(docker --version)"
# Environnement virtuel 
echo "[4/4] Création de l'environnement virtuel ..."
if [ ! -d " .venv" ]; then 
    python3 -m venv .venv
fi 
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "OK : Dépendances installées"
#Lancement Docker
echo "Lancement des containers Docker..."
docker-compose up -d --build
echo "OK : Containers lancés"


echo"======================================"
echo "   Environnement pret !"
echo "   JupyterLab : http://localhost:8888"
echo "   SonarQube  : http://localhost:9000"
echo "====================================="
EOF
