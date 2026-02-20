$images = @(
    @{Old="pexels-heftiba-1194420.jpg"; New="mural-1.jpg"},
    @{Old="pexels-heftiba-1194420 (1).jpg"; New="mural-2.jpg"},
    @{Old="pexels-mccutcheon-1209843.jpg"; New="mural-3.jpg"},
    @{Old="pexels-steve-1183992.jpg"; New="mural-4.jpg"}
)

$sourcePath = "static\images"
$destPath = "static\images\artwork"

foreach ($img in $images) {
    $source = Join-Path $sourcePath $img.Old
    $dest = Join-Path $destPath $img.New
    
    if (Test-Path $source) {
        Move-Item -Path $source -Destination $dest -Force
        Write-Host "Moved $($img.Old) to $($img.New)"
    } else {
        Write-Host "File not found: $($img.Old)"
    }
}

Write-Host "Done! All murals renamed and moved to artwork folder."
