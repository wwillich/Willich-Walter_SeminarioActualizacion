# Reproduce las 3 situaciones problema de la Clase 03 sin tocar GitHub.
# Cada "remoto" es un repo bare en una carpeta temporal, que hace de GitHub.
# Uso: .\reproducir_situaciones.ps1  (o con -Situacion 1, 2 o 3)

param([ValidateSet(0, 1, 2, 3)][int]$Situacion = 0)

$base = Join-Path $env:TEMP "clase03_situaciones"
if (Test-Path $base) { Remove-Item -Recurse -Force $base }
New-Item -ItemType Directory $base | Out-Null

function Titulo($texto) { Write-Host "`n==== $texto ====" -ForegroundColor Yellow }
function Paso($texto)   { Write-Host "`n> $texto" -ForegroundColor Cyan }

# ---------------------------------------------------------------------------
function Situacion1 {
    Titulo "SITUACION 1 - README duplicado"
    $remoto = "$base\s1_remoto.git"
    git init -q --bare -b main $remoto

    Paso "GitHub crea el repo CON README (simulado con un clon que sube un README)"
    git clone -q $remoto "$base\s1_github" 2>$null
    Set-Location "$base\s1_github"
    "# Repo de prueba (README creado por GitHub)" | Out-File -Encoding utf8 README.md
    git add README.md; git commit -q -m "Initial commit"; git push -q origin main

    Paso "Aparte, un repo local nuevo con git init y su propio README"
    New-Item -ItemType Directory "$base\s1_local" | Out-Null
    Set-Location "$base\s1_local"
    git init -q -b main
    "# Mi proyecto (README local)" | Out-File -Encoding utf8 README.md
    git add README.md; git commit -q -m "Primer commit local"
    git remote add origin $remoto

    Paso "git push -> lo rechaza: el remoto tiene un commit que yo no tengo"
    git push origin main

    Paso "git pull sin la opcion -> se niega a unir historias que no tienen nada en comun"
    git pull --no-rebase origin main

    Paso "Solucion: git pull con --allow-unrelated-histories -> conflicto en README.md"
    git pull --no-rebase origin main --allow-unrelated-histories

    Paso "Resuelvo el conflicto quedandome con un solo README y subo"
    "# Mi proyecto`n`nREADME unificado despues de resolver el conflicto." | Out-File -Encoding utf8 README.md
    git add README.md; git commit -q -m "Unifica README local y remoto"
    git push origin main
    git log --oneline --graph --all
}

# ---------------------------------------------------------------------------
function Situacion2 {
    Titulo "SITUACION 2 - Carpeta sin ignorar"
    $remoto = "$base\s2_remoto.git"
    git init -q --bare -b main $remoto
    New-Item -ItemType Directory "$base\s2_local" | Out-Null
    Set-Location "$base\s2_local"
    git init -q -b main
    git remote add origin $remoto

    Paso "Creo datos_prueba/ y la subo SIN ponerla en el .gitignore"
    New-Item -ItemType Directory datos_prueba | Out-Null
    "id,valor`n1,10" | Out-File -Encoding utf8 datos_prueba\datos.csv
    git add .; git commit -q -m "Sube datos_prueba por error"; git push -q -u origin main
    Write-Host "Archivos en el remoto:"; git ls-tree -r --name-only origin/main

    Paso "Agrego datos_prueba/ al .gitignore y cambio el archivo: Git lo sigue viendo"
    "datos_prueba/" | Out-File -Encoding utf8 .gitignore
    "id,valor`n1,10`n2,20" | Out-File -Encoding utf8 datos_prueba\datos.csv
    git status --short

    Paso "Solucion: git rm -r --cached (lo saca del repo, no de mi disco)"
    git rm -r -q --cached datos_prueba
    git add .gitignore
    git commit -q -m "Deja de trackear datos_prueba"
    git push -q
    Write-Host "Archivos en el remoto:"; git ls-tree -r --name-only origin/main
    Write-Host ("Sigue en mi disco: " + (Test-Path datos_prueba\datos.csv))
}

# ---------------------------------------------------------------------------
function Situacion3 {
    Titulo "SITUACION 3 - Ramas master / main"
    $remoto = "$base\s3_remoto.git"
    git init -q --bare -b main $remoto

    Paso "Repo local creado con master como rama por defecto"
    # En clase se hizo con: git config --global init.defaultBranch master
    # Aca uso -b master para no cambiar la configuracion global
    New-Item -ItemType Directory "$base\s3_local" | Out-Null
    Set-Location "$base\s3_local"
    git init -q -b master
    "# Proyecto" | Out-File -Encoding utf8 README.md
    git add .; git commit -q -m "Commit inicial"
    git remote add origin $remoto

    Paso "git push -u origin master -> en el remoto aparece una rama master"
    git push -q -u origin master
    git ls-remote --heads origin

    Paso "Solucion: renombro a main, subo main y borro master del remoto"
    git branch -m master main
    git push -q -u origin main
    git push -q origin --delete master
    git ls-remote --heads origin
    git branch -vv
}

# ---------------------------------------------------------------------------
$inicio = Get-Location
try {
    if ($Situacion -in 0, 1) { Situacion1 }
    if ($Situacion -in 0, 2) { Situacion2 }
    if ($Situacion -in 0, 3) { Situacion3 }
} finally {
    Set-Location $inicio
}
Write-Host "`nListo. Los repos de prueba quedaron en $base" -ForegroundColor Green
