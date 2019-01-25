# 0.このセッションが閉じるまで実行ポリシー変更
Set-ExecutionPolicy -Scope Process -ExecutionPolicy AllSigned -Force


# 1. ログの記録を開始する
$log = ".\$($env:ComputerName)_$(date -f yyyyMMdd).txt"
Start-Transcript $log
$Env:ComputerName
$Env:UserName
date

# 2. Windows Update を確認するセッションを開始
$updateSession = New-Object -com Microsoft.Update.Session

# 3. Windows Update の検索
$searcher = $updateSession.CreateUpdateSearcher()
$searchResult = $searcher.search("IsInstalled=0 and Type='software'")

# 4. Windows Update の結果確認
$searchResult.Updates | % { $_.title -replace ".*(KB\d+).*", "`$1`t$&" }

# 5. 手作業が不要な項目だけを抽出する（通常は検索結果すべて）
$updatesToDownload = New-Object -com Microsoft.Update.UpdateColl
$searchResult.Updates | ? { -not $_.InstallationBehavior.CanRequestUserInput } | ? { $_.EulaAccepted } | % { [void]$updatesToDownload.add($_) }

# 6. 終了
exit
