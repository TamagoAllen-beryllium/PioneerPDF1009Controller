#================================================================================================================================================IMPORTS
import tkinter, sqlite3, shutil, os
from tkinter import ttk, messagebox
from tkinter import *
from DBSearchFunct import *
from PostOpCode import *
from Remote import *

DiscId, DiscNo, TrackNo, AlbumId, DiscNum=list(''),list(''),list(''),list(''),list('')
#================================================================================================================================================MISC FUNCTIONS
def reset(): #Clears all variables used by track searches
    DiscId.clear(), DiscNo.clear(), TrackNo.clear(), AlbumId.clear(), DiscNum.clear()
    
def gentrackcodes(DiscNu): #Uses PostOpCode.py to convert retrieved IDs to disc and track numbers
    Tracks=GenAlbumNumbers(DiscId, DiscNo, AlbumId)
    DiscNu=DiscNu.extend(Tracks.ANo)

def IRConversion(): #Uses PostOpCode.py to convert retrieved IDs to useable IR codes and attempts to transmit them (Fails if theres no IR LED as part of the PC)
    IR=ConvertToIR(TrackNo,DiscNum)

def ShuffleTracks(): #Uses PostOpCode.py to shuffle tracks
    global TrackNo, DiscNum
    Shuffle=ConvertToShuffled(TrackNo, DiscNum)
    TrackNo=list(Shuffle.TrackNo)
    DiscNum=list(Shuffle.DiscNo)

def Truncate(): #Uses PostOpCode.py to truncate track lists to contain no more than 36 tracks as the CD carousel can only handle data for 36 tracks at a time
    global TrackNo, DiscNum
    Round=TruncateTracks(TrackNo, DiscNum)

def snipnship(): #Complete PostOp Script
    gentrackcodes(DiscNum)
    print("List: ", TrackNo,"\n",DiscNum)
    if (shufflevar.get() == 1):
        ShuffleTracks()
        print("Shuffled: ", TrackNo,"\n",DiscNum)
    Truncate()
    print("Truncated: ", TrackNo,"\n",DiscNum)
    IRConversion()
    print("Final String Marking End Of Broadcast: ", TrackNo,"\n",DiscNum)

def selectItem(tree): #Function that allows the clicked on track to be determined by the program
    def ReplaceText(Box,Value):
        Box.delete(0,END), Box.insert(0,values[int(Value)])# Deletes Current Entry And Inserts New One
    global UID
    try:
        curItem = tree.focus()
        details = tree.item(curItem)
        UID = details.get("values")[0] # Grab record Number
        curItem = tree.focus() # Grab record values
        values = tree.item(curItem, 'values')
        BoxVals=(PkIDEntry,NameEntry,NoEntry,FkIDEntry,GenreEntry,YearEntry) # Force clears entry boxes
        for i in BoxVals:
            i.delete(0,END)
        ReplaceText(PkIDEntry,0), ReplaceText(NameEntry,1)   # Outpus to entry boxes
        if ActiveTree != treeArtist:
            ReplaceText(NoEntry,2)
            if ActiveTree == treeTrack:
                ReplaceText(FkIDEntry,3)
                global TID, AID, TNM
                TNM = details.get("values")[1]
                TID = details.get("values")[2]
                AID = details.get("values")[3]
            else:
                ReplaceText(GenreEntry,3), ReplaceText(YearEntry,4), ReplaceText(FkIDEntry,5)
    except:
        UID = "-1"
   
class getTracks:
    def __init__(self, AlbumSearchedColumn, DiscIds, DiscNos, TrackNos, AlbumIds):
        if UID != "-1":
            Album=Search("AlbumID","Album", AlbumSearchedColumn, str(UID))
            DiscIds=DiscIds.extend(list((Album.PkID).split()))
            DiscNos=DiscNos.extend(list((Album.TrkNo).split()))

            Track=TrackSearch("TrackID","Track", "Fk_Album_Id", Album.PkID)
            TrackNos=TrackNos.extend(list((Track.TrkNo).split()))
            AlbumIds=AlbumIds.extend(list((Track.AlbId).split()))
        
            snipnship() #Class that templates track retrieval from Album Or Artist Names

    
def getTrack(DiscIds, DiscNos, TrackNos, AlbumIds): 
    
    Track=Search("TrackID","Track", "Pk_Track_Id", str(int(UID)))
    TrackNos=TrackNos.extend(list((Track.TrkNo).split()))
    AlbumIds=AlbumIds.extend(list((Track.AlbId).split()))
    
    Album=Search("AlbumID","Album", "Pk_Album_Id", str(Track.AlbId))
    DiscIds=DiscIds.extend(list((Album.PkID).split()))
    DiscNos=DiscNos.extend(list((Album.TrkNo).split()))

    snipnship()

def sort_treeview(tv, col, reverse): #sorts contents of treeview
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    try:  # in case the value is numeric
        l.sort(reverse=reverse, key=lambda tup: float(tup[0]))
    except ValueError:  # it was string and is handled as such
        l.sort(reverse=reverse)
    for index, (val, k) in enumerate(l): # rearrange items in treeview to new sorted positions
        tv.move(k, '', index)
    tv.heading(col, command=lambda: sort_treeview(tv, col, not reverse))  # reverse sort next time
    
def connect(): #connects to sqlite DB (CD Database)
    conn = sqlite3.connect("CDLibrary.db")
    cur = conn.cursor()
    conn.close()

#================================================================================================================================================BACKUP FUNCTIONS

class TableOutput:
    def __init__(self, TableName, TreeName):
        conn = sqlite3.connect("CDLibrary.db")
        cur = conn.cursor()
        TableAndRowName = ("SELECT * FROM "+TableName)
        cur.execute(TableAndRowName)
        rows = cur.fetchall()
        File = open("Backups/"+TableName+"s.txt", "w")
        
        if str(TableName) == "Artist":
            File.write("+===+"+"="*50+"+\n|No.|Artist Name"+" "*39+"|\n+===+"+"="*50+"+\n")
            for row in rows:
                File.write("|"+str(row[0])+(" "*(3-int(len(str(row[0]))))+"|"+str(row[1][:50])+(" "*(50-int(len(str(row[1]))))+"|\n")))   # Write inside file
            File.write("+===+"+"="*50+"+\n")
            
        if str(TableName) == "Album":
            File.write("+===+"+"="*50+"+====+"+"="*30+"+\n|No.|Album Name"+" "*40+"|Year|Genre"+" "*25+"|\n+===+"+"="*50+"+====+"+"="*30+"+\n")
            for row in rows:
                File.write("|"+str(row[2])+(" "*(3-int(len(str(row[2]))))+"|"+str(row[1][:50])+(" "*(50-int(len(str(row[1]))))+"|"+str(row[4])+(" "*(4-int(len(str(row[4]))))+"|"+str(row[3][:30])+(" "*(30-int(len(str(row[3]))))+"|\n")))) )  # Write inside file
            File.write("+===+"+"="*50+"+====+"+"="*30+"+\n")
            
        if str(TableName) == "Track":
            File.write("+=======+"+"="*50+"+=======+\n|Dsc No.|Track Name"+" "*40+"|Trk No.|\n+=======+"+"="*50+"+=======+\n")
            for row in rows:
                File.write("|"+str(row[3])+(" "*(7-int(len(str(row[3]))))+"|"+str(row[1][:50])+(" "*(50-int(len(str(row[1]))))+"|"+str(row[2])+(" "*(7-int(len(str(row[2]))))+"|\n"))))   # Write inside file
            File.write("+=======+"+"="*50+"+=======+\n")
            
        conn.close(), File.close()

#================================================================================================================================================MENU SWITCHING FUNCTIONS

def TreeNameTempStore(TreeName):
    global ActiveTree
    ActiveTree=TreeName #saves the current tree to a variable for ease of access
    
class View:
    def __init__(self, WidgetName):
        if WidgetName == Header:
            WidgetName.grid(column=0, row=0, sticky="sewn")
        WidgetName.grid(padx=10, pady=10, sticky="sewn")

class HideFrameContents:
    def __init__(self, FrameName):
        for Widget in FrameName.winfo_children():
            Widget.grid_forget()

class Hide:
    def __init__(self, WidgetName):
            WidgetName.grid_forget()
            
#================================================================================================================================================MENU BUTTON FUNCTIONS
def StaffBrowser(): #Checks Access Level and if Its High Enough It Hides & Shows Things Accordingly
    View(Header), HideFrameContents(Body), HideFrameContents(Editor), View(Editor), View(DBViewer), View(EntryBox), View(DBEditor), TableButtonsConfig(), ViewTable("Artist", treeArtist), treeArtist.tkraise(), ArtistPlay.tkraise(), TreeNameTempStore(treeArtist), ColumnHeadings(treeArtist, (all), ArtistColumns)

def PLBrowser(): #Checks Access Level and if Its High Enough It Hides & Shows Things Accordingly
    View(Header), HideFrameContents(Body), HideFrameContents(Editor), View(Editor), View(DBViewer), View(PLEditor), Hide(ArtistButton), Hide(AlbumButton), Hide(TrackButton), Hide(ArtistPlay), Hide(AlbumPlay), Hide(TrackPlay), ViewTable("Track", treeTrack), treeTrack.tkraise(), TrackPlay.tkraise(), TreeNameTempStore(treeTrack),  ColumnHeadings(treeTrack, (all), TrackColumns)

def BackUpsMenu(): #Checks Access Level and if Its High Enough It Hides & Shows Things Accordingly
    View(Header), HideFrameContents(Body), View(Backups)

#================================================================================================================================================GUI
root = Tk()
root.title("J.E.N.I.")
root.resizable(False, False)

Header = Frame(root)
Header.grid(column=0, row=0, sticky="nesw", padx=20)

Body = Frame(root)
Body.grid(column=0, row=1, sticky="nesw", padx=20)

Menu = Frame(Body)

Editor=Frame(Body)

Backups=Frame(Body)

for widget in Body.winfo_children():
  widget.grid_configure(column=0, row=1, sticky="nesw", padx=20)

DBViewer = LabelFrame(Editor, text="Database")
DBViewer.grid(column=0, row=0, sticky="nesw", padx=20)

PLEditor = LabelFrame(Editor, text="Playlist Menu")
PLEditor.grid(column=0, row=1, sticky="nesw", padx=20)

EntryBox = LabelFrame(Editor, text="Record")
EntryBox.grid(column=0, row=1, sticky="nesw", padx=20)

DBEditor = LabelFrame(Editor, text="Commands")
DBEditor.grid(column=0, row=2, sticky="nesw", padx=20)

shufflevar = IntVar()

#================================================================================================================================================ENTRY BOX FUNCTIONS
def clear_entries():
    EntryBoxes=(PkIDEntry,NameEntry,NoEntry,GenreEntry,YearEntry,FkIDEntry)
    for Widget in EntryBoxes:
            Widget.delete(0, END) # Clear entry boxes

class UpdateRecord: # Update record
    def __init__(self, Act):
        global Error
        curItem = ActiveTree.focus() # Update record
        ActiveTree.item(curItem, text="", values=(PkIDEntry.get(), NameEntry.get(), NoEntry.get(), GenreEntry.get(), YearEntry.get(), FkIDEntry.get())) # Update the database
        conn = sqlite3.connect('CDLibrary.db') # Create a cursor instance
        cur = conn.cursor()
        x = ActiveTree.selection()
        Error="0"
        if Act == 'delete': # delete function
            for record in x:
                details = ActiveTree.item(record)
                if ActiveTree == treeArtist:
                    cur.execute("""DELETE FROM Artist WHERE Pk_Artist_Id ="""+str(details.get("values")[0]))
                if ActiveTree == treeAlbum:
                    cur.execute("""DELETE FROM Album WHERE Pk_Album_Id ="""+str(details.get("values")[0]))
                if ActiveTree == treeTrack:
                    cur.execute("""DELETE FROM Track WHERE Pk_Track_Id ="""+str(details.get("values")[0]))
                ActiveTree.delete(record)
        if Act == 'addit': #add/ update function
            if ActiveTree == treeArtist:
                Validate("primary", PkIDEntry.get(), "Primary Key"), Validate("present", NameEntry.get(), "Artist Name")
                if Error == "0":
                    if PkIDEntry.get() != "":
                        cur.execute(("""INSERT or REPLACE INTO Artist (Pk_Artist_Id, Artist_Name)VALUES(?,?)"""), (PkIDEntry.get(), NameEntry.get()))
                    else:
                        print(NameEntry.get())
                        cur.execute(("INSERT INTO Artist(Pk_Artist_Id, Artist_Name) VALUES(null, ?)"), (NameEntry.get(),))
            if ActiveTree == treeAlbum:
                Validate("primary", PkIDEntry.get(), "Primary Key"), Validate("present", NameEntry.get(), "Album Name"), Validate("int", NoEntry.get(), "Album Number"), Validate("year", YearEntry.get(), "Release Year"), Validate("foreign", FkIDEntry.get(), "Artist Foreign Key")
                if Error == "0":
                    if PkIDEntry.get() != "":
                        cur.execute("""INSERT or REPLACE INTO Album (Pk_Album_Id, Album_Name, Album_Number, Album_Genre, Album_Release_Year, Fk_Artist_Id) VALUES(?,?,?,?,?,?)""", (PkIDEntry.get(), NameEntry.get(), NoEntry.get(), GenreEntry.get(), YearEntry.get(), FkIDEntry.get()))
                    else:
                        cur.execute("""INSERT INTO Album (Pk_Album_Id, Album_Name, Album_Number, Album_Genre, Album_Release_Year, Fk_Artist_Id) VALUES(null,?,?,?,?,?)""", (NameEntry.get(), NoEntry.get(), GenreEntry.get(), YearEntry.get(), FkIDEntry.get()))
            if ActiveTree == treeTrack:
                Validate("primary", PkIDEntry.get(), "Primary Key"), Validate("present", NameEntry.get(), "Track Name"), Validate("int", NoEntry.get(), "Track Number"), Validate("foreign", FkIDEntry.get(), "Album Foreign Key")
                if Error == "0":
                    if PkIDEntry.get() != "":
                        cur.execute("""INSERT or REPLACE INTO Track (Pk_Track_Id, Track_Name, Track_Number, Fk_Album_Id) VALUES(?,?,?,?)""", (PkIDEntry.get(), NameEntry.get(), NoEntry.get(), FkIDEntry.get()))
                    else:
                        cur.execute("""INSERT INTO Track (Pk_Track_Id, Track_Name, Track_Number, Fk_Album_Id) VALUES(null,?,?,?)""", (NameEntry.get(), NoEntry.get(), FkIDEntry.get()))
        conn.commit()
        if ActiveTree == treeArtist: #update trees
            ViewTable("Artist", treeArtist)
        if ActiveTree == treeAlbum:
            ViewTable("Album", treeAlbum)
        if ActiveTree == treeTrack:
            ViewTable("Track", treeTrack)
        conn.close()
    
#================================================================================================================================================VALIDATION FUNCTIONS

def Validate(Type, CheckVal, ValName): #validation function
    global Error
    
    if Type == "int": #integer check
        try:
            CheckVal = int(CheckVal)
        except:
            tkinter.messagebox.showerror(title="DataType Invalid",message=ValName + ' Must Be An Integer')
            Error=Error+"1"

    if Type == "present": # presence check
        if str(CheckVal) == "":
            tkinter.messagebox.showerror(title="Required Info Absence",message=ValName + ' Must Be Entered')
            Error=Error+"1"

    if Type == "year": #checks presence, then integer then that its a valid year
        try:
            CheckVal = int(CheckVal)
            if str(CheckVal) == "":
                tkinter.messagebox.showerror(title="Required Info Absence",message=ValName + ' Must Be Entered')
                Error=Error+"1"
            elif int(CheckVal) < 1850 or int(CheckVal) > 2050:
                tkinter.messagebox.showerror(title="Invalid Year",message=ValName + ' Must Be A Year In YYYY Format')
                Error=Error+"1"
        except:
            tkinter.messagebox.showerror(title="DataType Invalid",message=ValName + ' Must Be An Integer')
            Error=Error+"1"

    if Type == "foreign": #checks that a valid primary key is being referenced
        try:
            CheckVal = int(CheckVal)
            if ValName == "Artist Foreign Key":
                FkCheck=("""SELECT Pk_Artist_Id FROM Artist WHERE Pk_Artist_Id = ? """)
            if ValName == "Album Foreign Key":
                FkCheck=("""SELECT Pk_Album_Id FROM Album WHERE Pk_Album_Id = ? """)
            conn = sqlite3.connect('CDLibrary.db')
            cursor = conn.cursor()
            Fk=int(CheckVal)
            cursor.execute(FkCheck, (Fk,))
            record=(cursor.fetchone())
            if str(record)=="None":
                tkinter.messagebox.showerror(title="Foreign Key Invalid",message='The' + ValName + " Could Not Be Found")
                Error=Error+"1"
        except:
            tkinter.messagebox.showerror(title="DataType Invalid",message=ValName + ' Must Be An Integer')
            Error=Error+"1"
            
    if Type == "primary":  #checks if the primary key is either valid or empty(for autofill)
        if CheckVal != "":
            try:
                CheckVal = int(CheckVal)
            except:
                tkinter.messagebox.showerror(title="DataType Invalid",message=ValName + ' Must Be An Integer,\nOr Left Blank')
                Error=Error+"1"

#================================================================================================================================================PLAYLIST EDITOR FUNCTIONS
def updateNum(event): #update the track number display
    File = open("Playlists/"+PLList.get(), "r")
    TracksInPLLabel.config(text="Tracks In Playlist: " + str(len(File.readlines()))), File.close()
    
def RefreshList(): #refresh playlist list
    PLList.config(values=os.listdir("Playlists"))
    
def CreatePL(): #create new playlist file
    PLName = PLEntry.get()
    File = open("Playlists/"+PLName+".txt", "w")
    File.close()
    
def AddTrkToPL(): #adds new track to playlist file
    try:
        File = open("Playlists/"+PLList.get(), "a")
        File.write(str(AID)+" "+str(TID)+" | "+str(TNM)+"\n")
        File = open("Playlists/"+PLList.get(), "r")
        TracksInPLLabel.config(text="Tracks In Playlist: " + str(len(File.readlines()))), File.close()
    except:
        tkinter.messagebox.showerror(title="Nothing To Add",message="You Must Select A Track To Add Within This Menu Or The Database ")   

def PLPlay(): #grabs and plays tracks from playlist file
    global DiscNum, TrackNo
    DiscNum=""
    TrackNo=""
    i = 0
    print(PLList.get())
    File = open("Playlists/"+PLList.get(), "r")
    Playlist = File.readlines()
    while i < len(Playlist):
            Track=(Playlist[i]).split()
            DiscNum=str(DiscNum)+(Track[0])+' '
            TrackNo=str(TrackNo)+(Track[1])+' '
            i = i+1
    DiscNum=DiscNum.split()
    TrackNo=TrackNo.split()
    File.close(), snipnship()
    
#================================================================================================================================================HEADER
BackButton=Button(Header, text='Back', command=lambda:[HideFrameContents(Body), View(Menu), Hide(Header)])
BackButton.pack(side="left", padx=40, expand=True, anchor=W)
img=PhotoImage(file='GoodVibrationsLogo.gif')
Logo = Label(Header, image=(img))
Logo.pack(side="right", padx=40, expand=True, anchor=E)

#================================================================================================================================================MENU BUTTONS
StaffBrowserButton=Button(Menu, text='Database', command=StaffBrowser)
StaffBrowserButton.grid(column=0, row=0, sticky="w", padx=10, pady=10)

PLEditorButton=Button(Menu, text='Playlists', command=PLBrowser)
PLEditorButton.grid(column=0, row=1, sticky="w", padx=10, pady=10)

BackUpButton=Button(Menu, text='Prints', command=lambda:[BackUpsMenu()])
BackUpButton.grid(column=0, row=2, sticky="w", padx=10, pady=10)

RemoteButton=Button(Menu, text='Remote', command=lambda:[RemoteWindow()])
RemoteButton.grid(column=0, row=3, sticky="w", padx=10, pady=10)
#================================================================================================================================================BROWSER

ArtistButton=Button(DBViewer, text='Artist', command=lambda:[ViewTable("Artist", treeArtist), treeArtist.tkraise(), ArtistPlay.tkraise(), DBViewer.tkraise(), TreeNameTempStore(treeArtist), ColumnHeadings(treeArtist, (all), ArtistColumns)])
AlbumButton=Button(DBViewer, text='Album', command=lambda:[ViewTable("Album", treeAlbum), treeAlbum.tkraise(), AlbumPlay.tkraise(), TreeNameTempStore(treeAlbum),  ColumnHeadings(treeAlbum, (0,1,3,4), AlbumColumns)])
TrackButton=Button(DBViewer, text='Track', command=lambda:[ViewTable("Track", treeTrack), treeTrack.tkraise(), TrackPlay.tkraise(), TreeNameTempStore(treeTrack),  ColumnHeadings(treeTrack, (all), TrackColumns)])
#Buttons to change tables

#================================================================================================================================================DBVIEWER
class ViewTable: #Class to populate treeview
    def __init__(self, TableName, TreeName):
        TreeName.delete(*TreeName.get_children()) #Purges All Treeview Data Before Each Viewing,
                                                  #[Fixes An Issue With The Tab Sorting Where The Fields Are Generated A Second Time Upon Sorting Creating Duplicates]
        conn = sqlite3.connect("CDLibrary.db")
        cur = conn.cursor()
        TableAndRowName = ("SELECT * FROM "+TableName)
        cur.execute(TableAndRowName)
        rows = cur.fetchall()
        for row in rows:
            #print(row) # it print all records in the database
            TreeName.insert("", END, values=row)
        conn.close()
        
class ColumnHeadings:
    def __init__(self, TreeName, ColumnsShown, ColumnVar):
        TreeName.grid(column=2, row=0, rowspan=4, columnspan=4, sticky='sewn')
        for i in ColumnVar:
            TreeName.heading(i, text=i, command=lambda c=i: sort_treeview(TreeName, c, False))
            TreeName.column(i, width=100)
        # Create a Treeview Scrollbar v
        TreeScroll = Scrollbar((DBViewer), orient="vertical", command=TreeName.yview)
        TreeScroll.grid(column=5, row=0, rowspan=4, sticky='nse')
        TreeName.config(yscrollcommand=TreeScroll.set)

ArtistColumns=("ID","Artist Name")
treeArtist= ttk.Treeview(DBViewer, column=(ArtistColumns), show='headings')
ColumnHeadings(treeArtist, (all), ArtistColumns)

AlbumColumns=("ID","Album Name", "AlbumNo", "Genre", "Release Year")
treeAlbum= ttk.Treeview(DBViewer, column=(AlbumColumns), show='headings', displaycolumns=(0,1,3,4))
ColumnHeadings(treeAlbum, (0,1,3,4), AlbumColumns)

TrackColumns=("ID","Track Name", "Track No. On Disc")
treeTrack= ttk.Treeview(DBViewer, column=(TrackColumns), show='headings')
ColumnHeadings(treeTrack, (all), TrackColumns)
#Structure for defining treeview table headings and structures (Needed to allow table sorting)

treeTrack.bind('<ButtonRelease-1>', lambda eff: [selectItem(treeTrack), reset()])
treeAlbum.bind('<ButtonRelease-1>', lambda eff: [selectItem(treeAlbum), reset()])
treeArtist.bind('<ButtonRelease-1>', lambda eff: [selectItem(treeArtist), reset()])
#Binds the changing of the selected item and reseting of search parameters to mouse clicks on a per treeview basis

ArtistPlay=Button(DBViewer, text='Play', command=lambda:[reset(), getTracks("Fk_Artist_Id", DiscId, DiscNo, TrackNo, AlbumId)])

AlbumPlay=Button(DBViewer, text='Play', command=lambda:[reset(), getTracks("Pk_Album_Id", DiscId, DiscNo, TrackNo, AlbumId)])

TrackPlay=Button(DBViewer, text='Play', command=lambda:[reset(), getTrack(DiscId, DiscNo, TrackNo, AlbumId)])

def TableButtonsConfig():
    ArtistButton.grid(column=1, row=1, sticky="w", padx=10, pady=10)
    ArtistPlay.grid(column=6, row=2, sticky='sewn')
    AlbumButton.grid(column=1, row=2, sticky="w", padx=10, pady=10)
    AlbumPlay.grid(column=6, row=2, sticky='sewn')
    TrackButton.grid(column=1, row=3, sticky="w", padx=10, pady=10)
    TrackPlay.grid(column=6, row=2, sticky='sewn')

TableButtonsConfig()
    
ShuffleButton=Checkbutton(DBViewer, text='Shuffle', variable=shufflevar, onvalue=1, offvalue=0)
ShuffleButton.grid(column=6, row=1, sticky='sewn')
#Creates the 3 tab buttons and shuffle buttons

#================================================================================================================================================ENTRY BOXES

PkIDLabel = Label(EntryBox, text="ID")
PkIDLabel.grid(row=0, column=0)
PkIDEntry = Entry(EntryBox)
PkIDEntry.grid(row=0, column=1)

NameLabel = Label(EntryBox, text="Name")
NameLabel.grid(row=0, column=2)
NameEntry = Entry(EntryBox)
NameEntry.grid(row=0, column=3)

NoLabel = Label(EntryBox, text="Number")
NoLabel.grid(row=0, column=4)
NoEntry = Entry(EntryBox)
NoEntry.grid(row=0, column=5)

GenreLabel = Label(EntryBox, text="Genre")
GenreLabel.grid(row=1, column=0)
GenreEntry = Entry(EntryBox)
GenreEntry.grid(row=1, column=1)

YearLabel = Label(EntryBox, text="Year")
YearLabel.grid(row=1, column=2)
YearEntry = Entry(EntryBox)
YearEntry.grid(row=1, column=3)

FkIDLabel = Label(EntryBox, text="FkID")
FkIDLabel.grid(row=1, column=4)
FkIDEntry = Entry(EntryBox)
FkIDEntry.grid(row=1, column=5)

for Widget in EntryBox.winfo_children():
            Widget.grid(padx=10, pady=10)

#================================================================================================================================================DBEDITOR

# Add Buttons
update_button = Button(DBEditor, text="Update/ Add Record", command=lambda:UpdateRecord('addit'))
update_button.grid(row=0, column=0, padx=10, pady=10)

Deletebutton = Button(DBEditor, text="Delete Record(s)", command=lambda:UpdateRecord('delete'))
Deletebutton.grid(row=0, column=3, padx=10, pady=10)

select_record_button = Button(DBEditor, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

#Binding The Delete, Edit And Add Functions To Keyboard Presses In Their Specific Menus For Convenience
PkIDEntry.bind('<Return>', lambda event: UpdateRecord('addit'))
NameEntry.bind('<Return>', lambda event: UpdateRecord('addit'))
NoEntry.bind('<Return>', lambda event: UpdateRecord('addit'))
GenreEntry.bind('<Return>', lambda event: UpdateRecord('addit'))
YearEntry.bind('<Return>', lambda event: UpdateRecord('addit'))
FkIDEntry.bind('<Return>', lambda event: UpdateRecord('addit'))
treeArtist.bind('<Delete>', lambda event: UpdateRecord('delete'))
treeAlbum.bind('<Delete>', lambda event: UpdateRecord('delete'))
#Silly code to let the logo feel sad
Logo.bind('<Button-1>', lambda event: tkinter.messagebox.showerror(title="OW",message="Watch Out That Hurts ):"))


#================================================================================================================================================PLAYLIST MAKER/PLAYER BUTTONS
TracksInPLLabel = Label(PLEditor)
TracksInPLLabel.grid(row=0, column=2)

AddTrackButton = Button(PLEditor, text="Add Track To Playlist", command=lambda:[AddTrkToPL()])
AddTrackButton.grid(row=0, column=0)

PLList = ttk.Combobox(PLEditor, state="readonly", postcommand=RefreshList)
PLList['values']=os.listdir("Playlists")
PLList.current(0)
PLList.grid(row=0, column=1)
PLList.bind("<<ComboboxSelected>>", updateNum)

NewPLButton = Button(PLEditor, text="Create New/ Wipe Playlist", command=lambda:[CreatePL()])
NewPLButton.grid(row=1, column=0)

PLEntry = Entry(PLEditor)
PLEntry.grid(row=1, column=1)

PLPlayButton = Button(PLEditor, text="Play", command=lambda:[PLPlay()])
PLPlayButton.grid(row=2, column=2)

for widget in PLEditor.winfo_children():
  widget.grid_configure(padx=10, pady=10, sticky="SEWN")

#================================================================================================================================================BACKUPS
ArtistBackupButton = Button(Backups, text="Artist Txt", command=lambda:[TableOutput("Artist", treeArtist),tkinter.messagebox.showinfo(title="File Created Successfully",message="Artists.txt Successfully Generated Within Backups Folder!")])
ArtistBackupButton.grid(row=0, column=0)

AlbumBackupButton = Button(Backups, text="Album Txt", command=lambda:[TableOutput("Album", treeAlbum),tkinter.messagebox.showinfo(title="File Created Successfully",message="Albums.txt Successfully Generated Within Backups Folder!")])
AlbumBackupButton.grid(row=0, column=1)

TrackBackupButton = Button(Backups, text="Track Txt", command=lambda:[TableOutput("Track", treeTrack),tkinter.messagebox.showinfo(title="File Created Successfully",message="Tracks.txt Successfully Generated Within Backups Folder!")])
TrackBackupButton.grid(row=0, column=2)

for widget in Backups.winfo_children():
  widget.grid_configure(padx=10, pady=10, sticky='nesw')

#================================================================================================================================================INITIAL LOOP TO SHOW MENU
Hide(Header), HideFrameContents(Body), View(Menu)
root.mainloop()

