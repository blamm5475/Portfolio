#USE AT YOUR OWN RISK
# Get the list of all files in the current directory
$fileList = Get-ChildItem -File

# Create a hashtable to store file hashes and paths
$fileHashes = @{}

# Initialize a counter for the processed files
$processedFiles = 0

# Loop through each file and calculate its hash
foreach ($file in $fileList) {
    $processedFiles++
    Write-Host "Processing file $processedFiles of $($fileList.Count) - $($file.Name)"

    $fileHash = (Get-FileHash -Path $file.FullName -Algorithm SHA256).Hash

    if ($fileHashes.ContainsKey($fileHash)) {
        # Delete the duplicate file
        Write-Host "Deleting duplicate file: $($file.Name)"
        Remove-Item -Path $file.FullName -Force
    }
    else {
        # Store the file hash and path in the hashtable
        $fileHashes[$fileHash] = $file.FullName
    }
}

Write-Host "Script finished processing all files."