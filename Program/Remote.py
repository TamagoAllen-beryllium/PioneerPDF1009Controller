from tkinter import *
from tkinter import ttk
from JENIHex import *
import subprocess
import tkinter

def RemoteWindow():
                                                                               #CD Carousel Buttons

    remotewindow=tkinter.Tk()
    remotewindow.title("Remote")
    Pdf=tkinter.Label(remotewindow, text="Pioneer PD-F1009")
    Pdf.grid(row=0, column=4)

    Power=tkinter.Button(remotewindow, text="Power", command=cdpower)
    Power.grid(row=0, column=0)

    Hilite=tkinter.Button(remotewindow, text="Hi-lite", command=cdhilite)
    Hilite.grid(row=0, column=1)

    Prev=tkinter.Button(remotewindow, text="Previous", command=cdprev)
    Prev.grid(row=0, column=2)

    Best=tkinter.Button(remotewindow, text="Best", command=cdbest)
    Best.grid(row=0, column=3)

    Repeat=tkinter.Button(remotewindow, text="Repeat", command=cdrepeat)
    Repeat.grid(row=1, column=0)

    Mode=tkinter.Button(remotewindow, text="Mode", command=cdmode)
    Mode.grid(row=1, column=1)

    Program=tkinter.Button(remotewindow, text="Program", command=cdprogram)
    Program.grid(row=1, column=2)

    Clear=tkinter.Button(remotewindow, text="Clear", command=cdclear)
    Clear.grid(row=1, column=3)

    One=tkinter.Button(remotewindow, text="1", command=cdKEY1)
    One.grid(row=2, column=0)

    Two=tkinter.Button(remotewindow, text="2", command=cdKEY2)
    Two.grid(row=2, column=1)

    Three=tkinter.Button(remotewindow, text="3", command=cdKEY3)
    Three.grid(row=2, column=2)

    Display=tkinter.Button(remotewindow, text="Display", command=cddisplay)
    Display.grid(row=2, column=3)

    Four=tkinter.Button(remotewindow, text="4", command=cdKEY4)
    Four.grid(row=3, column=0)

    Five=tkinter.Button(remotewindow, text="5", command=cdKEY5)
    Five.grid(row=3, column=1)

    Six=tkinter.Button(remotewindow, text="6", command=cdKEY6)
    Six.grid(row=3, column=2)

    Seven=tkinter.Button(remotewindow, text="7", command=cdKEY7)
    Seven.grid(row=4, column=0)

    Eight=tkinter.Button(remotewindow, text="8", command=cdKEY8)
    Eight.grid(row=4, column=1)

    Nine=tkinter.Button(remotewindow, text="9", command=cdKEY9)
    Nine.grid(row=4, column=2)

    Disc=tkinter.Button(remotewindow, text="Disc", command=cddisc)
    Disc.grid(row=5, column=0)

    Zero=tkinter.Button(remotewindow, text="0", command=cdKEY0)
    Zero.grid(row=5, column=1)

    Track=tkinter.Button(remotewindow, text="Track", command=cdtrack)
    Track.grid(row=5, column=2)

    PrevDisc=tkinter.Button(remotewindow, text="- Disc", command=cdprevdisc)
    PrevDisc.grid(row=6, column=2)

    NextDisc=tkinter.Button(remotewindow, text="+ Disc", command=cdnextdisc)
    NextDisc.grid(row=6, column=3)

    Rewind=tkinter.Button(remotewindow, text="<<", command=cdrewind)
    Rewind.grid(row=7, column=0)

    Fastforward=tkinter.Button(remotewindow, text=">>", command=cdfastforward)
    Fastforward.grid(row=7, column=1)

    SkipBack=tkinter.Button(remotewindow, text="│<<", command=cdskipback)
    SkipBack.grid(row=7, column=2)

    SkipForward=tkinter.Button(remotewindow, text=">>│", command=cdskipforward)
    SkipForward.grid(row=7, column=3)

    Stop=tkinter.Button(remotewindow, text="■", command=cdstop)
    Stop.grid(row=8, column=0)

    Pause=tkinter.Button(remotewindow, text="││", command=cdpause)
    Pause.grid(row=8, column=1)

    Play=tkinter.Button(remotewindow, text="▸", command=cdplay)
    Play.grid(row=8, column=2)

    Random=tkinter.Button(remotewindow, text="Random", command=cdrandom)
    Random.grid(row=8, column=3)

    div=ttk.Separator(remotewindow, orient='horizontal')
    div.grid(row=9, columnspan=5, sticky='ew')

                                                                                            #Cassette Player Buttons

    Cst=tkinter.Label(remotewindow, text="Pioneer CT-M6R")
    Cst.grid(row=10, column=4)

    CstEject=tkinter.Button(remotewindow, text="Open/Close", command=csteject)
    CstEject.grid(row=10, column=0)

    CstReturn=tkinter.Button(remotewindow, text="Return", command=cstreturn)
    CstReturn.grid(row=10, column=1)

    CstMode=tkinter.Button(remotewindow, text="Counter Mode", command=cstcountermode)
    CstMode.grid(row=10, column=2)

    CstReset=tkinter.Button(remotewindow, text="Counter Reset", command=cstcounterreset)
    CstReset.grid(row=10, column=3)

    CstAllRewind=tkinter.Button(remotewindow, text="All Rewind", command=cstrewindall)
    CstAllRewind.grid(row=11, column=0)

    CstRelay=tkinter.Button(remotewindow, text="Relay", command=cstrelay)
    CstRelay.grid(row=11, column=1)

    CstRewind=tkinter.Button(remotewindow, text="<<", command=cstrewind)
    CstRewind.grid(row=11, column=2)

    CstFastforward=tkinter.Button(remotewindow, text=">>", command=cstfastforward)
    CstFastforward.grid(row=11, column=3)

    CstPlayBack=tkinter.Button(remotewindow, text="<", command=cstplayback)
    CstPlayBack.grid(row=12, column=2)

    CstPlayForward=tkinter.Button(remotewindow, text=">", command=cstplayforward)
    CstPlayForward.grid(row=12, column=3)

    CstRecord=tkinter.Button(remotewindow, text="o", command=cstrecord)
    CstRecord.grid(row=13, column=0, columnspan=2, sticky='ew')

    CstPause=tkinter.Button(remotewindow, text="││", command=cstpause)
    CstPause.grid(row=13, column=2)

    CstStop=tkinter.Button(remotewindow, text="■", command=cststop)
    CstStop.grid(row=13, column=3)

    CstKEY1=tkinter.Button(remotewindow, text="1", command=cstKEY1)
    CstKEY1.grid(row=14, column=0)

    CstKEY2=tkinter.Button(remotewindow, text="2", command=cstKEY2)
    CstKEY2.grid(row=14, column=1)

    CstKEY3=tkinter.Button(remotewindow, text="3", command=cstKEY3)
    CstKEY3.grid(row=14, column=2)

    CstScan=tkinter.Button(remotewindow, text="Scan", command=cstscan)
    CstScan.grid(row=14, column=3)

    CstKEY4=tkinter.Button(remotewindow, text="4", command=cstKEY4)
    CstKEY4.grid(row=15, column=0)

    CstKEY5=tkinter.Button(remotewindow, text="5", command=cstKEY5)
    CstKEY5.grid(row=15, column=1)

    CstKEY6=tkinter.Button(remotewindow, text="6", command=cstKEY6)
    CstKEY6.grid(row=15, column=2)

    CstRandom=tkinter.Button(remotewindow, text="Random", command=cstrandom)
    CstRandom.grid(row=15, column=3)

    div2=ttk.Separator(remotewindow, orient='horizontal')
    div2.grid(row=16, columnspan=5, sticky='ew')

                                                                                    #Amp Buttons
        
    Amp=tkinter.Label(remotewindow, text="Kenwood A-71")
    Amp.grid(row=17, column=4)

    AmpTuner=tkinter.Button(remotewindow, text="Tuner", command=amptuner)
    AmpTuner.grid(row=17, column=0)

    AmpPhono=tkinter.Button(remotewindow, text="Phono", command=ampphono)
    AmpPhono.grid(row=17, column=1)

    AmpCD=tkinter.Button(remotewindow, text="CD", command=ampcd)
    AmpCD.grid(row=17, column=2)

    AmpMute=tkinter.Button(remotewindow, text="Mute", command=ampmute)
    AmpMute.grid(row=17, column=3)

    AmpVTR=tkinter.Button(remotewindow, text="VTR", command=ampvtr)
    AmpVTR.grid(row=18, column=0)

    AmpAVAUX=tkinter.Button(remotewindow, text="AV AUX", command=ampavaux)
    AmpAVAUX.grid(row=18, column=1)

    AmpDAT=tkinter.Button(remotewindow, text="DAT", command=ampdat)
    AmpDAT.grid(row=18, column=2)

    AmpVolUp=tkinter.Button(remotewindow, text="Vol +", command=ampvolup)
    AmpVolUp.grid(row=18, column=3)

    AmpTapeA=tkinter.Button(remotewindow, text="Tape A", command=amptapea)
    AmpTapeA.grid(row=19, column=0)

    AmpTapeB=tkinter.Button(remotewindow, text="Tape B", command=amptapeb)
    AmpTapeB.grid(row=19, column=1)

    AmpPower=tkinter.Button(remotewindow, text="Power", command=amppower)
    AmpPower.grid(row=19, column=2)

    AmpVolDown=tkinter.Button(remotewindow, text="Vol -", command=ampvoldown)
    AmpVolDown.grid(row=19, column=3)

                                                                                    #MD Player Buttons

    div2=ttk.Separator(remotewindow, orient='horizontal')
    div2.grid(row=20, columnspan=5, sticky='ew')
        
    MDPlayer=tkinter.Label(remotewindow, text="MDX-C6500R")
    MDPlayer.grid(row=21, column=4)

    MDPower=tkinter.Button(remotewindow, text="Power", command=mdpower)
    MDPower.grid(row=21, column=0)

    MDBass=tkinter.Button(remotewindow, text="D-Bass", command=mdDbass)
    MDBass.grid(row=21, column=1)

    MDVolUp=tkinter.Button(remotewindow, text="Vol +", command=mdvolumeup)
    MDVolUp.grid(row=21, column=3)

    MDDSCUP=tkinter.Button(remotewindow, text="DISC +", command=mdDISCUP)
    MDDSCUP.grid(row=21, column=2)

    MDList=tkinter.Button(remotewindow, text="List", command=mdlist)
    MDList.grid(row=22, column=0)

    MDBack=tkinter.Button(remotewindow, text="<<", command=mdback)
    MDBack.grid(row=22, column=1)

    MDFwd=tkinter.Button(remotewindow, text=">>", command=mdfwd)
    MDFwd.grid(row=22, column=3)

    MDDSCDOWN=tkinter.Button(remotewindow, text="DISC -", command=mdDISCDOWN)
    MDDSCDOWN.grid(row=23, column=2)

    MDSource=tkinter.Button(remotewindow, text="Source", command=mdsource)
    MDSource.grid(row=23, column=0)

    MDSound=tkinter.Button(remotewindow, text="Sound", command=mdsoundmenu)
    MDSound.grid(row=23, column=1)

    MDEnter=tkinter.Button(remotewindow, text="Enter", command=mdenter)
    MDEnter.grid(row=22, column=2)

    MDVolDown=tkinter.Button(remotewindow, text="Vol -", command=mdvolumedown)
    MDVolDown.grid(row=23, column=3)

    MDMenu=tkinter.Button(remotewindow, text="Menu", command=mdmenu)
    MDMenu.grid(row=24, column=0)

    MDdisplay=tkinter.Button(remotewindow, text="Display", command=mddisplay)
    MDdisplay.grid(row=24, column=1)

    MDAFTA=tkinter.Button(remotewindow, text="AF-TA", command=mdAFTA)
    MDAFTA.grid(row=24, column=2)

    MDmode=tkinter.Button(remotewindow, text="Mode", command=mdmode)
    MDmode.grid(row=24, column=3)

    MDATT=tkinter.Button(remotewindow, text="ATT", command=mdATT)
    MDATT.grid(row=25, column=0)
                                                                                    #End Loop Code


    for Widget in remotewindow.winfo_children():
                Widget.grid(padx=2, pady=2, sticky="sewn")

    remotewindow.mainloop()
