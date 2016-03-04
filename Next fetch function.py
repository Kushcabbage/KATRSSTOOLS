def Fetchnextentrie(currentnum):
    os.system('cls' if os.name == 'nt' else 'clear')
    ent=currentnum+1

    d = feedparser.parse(url)

    print("Next Entry\n",d["entries"][ent]["title"],"-",d["entries"][ent]["link"])


    print("ADD TORRENT Y/N        --OR press enter for next result")
    YN=input()


    if YN=="":
        print("lol not programmed yet ;)")
        input()
        ##MAKE SHIT RECURSIVE!!



    elif (YN=="Y") or (YN=="y"):
        magnet=d.entries[ent].torrent_magneturi
        webbrowser.open_new_tab(magnet)



    elif (YN=="N") or (YN=="Y"):
        pass


    else:
        FetchLatestKATTorrrent(RSS+" "+YN)