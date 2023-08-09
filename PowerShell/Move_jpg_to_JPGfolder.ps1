#This script will look for jpg files in current directory and move them to a folder named JPG, it will create a folder if one does not exist
# Create the 'JPG' directory if it doesn't exist
$destinationDir = Join-Path $PSScriptRoot "JPG"
if (-not (Test-Path $destinationDir)) {
    New-Item -ItemType Directory -Path $destinationDir | Out-Null
}

# Get the list of all files ending in '.jpg' in the current directory
$jpgFiles = Get-ChildItem -File -Filter "*.jpg"

# Move each '.jpg' file to the 'JPG' directory
foreach ($jpgFile in $jpgFiles) {
    $destinationPath = Join-Path $destinationDir $jpgFile.Name
    Move-Item -Path $jpgFile.FullName -Destination $destinationPath -Force
    Write-Host "Moved $($jpgFile.Name) to 'JPG' folder"
}

Write-Host "Script finished moving '.jpg' files to 'JPG' folder."