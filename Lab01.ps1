# Dericus Horner
# Ops-401d6: Lab 01

# Main

# Check if Windows Defender is enabled
$defender = Get-MpComputerStatus
if ($defender.AntivirusEnabled -eq $false) {
    # Enable Windows Defender if it's disabled
    Set-MpPreference -DisableRealtimeMonitoring $false
}

# Start a Quick Scan
Start-MpScan -ScanType QuickScan

# Check the last scan time
$lastScanTime = Get-MpComputerStatus | Select-Object -ExpandProperty LastScanTime

Write-Output "Windows Defender scan complete. Last scan time: $lastScanTime."

# Done