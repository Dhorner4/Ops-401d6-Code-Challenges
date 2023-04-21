$currentUsername = $env:USERNAME
$newPassword = Read-Host -Prompt "Enter a new password" -AsSecureString

$success = $false
do {
    try {
        $user = [ADSI]"WinNT://$env:COMPUTERNAME/$currentUsername,user"
        $user.SetPassword([System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($newPassword)))
        $user.SetInfo()
        Write-Host "Password has been set for user $currentUsername."
        $success = $true
    }
    catch {
        Write-Host "Failed to set password for user $currentUsername. Error message: $($_.Exception.Message)"
        $newPassword = Read-Host -Prompt "Enter a new password" -AsSecureString
    }
} while (!$success)

# Check if SMB1 is currently enabled
if ((Get-SmbServerConfiguration).EnableSMB1Protocol) {
    # Disable SMB1
    Set-SmbServerConfiguration -EnableSMB1Protocol $false

    # Output a message indicating that SMB1 has been disabled
    Write-Host "SMB1 protocol has been disabled."
} else {
    # Output a message indicating that SMB1 is already disabled
    Write-Host "SMB1 protocol is already disabled."
}