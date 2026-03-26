# ============================================================
# Script de déploiement - Environnement ML/DL
# ============================================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Déploiement de l'environnement ML/DL  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# --- Vérification Python ---
Write-Host "`n[1/4] Vérification de Python..." -ForegroundColor Yellow
$python = py -3.11 --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERREUR : Python 3.11 non trouvé. Installez-le depuis https://python.org" -ForegroundColor Red
    exit 1
}
Write-Host "OK : $python" -ForegroundColor Green

# --- Vérification Git ---
Write-Host "`n[2/4] Vérification de Git..." -ForegroundColor Yellow
$git = git --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERREUR : Git non trouvé. Installez-le depuis https://git-scm.com" -ForegroundColor Red
    exit 1
}
Write-Host "OK : $git" -ForegroundColor Green

# --- Vérification Docker ---
Write-Host "`n[3/4] Vérification de Docker..." -ForegroundColor Yellow
$docker = docker --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERREUR : Docker non trouvé. Installez Docker Desktop." -ForegroundColor Red
    exit 1
}
Write-Host "OK : $docker" -ForegroundColor Green

# --- Environnement virtuel ---
Write-Host "`n[4/4] Création de l'environnement virtuel..." -ForegroundColor Yellow
if (!(Test-Path ".venv")) {
    py -3.11 -m venv .venv
    Write-Host "OK : Environnement virtuel créé" -ForegroundColor Green
} else {
    Write-Host "OK : Environnement virtuel déjà existant" -ForegroundColor Green
}

# --- Activation et installation des dépendances ---
Write-Host "`nInstallation des dépendances Python..." -ForegroundColor Yellow
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
Write-Host "OK : Dépendances installées" -ForegroundColor Green

# --- Lancement Docker ---
Write-Host "`nLancement des containers Docker..." -ForegroundColor Yellow
docker-compose up -d --build
Write-Host "OK : Containers lancés" -ForegroundColor Green

# --- Résumé ---
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Environnement prêt !" -ForegroundColor Cyan
Write-Host "  JupyterLab  : http://localhost:8888" -ForegroundColor Cyan
Write-Host "  SonarQube   : http://localhost:9000" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan