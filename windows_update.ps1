# 0.このセッションが閉じるまで実行ポリシー変更
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted -Force

# COMオブジェクトの作成。
$Session = New-Object -ComObject Microsoft.Update.Session
# 更新ファイルを探索するオブジェクトを作成。
$Searcher = $Session.CreateUpdateSearcher()

# テキストファイルの初期化
New-Item .\Updatelist.txt -ItemType file -Force 

Write-Host '処理を開始します。しばらくお待ちください...'
# 更新ファイルを探索。（未インストールの更新ファイルを探索）
#$Results = $Searcher.Search("IsInstalled = 0 And Type = 'software'")

$Enter = "`r`n"

$BStart = "===== 未インストールの更新 ====="
$BEnd =   "== 未インストール更新表示終了 =="


$BStart | Out-File .\Updatelist.txt -Append

$Results = $Searcher.Search("IsInstalled = 0")
foreach ($Result in $Results.Updates) {
    $Result.Title | Out-File .\Updatelist.txt -Append
    }

$BEnd | Out-File .\Updatelist.txt -Append

$Enter | Out-File .\Updatelist.txt -Append

# 更新されたファイルの検索。

$AStart = "==== インストール済みの更新 ===="
$AEnd =   "==インストール済み更新表示終了=="

$AStart | Out-File .\Updatelist.txt -Append

$Results = $Searcher.Search("IsInstalled = 1")
foreach ($Result in $Results.Updates) {
    $Result.Title | Out-File .\Updatelist.txt -Append
    }

$AEnd | Out-File .\Updatelist.txt -Append

Write-Host '処理が終了しました。'
exit 