# Setup Streamlit virtual environment for VNBR-RCC RW project
# Run from project root: .\setup-streamlit-env.ps1

$envName = "venv-streamlit"
$reqFile = "requirements-streamlit.txt"

Write-Host "Creating virtual environment: $envName" -ForegroundColor Cyan
python -m venv $envName

Write-Host "Activating and installing dependencies..." -ForegroundColor Cyan
& ".\$envName\Scripts\Activate.ps1"
pip install --upgrade pip
pip install -r $reqFile

Write-Host "`nDone! To use this environment:" -ForegroundColor Green
Write-Host "  .\$envName\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host "  streamlit run streamlit_app.py" -ForegroundColor Yellow
