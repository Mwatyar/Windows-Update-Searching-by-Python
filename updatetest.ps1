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
    $Result | Out-File .\Updatelist.txt -Append
    }



exit 