import sqlite3

class Search:
    def __init__(self, ID, TableName, RowName, SearchItem):
        try:
            PkID=""
            TrkNo=""
            try:
              TableAndRowName = ("""SELECT * from """+TableName+""" WHERE """+RowName+""" Like '"""+SearchItem+"""' COLLATE NOCASE""")
              #print(TableAndRowName)
              connection = sqlite3.connect('CDLibrary.db') #connects to db
              cursor = connection.cursor()
              print("Established Link With J.E.N.I.")
              cursor.execute(TableAndRowName) #fetches all requested items
              records = cursor.fetchall()
              #print("Total Rows Are: ", len(records))
              if len(records)==0: #runs a second search if the search term returns nothing, this was to handle incomplete search terms, 
                                  #it is no longer needed but kept for potential redundancy
                  TableAndRowName = ("""SELECT * from """+TableName+""" WHERE """+RowName+""" Like '%"""+SearchItem+"""%' COLLATE NOCASE""")
                  cursor.execute(TableAndRowName)
                  records = cursor.fetchall()
                  #print("Total Rows Are: ", len(records))
              #print("Printing Each Row:")
              #TrkNo, AlbId, PkID = '','',''
              for row in records:
                  #print('ID: ', row[0])
                  #print('Name: ', row[1])
                  #print('\n')
                  try: #attempts to get a value for Primary Key, Track Number/ Disc Number and Album Id
                    TrkNo=str(TrkNo)+str(row[2])+' '
                    AlbId=str(row[3])
                    PkID=str(PkID)+str(row[0])+' '
                    self.PkID=PkID
                    self.TrkNo=TrkNo
                    self.AlbId=AlbId
                  except: #if its an artist search it can only get primary key and this is run
                    PkID=str(PkID)+str(row[0])+' '
                    self.PkID=PkID
              #global DiscIds
              #global DiscNos
              #global TrackNos
              #global AlbumIds
            except sqlite3.Error as error:
                  print("J.E.N.I. Output Read Failure")
        except:
            print("No Track Selected For Playback")

class TrackSearch: #same as above but works with multiple inputs
    def __init__(self, ID, TableName, RowName, SearchItem):
        TrkId=""
        TrkNo=""
        AlbId=""
        try:          
          connection = sqlite3.connect('CDLibrary.db')
          cursor = connection.cursor()
          print("Established Link With J.E.N.I.")
          TrackList=list((SearchItem).split())
          TempIndex=0
          while TempIndex < len(TrackList):
            SingleAlbumId=TrackList[TempIndex]
            TableAndRowName = ("""SELECT * from """+TableName+""" WHERE """+RowName+""" Like '"""+SingleAlbumId+"""' COLLATE NOCASE""")
            cursor.execute(TableAndRowName)
            records = cursor.fetchall()
            #print("Total Rows Are: ", len(records))
            if len(records)==0:
                TableAndRowName = ("""SELECT * from """+TableName+""" WHERE """+RowName+""" Like '%"""+SearchItem+"""%' COLLATE NOCASE""")
                cursor.execute(TableAndRowName)
                records = cursor.fetchall()
            #print("Printing Each Row:")
            #TrkNo, AlbId, PkID = '','',''
            for row in records:
                TrkId=str(TrkId)+str(row[0])+' '
                TrkNo=str(TrkNo)+str(row[2])+' '
                AlbId=str(AlbId)+str(row[3])+' '
                self.TrkId=TrkId
                self.TrkNo=TrkNo
                self.AlbId=AlbId
            TempIndex=TempIndex+1
        except sqlite3.Error as error:
            print("J.E.N.I. Output Read Failure")


