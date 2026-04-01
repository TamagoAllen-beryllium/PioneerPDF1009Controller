import time
from JENIHex import *
import random

class GenAlbumNumbers:
    def __init__(self, DID, DNo, AID):
        dict={DID[i]: DNo[i] for i in range(len(DID))}  #associate the album number with their disc number
        self.ANo = [dict[j] for j in AID]               #swap the album number for the disc number
        
class TruncateTracks:
    def __init__(self, TrackNo,DiscNo):
        del TrackNo[36:]		#cull after 36 items
        del DiscNo[36:]			#cull after 36 items
        
class ConvertToShuffled:
    def __init__(self, TrackNo, DiscNo):        
        temp=list(zip(TrackNo, DiscNo)) #merge to 1 list
        random.shuffle(temp)		#shuffle merged
        self.TrackNo, self.DiscNo=zip(*temp) #unmerge back to 2 lists
               
class ConvertToIR:
    def __init__(self, TrackNo, DiscNo):
        CodeDictionary = {'1':KEY1,'2':KEY2,'3':KEY3,'4':KEY4,'5':KEY5,'6':KEY6,'7':KEY7,'8':KEY8,'9':KEY9,'0':KEY0}
        cdstop()
        cdstop()				#to stop any already running operations
        cdprogram()			#start of input to player
        TrackDex=0
        while TrackDex < len(TrackNo):  #for as many tracks as there are
            DiscChar = DiscNo[TrackDex]
            TrackChar = TrackNo[TrackDex]
            for Char in DiscChar:       #for each digit in the disc number of that track
                CodeDictionary[Char]()
                time.sleep(0.1)
            cddisc()			#end disc code
            for Char in TrackChar:      #for each digit in the track number of that track
                CodeDictionary[Char]()
                time.sleep(0.1)
            cdtrack()			#end track code
            TrackDex = TrackDex+1
        cdplay()				#begin playback
     
