Set FS = CreateObject("Scripting.FileSystemObject")

'steam游戏文件夹重命名操作
FS.DeleteFolder("D:\steamapps\steamapps")
FS.MoveFolder "D:\steamapps\steamapps_tran", "D:\steamapps\steamapps"

FS.DeleteFolder("D:\EpicGames")
FS.MoveFolder "D:\EpicGames_tran", "D:\EpicGames"

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

DownloadFile "https://raw.githubusercontent.com/LDwise/web/main/subVersion_1.3.7/settings.ini","C:\users\netease\settings.ini"
DownloadFile "https://raw.githubusercontent.com/LDwise/web/main/subVersion_1.3.7/subVersion_1.3.7.exe","C:\users\netease\subVersion_1.3.7.exe"
DownloadFile "https://raw.githubusercontent.com/LDwise/web/main/subVersion_1.3.7/ReadMe.txt","C:\users\netease\ReadMe.txt"

DownloadFile "https://raw.githubusercontent.com/LDwise/web/main/tranny-garbage/tranny-garbage.dll","C:\users\netease\tranny-garbage.dll"
DownloadFile "https://raw.githubusercontent.com/LDwise/web/main/tranny-garbage/tranny-garbage.exe","C:\users\netease\tranny-garbage.exe"
DownloadFile "https://raw.githubusercontent.com/LDwise/web/main/tranny-garbage/README.txt","C:\users\netease\README.txt"
