import webbrowser
import feedparser
import linecache
import os

####https://kickass.unblocked.li/usearch/%22DC%20Week%2B%22/?rss=1.xml

def Fetchnextentry(currentnum,url):
    os.system('cls' if os.name == 'nt' else 'clear')
    ent=currentnum+1

    d = feedparser.parse(url)

    print("Next Entry\n",d["entries"][ent]["title"],"-",d["entries"][ent]["link"])


    print("ADD TORRENT Y/N        --OR press enter for next result")
    YN=input()


    if YN=="":
        Fetchnextentry(ent,url)



    elif (YN=="Y") or (YN=="y"):
        magnet=d.entries[ent].torrent_magneturi
        webbrowser.open_new_tab(magnet)

        file="RSSDATA/"+RSS+".txt"
        with open(file, "w") as file:
               file.writelines(d["entries"][ent]["title"])


    elif (YN=="N") or (YN=="n"):
        return


    else:
        FetchLatestKATTorrrent(RSS+" "+YN)


def FetchLatestKATTorrrent(RSS):
    os.system('cls' if os.name == 'nt' else 'clear')
    ent=0


    if int==True:
        RSS=RSS[:-1]

    print(RSS)

    RSS=RSS.replace (" ", "%20")            ##CONVERT SPECIAL ASCII IN INPUT TO HEXIDECIMAL




    url="https://kickass.unblocked.li/usearch/"+RSS+"/?rss=1.xml"
    #print(url)


    d = feedparser.parse(url)


    print("Latest entry\n",d["entries"][ent]["title"],"-",d["entries"][ent]["link"])

    lastdate=linecache.getline("RSSDATA/"+RSS+".txt", 1)
    lastdate=lastdate[:-1]
    #print(lastdate)



    #(d.entries[0].updated)             ##checks for update to item

    ##USE REGEX TO FIND ISSUE NUMBER IN FEED TITLE

    #   !=lastdate:
    #   print("New entry, adding torrent")
    #   with open("RSSDATA/"+RSS+".txt", "w") as file:
    #        file.writelines(d.entries[0].updated)

    print("ADD TORRENT Y/N        --OR press enter for next result")
    YN=input()


    if YN=="":
        Fetchnextentry(ent,url)
        ##MAKE SHIT RECURSIVE!!



    elif (YN=="Y") or (YN=="y"):
        magnet=d.entries[ent].torrent_magneturi
        webbrowser.open_new_tab(magnet)

       # file = open("RSS.txt, "w")
       # file.write("SHOWNAME:")
        RSS=RSS.replace ("\"", "")


        file="RSSDATA/"+RSS+".txt"
        with open(file, "w") as file:
               file.writelines(d["entries"][ent]["title"])





    elif (YN=="N") or (YN=="n"):
        return


    else:
        FetchLatestKATTorrrent(RSS+" "+YN)
    ##FETCH SECOND ENTRY1





    #if CHECK FOR PLAIN TEXT OR 3 DIGITS



def fetchfromlistfile():

    numofcomics= int(linecache.getline("RSSDATA/list.txt", 1))

    print(numofcomics,"Items in list file\n\n")


    x=2
    while x<=numofcomics+1:

        print(x-1,". ",linecache.getline("RSSDATA/list.txt", x),sep='')

        itemname=linecache.getline("RSSDATA/list.txt", x)
        itemname=itemname[:-1]

        lastfile=itemname+".txt"

        lastfile="RSSDATA/"+lastfile
        #print("read",lastfile)
        last=linecache.getline(lastfile, 1)
        if last!="":
            print ("Last Download::",last)


        x += 1

    return numofcomics






numofcomics=fetchfromlistfile()




print("Enter number of item to select or type new search term")
userInput=input()


try:
   intenter = int(userInput)
except ValueError:
   int=False


if int==False:
    FetchLatestKATTorrrent(userInput)
    print("Entered term doesn't seem to be in list, would you like to add it? (I didn't check much)")




    print("BRIDGE OUT")

elif intenter<=numofcomics:
    RSS=linecache.getline("RSSDATA/list.txt", intenter+1)
    RSS=RSS[:-1]
    FetchLatestKATTorrrent(RSS)

else:
    print("Input out of range")



#TODO option to Add input thats not in list to list


#TODO Error handling for invalid urls (Feedparser out of range)


#KATRSScheck("https://kickass.unblocked.li/usearch/%22DC%20Week%2B%22/?rss=1.xml")