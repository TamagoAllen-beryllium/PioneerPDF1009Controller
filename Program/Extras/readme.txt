+=================================================================================================================+
|	 ________  _______   ________  ________  _____ ______   _______   _________   ___    ___ _________        |
|	|\   __  \|\  ___ \ |\   __  \|\   ___ \|\   _ \  _   \|\  ___ \ |\___   ___\|\  \  /  /|\___   ___\   	  |
|	\ \  \|\  \ \   __/|\ \  \|\  \ \  \_|\ \ \  \\\__\ \  \ \   __/|\|___ \  \_|\ \  \/  / ||___ \  \_|   	  |
|	 \ \   _  _\ \  \_|/_\ \   __  \ \  \ \\ \ \  \\|__| \  \ \  \_|/__   \ \  \  \ \    / /     \ \  \    	  |
|	  \ \  \\  \\ \  \_|\ \ \  \ \  \ \  \_\\ \ \  \    \ \  \ \  \_|\ \ __\ \  \  /     \/       \ \  \   	  |
|	   \ \__\\ _\\ \_______\ \__\ \__\ \_______\ \__\    \ \__\ \_______\\__\ \__\/  /\   \        \ \__\  	  |
|	    \|__|\|__|\|_______|\|__|\|__|\|_______|\|__|     \|__|\|_______\|__|\|__/__/ /\ __\        \|__|  	  |
|	                                                                             |__|/ \|__|               	  |
+=================================================================================================================+

Test Logins:

+===========+========+========+
|Access Lvl:|UserName|Password| 
+===========+========+========+  
|1          |Test1   |Password|   
|2          |Test2   |Password| 
+===========+========+========+                                                                                            
                                                                                                     
Folder Contents:

[01] - The Backups Folder 
	Stores All Files Created Within The Backups Menu

[02] - The Playlists Folder
	Stores All Playlist.txt Files Created Within The Playlists Menu

[03] - The CDLibrary Database File
	Stores All Data Related To Tracks Within The CD Carousel
	
[04] - The DBSearchFunct Python File
	Internal File Containing All Functions For Searching The CDLibrary File

[05] - GoodVibrations Logo Image
	Store Logo

[06] - JENIHex Python File
	Internal File Containing All Functions For Converting Plain Text To IR Instructions

[07] - JENIPrint Python File
	Internal File Containing All Functions For Converting Plain Text To Print Functions For Demo Purposes

[08] - Main Executeable File
	This File Launches The GUI Portion Of The Program

[09] - PostOpCode Python File
	Internal File Containing All Functions For Converting Fetched Data To IR Function Strings

[10] - Readme Text File     												 < You Are Here
	The Instructions File You Are Currently Reading

[11] - Remote Python File
	Executeable File Referenced By Application Which Launches A Digital Remote Window

[12] - StaffLogins Database File
	Stores All Data Related To Employee Logins

Operation:

If You Are Not Running A Raspberry Pi With An IR Module Swap The Names Of The JENIHex.py [06] & JENIPrint.py [07] Files 
To Allow The Programme To Print The Hex Code Values Of The IR Commands To The Terminal Instead Of Attempting To Access The Non-Existent IR Module

1) Open Main.py
2) Click Log In
3) Enter Login Credentials From Test Logins
4) Enjoy