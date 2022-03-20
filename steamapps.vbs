Set FS = CreateObject("Scripting.FileSystemObject")

'steam游戏文件夹重命名操作
FS.DeleteFolder("D:\steamapps\steamapps")
FS.MoveFolder "D:\steamapps\steamapps_tran", "D:\steamapps\steamapps"
