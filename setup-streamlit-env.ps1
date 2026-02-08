# Setup Streamlit virtual environment for VNBR project
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
Write-Host "  streamlit run Pages\app_mbook.py" -ForegroundColor Yellow
Write-Host "  # or: streamlit run Pages\app_progress.py" -ForegroundColor Gray
Write-Host "  # or: streamlit run Pages\app_overlap_gap.py" -ForegroundColor Gray
Write-Host "  # or: streamlit run Pages\app_timeline.py" -ForegroundColor Gray
