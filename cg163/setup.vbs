Set FS = CreateObject("Scripting.FileSystemObject")

'steam游戏文件夹重命名操作
FS.DeleteFolder("D:\steamapps\steamapps")
FS.MoveFolder "D:\steamapps\steamapps_tran", "D:\steamapps\steamapps"
'epic游戏文件夹重命名操作
FS.DeleteFolder("D:\EpicGames")
FS.MoveFolder "D:\EpicGames_tran", "D:\EpicGames"
'orgin游戏文件夹重命名操作
FS.DeleteFolder("D:\origin games")
FS.MoveFolder "D:\origin games_tran", "D:\origin games"

Set objShell = CreateObject("Wscript.Shell")
objShell.Run "C:\users\Public\Desktop\网易UU加速器网吧版.lnk"
objShell.Run "C:\users\Public\Desktop\Steam.lnk"

Set Post = CreateObject("Msxml2.XMLHTTP")
Set aGet = CreateObject("ADODB.Stream")
Function DownloadFile(url,locate)
Post.Open "GET",url,0
Post.Send()
aGet.Mode = 3
aGet.Type = 1
aGet.Open()
aGet.Write(Post.responseBody)
aGet.SaveToFile locate,2
aGet.Close
End Function

DownloadFile "https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/releases/download/v2.2.6/Heroic-Setup-2.2.6.exe","C:\users\netease\Heroic-Setup-2.2.6.exe"

DownloadFile "https://github.com/cheat-engine/cheat-engine/releases/download/7.4/CheatEngine74.exe","C:\users\netease\CheatEngine74.exe"

DownloadFile "https://github.com/AmazingPP/subVerison_GTAV_Hack/releases/download/v1.3.5.2/subVersion_1.3.5.2.zip","C:\users\netease\subVersion_1.3.5.2.zip"

DownloadFile "https://cdn.discordapp.com/attachments/925878429054820402/928635764693168128/tranny-garbage.zip","C:\users\netease\tranny-garbage.zip"

DownloadFile "https://stand.gg/dl/launchpad/1.8/Stand%20Launchpad.exe","C:\users\netease\Stand_Launchpad.exe"
