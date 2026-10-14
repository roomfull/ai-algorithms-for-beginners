[CmdletBinding()]
param(
    [string]$PythonExe = ""
)

$ErrorActionPreference = "Stop"
$projectRoot = $PSScriptRoot
$venvRoot = Join-Path $projectRoot ".venv"
$venvPython = Join-Path $venvRoot "Scripts\python.exe"
$installTemp = Join-Path $projectRoot ".setup-tmp"
$savedTemp = $env:TEMP
$savedTmp = $env:TMP

function Assert-LastExit([string]$Step) {
    if ($LASTEXITCODE -ne 0) {
        throw "$Step failed (exit code $LASTEXITCODE)."
    }
}

try {
    # Keep temporary wheels inside the project, including in restricted shells.
    New-Item -ItemType Directory -Force -Path $installTemp | Out-Null
    $env:TEMP = $installTemp
    $env:TMP = $installTemp

    if (-not (Test-Path -LiteralPath $venvPython)) {
        if (-not $PythonExe) {
            $localPython = Join-Path $env:APPDATA "uv\python\cpython-3.11-windows-x86_64-none\python.exe"
            if (Test-Path -LiteralPath $localPython) {
                $PythonExe = $localPython
            } else {
                $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
                if ($pythonCommand) { $PythonExe = $pythonCommand.Source }
            }
        }
        if (-not $PythonExe) {
            throw "Python 3.11 not found. Run .\setup.ps1 -PythonExe 'C:\path\to\python.exe'."
        }
        & $PythonExe -c "import sys; assert sys.version_info[:2] == (3, 11), 'Python 3.11 is required'"
        Assert-LastExit "Python version check"
        & $PythonExe -m venv $venvRoot
        Assert-LastExit "Virtual environment creation"
    }

    & $venvPython -c "import sys; assert sys.version_info[:2] == (3, 11), 'Existing .venv must use Python 3.11'; assert sys.prefix != sys.base_prefix, 'An isolated venv is required'"
    Assert-LastExit "Virtual environment check"
    & $venvPython -m pip --version
    if ($LASTEXITCODE -ne 0) {
        & $venvPython -m ensurepip --upgrade --default-pip
        Assert-LastExit "pip bootstrap"
    }
    & $venvPython -m pip install --disable-pip-version-check --no-cache-dir -r (Join-Path $projectRoot "requirements.txt")
    Assert-LastExit "Dependency installation"
    & $venvPython -c "import sys, numpy; assert numpy.__version__ == '2.2.6'; print('Python:', sys.version.split()[0]); print('NumPy:', numpy.__version__); print('Interpreter:', sys.executable)"
    Assert-LastExit "Dependency verification"
    Write-Host 'Ready. Use .\.venv\Scripts\python.exe check.py --list from the project root.'
} finally {
    $env:TEMP = $savedTemp
    $env:TMP = $savedTmp
}
