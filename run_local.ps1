# run_local.ps1
$ErrorActionPreference = "Stop"

# 1) Пути
$Project = "C:\Users\User_\Desktop\robochi_site"
$Python  = Join-Path $Project "venv\Scripts\python.exe"

if (-not (Test-Path $Project)) { throw "Папка проекта не найдена: $Project" }
if (-not (Test-Path $Python))  { throw "Не найден Python из venv: $Python" }

Set-Location $Project

# 2) Автовыбор свободного порта, начиная с 8000
$port = 8000
while (Get-NetTCPConnection -State Listen -LocalPort $port -ErrorAction SilentlyContinue) {
  Write-Host "[WARN] Порт $port занят. Пробую следующий..."
  $port++
}
Write-Host "[INFO] Использую порт $port"

# 3) Миграции
& $Python manage.py migrate

# 4) Обновляем django_site, чтобы /admin и /sitemap.xml не падали
$domain = "127.0.0.1:$port"
$code = "from django.contrib.sites.models import Site; Site.objects.update_or_create(id=1, defaults={'domain':'$domain','name':'Localhost'})"
& $Python manage.py shell -c $code

# 5) Открываем браузер и запускаем сервер
Start-Process "http://127.0.0.1:$port/"
& $Python manage.py runserver $port
