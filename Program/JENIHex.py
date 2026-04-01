import subprocess

#------------------------------------------------------------------- PDF-1009 CD Carousel

def cdpower():
    subprocess.run(["ir-ctl", "-S", "nec:0xa21c"])
    
def cdhilite():
    subprocess.run(["ir-ctl", "-S", "nec:0xa25e"])
    
def cdprev():
    subprocess.run(["ir-ctl", "-S", "nec:0xa2c6"])
    subprocess.run(["ir-ctl", "-S", "nec:0xa293"])
    
def cdbest():
    subprocess.run(["ir-ctl", "-S", "nec:0xa2c2"])
    subprocess.run(["ir-ctl", "-S", "nec:0xa29b"])
    
def cdrepeat():
    subprocess.run(["ir-ctl", "-S", "nec:0xa20c"])
    
def cdmode():
    subprocess.run(["ir-ctl", "-S", "nec:0xa2c1"])
    subprocess.run(["ir-ctl", "-S", "nec:0xa29c"])

def cdall():
    subprocess.run(["ir-ctl", "-S", "nec:0xa216"])
    mode()

def cdsingle():
    subprocess.run(["ir-ctl", "-S", "nec:0xa216"])
    mode(), mode()

def cdcustom():
    subprocess.run(["ir-ctl", "-S", "nec:0xa216"])
    mode(), mode(), mode()
    
def cdprogram():
    subprocess.run(["ir-ctl", "-S", "nec:0xa20d"])
    
def cdclear():
    subprocess.run(["ir-ctl", "-S", "nec:0xa245"])
    
def cddisplay():
    subprocess.run(["ir-ctl", "-S", "nec:0xa243"])

def cdKEY1():
    subprocess.run(["ir-ctl", "-S", "nec:0xa201"])
    
def cdKEY2():
    subprocess.run(["ir-ctl", "-S", "nec:0xa202"])
    
def cdKEY3():
    subprocess.run(["ir-ctl", "-S", "nec:0xa203"])
    
def cdKEY4():
    subprocess.run(["ir-ctl", "-S", "nec:0xa204"])
    
def cdKEY5():
    subprocess.run(["ir-ctl", "-S", "nec:0xa205"])
    
def cdKEY6():
    subprocess.run(["ir-ctl", "-S", "nec:0xa206"])
    
def cdKEY7():
    subprocess.run(["ir-ctl", "-S", "nec:0xa207"])
    
def cdKEY8():
    subprocess.run(["ir-ctl", "-S", "nec:0xa208"])
    
def cdKEY9():
    subprocess.run(["ir-ctl", "-S", "nec:0xa209"])
    
def cdKEY0():
    subprocess.run(["ir-ctl", "-S", "nec:0xa200"])
    
def cddisc():
    subprocess.run(["ir-ctl", "-S", "nec:0xa241"])
    
def cdtrack():
    subprocess.run(["ir-ctl", "-S", "nec:0xa240"])
    
def cdprevdisc():
    subprocess.run(["ir-ctl", "-S", "nec:0xa2c1"])
    subprocess.run(["ir-ctl", "-S", "nec:0xa293"])
    
def cdnextdisc():
    subprocess.run(["ir-ctl", "-S", "nec:0xa21d"])
    
def cdrewind():
    subprocess.run(["ir-ctl", "-S", "nec:0xa20f"])
    
def cdfastforward():
    subprocess.run(["ir-ctl", "-S", "nec:0xa20e"])
    
def cdskipback():
    subprocess.run(["ir-ctl", "-S", "nec:0xa211"])
    
def cdskipforward():
    subprocess.run(["ir-ctl", "-S", "nec:0xa210"])
    
def cdstop():
    subprocess.run(["ir-ctl", "-S", "nec:0xa216"])
    
def cdpause():
    subprocess.run(["ir-ctl", "-S", "nec:0xa218"])
    
def cdplay():
    subprocess.run(["ir-ctl", "-S", "nec:0xa217"])
    
def cdrandom():
    subprocess.run(["ir-ctl", "-S", "nec:0xa24a"])

#------------------------------------------------------------------- CT-M6R Cassette Player

def cstKEY1():
    subprocess.run(["ir-ctl", "-S", "nec:0xa101"])

def cstKEY2():
    subprocess.run(["ir-ctl", "-S", "nec:0xa102"])

def cstKEY3():
    subprocess.run(["ir-ctl", "-S", "nec:0xa103"])
    
def cstKEY4():
    subprocess.run(["ir-ctl", "-S", "nec:0xa104"])
    
def cstKEY5():
    subprocess.run(["ir-ctl", "-S", "nec:0xa105"])
    
def cstKEY6():
    subprocess.run(["ir-ctl", "-S", "nec:0xa106"])
    
def cstfastforward():
    subprocess.run(["ir-ctl", "-S", "nec:0xa110"])
    
def cstrewind():
    subprocess.run(["ir-ctl", "-S", "nec:0xa111"])
    
def cstrecord():
    subprocess.run(["ir-ctl", "-S", "nec:0xa114"])
    
def cstplayback():
    subprocess.run(["ir-ctl", "-S", "nec:0xa115"])
    
def cststop():
    subprocess.run(["ir-ctl", "-S", "nec:0xa116"])
    
def cstplayforward():
    subprocess.run(["ir-ctl", "-S", "nec:0xa117"])
    
def cstpause():
    subprocess.run(["ir-ctl", "-S", "nec:0xa118"])
    
def cstrandom():
    subprocess.run(["ir-ctl", "-S", "nec:0xa122"])
    
def cstreturn():
    subprocess.run(["ir-ctl", "-S", "nec:0xa11e"])
    
def csteject():
    subprocess.run(["ir-ctl", "-S", "nec:0xa132"])
    
def cstnext():
    subprocess.run(["ir-ctl", "-S", "nec:0xa12c"])
    
def cstscan():
    subprocess.run(["ir-ctl", "-S", "nec:0xa124"])
    
def cstrelay():
    subprocess.run(["ir-ctl", "-S", "nec:0xa126"])
    
def cstcountermode():
    subprocess.run(["ir-ctl", "-S", "nec:0xa127"])
    
def cstcounterreset():
    subprocess.run(["ir-ctl", "-S", "nec:0xa128"])
    
def cstrewindall():
    subprocess.run(["ir-ctl", "-S", "nec:0xa11f"])

#------------------------------------------------------------------- A-71 Amp

def amptuner():
    subprocess.run(["ir-ctl", "-S", "nec:0xb891"])

def ampphono():
    subprocess.run(["ir-ctl", "-S", "nec:0xb890"])

def ampcd():
    subprocess.run(["ir-ctl", "-S", "nec:0xb892"])
    
def amptapea():
    subprocess.run(["ir-ctl", "-S", "nec:0xb894"])
    
def amptapeb():
    subprocess.run(["ir-ctl", "-S", "nec:0xb895"])
    
def ampvtr():
    subprocess.run(["ir-ctl", "-S", "nec:0xb896"])
    
def ampavaux():
    subprocess.run(["ir-ctl", "-S", "nec:0xb893"])
    
def ampdat():
    subprocess.run(["ir-ctl", "-S", "nec:0xb8a0"])
    
def ampmute():
    subprocess.run(["ir-ctl", "-S", "nec:0xb89c"])
    
def ampvolup():
    subprocess.run(["ir-ctl", "-S", "nec:0xb89b"])
    
def ampvoldown():
    subprocess.run(["ir-ctl", "-S", "nec:0xb89a"])
    
def amppower():
    subprocess.run(["ir-ctl", "-S", "nec:0xb89d"])

#------------------------------------------------------------------- MDX-C6500R Amp

def mdpower():
    subprocess.run(["ir-ctl", "-S", "sony15:0x84000d"])

def mdDbass():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840073"])

def mdmenu():
    subprocess.run(["ir-ctl", "-S", "sony15:0x84000a"])

def mdDISCUP():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840033"])

def mdDISCDOWN():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840032"])

def mdlist():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840027"])

def mdback():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840035"])

def mdfwd():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840034"])

def mdsource():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840046"])

def mdsoundmenu():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840010"])

def mdenter():
    subprocess.run(["ir-ctl", "-S", "sony15:0x84005c"])

def mddisplay():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840028"])

def mdAFTA():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840014"])

def mdmode():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840047"])

def mdATT():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840014"])

def mdvolumeup():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840012"])

def mdvolumedown():
    subprocess.run(["ir-ctl", "-S", "sony15:0x840013"])

