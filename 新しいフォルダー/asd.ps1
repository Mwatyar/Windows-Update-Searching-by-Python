# 0.���̃Z�b�V����������܂Ŏ��s�|���V�[�ύX
Set-ExecutionPolicy -Scope Process -ExecutionPolicy AllSigned -Force


# 1. ���O�̋L�^���J�n����
$log = ".\$($env:ComputerName)_$(date -f yyyyMMdd).txt"
Start-Transcript $log
$Env:ComputerName
$Env:UserName
date

# 2. Windows Update ���m�F����Z�b�V�������J�n
$updateSession = New-Object -com Microsoft.Update.Session

# 3. Windows Update �̌���
$searcher = $updateSession.CreateUpdateSearcher()
$searchResult = $searcher.search("IsInstalled=0 and Type='software'")

# 4. Windows Update �̌��ʊm�F
$searchResult.Updates | % { $_.title -replace ".*(KB\d+).*", "`$1`t$&" }

# 5. ���Ƃ��s�v�ȍ��ڂ����𒊏o����i�ʏ�͌������ʂ��ׂāj
$updatesToDownload = New-Object -com Microsoft.Update.UpdateColl
$searchResult.Updates | ? { -not $_.InstallationBehavior.CanRequestUserInput } | ? { $_.EulaAccepted } | % { [void]$updatesToDownload.add($_) }

# 6. �I��
exit