import urllib, http.cookiejar, ssl, codecs, subprocess, time
from bs4 import BeautifulSoup

#### LOGIN INFO ####
login_info={
        'userDTO.userId':'YourID',
        'userDTO.password':'YourPW'
        }

#### LOGIN OPERATION ####
cj=http.cookiejar.LWPCookieJar()
https_sslv23_handler=urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
opener=urllib.request.build_opener(https_sslv23_handler,urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
login_url='https://eclass.dongguk.edu/User.do?cmd=loginUser'

login_request=urllib.parse.urlencode(login_info)
req=urllib.request.Request(login_url,login_request.encode('UTF-8'))
res = urllib.request.urlopen(req)

#### UPDATE HISTORY FILE (IF NOT EXIST, CREATE) ####
subprocess.call(["touch","prev_assign1.txt"])
subprocess.call(["touch","prev_assign2.txt"])
subprocess.call(["touch","prev_assign3.txt"])
subprocess.call(["touch","prev_assign4.txt"])
subprocess.call(["touch","prev_assign5.txt"])
subprocess.call(["touch","prev_assign6.txt"])
subprocess.call(["touch","prev_assign7.txt"])


#### LOOP INFINITELY ####
while 1:
    #### No.1 ####
    url1 = 'http://eclass.dongguk.edu/Board.do?cmd=viewBoardContents&boardInfoDTO.boardInfoId=S2016U0002001UCSE404401Q&boardContentsDTO.boardContentsId=BOAD_160312A143056I5e4fdc&boardContentsDTO.contentsNo=7&boardContentsDTO.gongjiYn=N&gubun=V&curPage=1&typeYn=Y'

    res = opener.open(url1)
    data=res.read().decode('utf-8')
    soup=BeautifulSoup(data,"lxml")
    comlists=soup.find_all('div',{'class':'section_gudieline_frame'})

    content=''
    for comment in comlists:
        content+=comment.text

    fr=codecs.open('prev_assign1.txt','r+','utf-8')
    if content!=fr.read():
        as1=1
    else:
        as1=0
    fr.close()
    fw=codecs.open('prev_assign1.txt','w','utf-8')
    fw.write(content)
    fw.close()


    #### No.2 ####
    url2 = 'http://eclass.dongguk.edu/Board.do?cmd=viewBoardContents&boardInfoDTO.boardInfoId=S2016U0002001UCSE404401Q&boardContentsDTO.boardContentsId=BOAD_160312A143038I5e4fdb&boardContentsDTO.contentsNo=6&boardContentsDTO.gongjiYn=N&gubun=V&curPage=1&typeYn=Y'

    res = opener.open(url2)
    data=res.read().decode('utf-8')
    soup=BeautifulSoup(data,"lxml")
    comlists=soup.find_all('div',{'class':'section_gudieline_frame'})

    content=''
    for comment in comlists:
        content+=comment.text

    fr=codecs.open('prev_assign2.txt','r+','utf-8')
    if content!=fr.read():
        as2=1
    else:
        as2=0
    fr.close()
    fw=codecs.open('prev_assign2.txt','w','utf-8')
    fw.write(content)
    fw.close()

    #### No.3 ####
    url3 = 'http://eclass.dongguk.edu/Board.do?cmd=viewBoardContents&boardInfoDTO.boardInfoId=S2016U0002001UCSE404401Q&boardContentsDTO.boardContentsId=BOAD_160312A143021I5e4fda&boardContentsDTO.contentsNo=5&boardContentsDTO.gongjiYn=N&gubun=V&curPage=1&typeYn=Y'

    res = opener.open(url3)
    data=res.read().decode('utf-8')
    soup=BeautifulSoup(data,"lxml")
    comlists=soup.find_all('div',{'class':'section_gudieline_frame'})

    content=''
    for comment in comlists:
        content+=comment.text

    fr=codecs.open('prev_assign3.txt','r+','utf-8')
    if content!=fr.read():
        as3=1
    else:
        as3=0
    fr.close()
    fw=codecs.open('prev_assign3.txt','w','utf-8')
    fw.write(content)
    fw.close()

    #### No.4 ####
    url4 = 'http://eclass.dongguk.edu/Board.do?cmd=viewBoardContents&boardInfoDTO.boardInfoId=S2016U0002001UCSE404401Q&boardContentsDTO.boardContentsId=BOAD_160312A143001I5e4fd9&boardContentsDTO.contentsNo=4&boardContentsDTO.gongjiYn=N&gubun=V&curPage=1&typeYn=Y'

    res = opener.open(url4)
    data=res.read().decode('utf-8')
    soup=BeautifulSoup(data,"lxml")
    comlists=soup.find_all('div',{'class':'section_gudieline_frame'})

    content=''
    for comment in comlists:
        content+=comment.text

    fr=codecs.open('prev_assign4.txt','r+','utf-8')
    if content!=fr.read():
        as4=1
    else:
        as4=0
    fr.close()
    fw=codecs.open('prev_assign4.txt','w','utf-8')
    fw.write(content)
    fw.close()

    #### No.5 ####

    url5 = 'http://eclass.dongguk.edu/Board.do?cmd=viewBoardContents&boardInfoDTO.boardInfoId=S2016U0002001UCSE404401Q&boardContentsDTO.boardContentsId=BOAD_160312A142935I5e4fd3&boardContentsDTO.contentsNo=3&boardContentsDTO.gongjiYn=N&gubun=V&curPage=1&typeYn=Y'

    res = opener.open(url5)
    data=res.read().decode('utf-8')
    soup=BeautifulSoup(data,"lxml")
    comlists=soup.find_all('div',{'class':'section_gudieline_frame'})

    content=''
    for comment in comlists:
        content+=comment.text

    fr=codecs.open('prev_assign5.txt','r+','utf-8')
    if content!=fr.read():
        as5=1
    else:
        as5=0
    fr.close()
    fw=codecs.open('prev_assign5.txt','w','utf-8')
    fw.write(content)
    fw.close()

    #### No.6 ####
    url6 = 'http://eclass.dongguk.edu/Board.do?cmd=viewBoardContents&boardInfoDTO.boardInfoId=S2016U0002001UCSE404401Q&boardContentsDTO.boardContentsId=BOAD_160312A142917I5e4fd2&boardContentsDTO.contentsNo=2&boardContentsDTO.gongjiYn=N&gubun=V&curPage=1&typeYn=Y'

    res = opener.open(url6)
    data=res.read().decode('utf-8')
    soup=BeautifulSoup(data,"lxml")
    comlists=soup.find_all('div',{'class':'section_gudieline_frame'})

    content=''
    for comment in comlists:
        content+=comment.text

    fr=codecs.open('prev_assign6.txt','r+','utf-8')
    if content!=fr.read():
        as6=1
    else:
        as6=0
    fr.close()
    fw=codecs.open('prev_assign6.txt','w','utf-8')
    fw.write(content)
    fw.close()

    #### No.7 ####
    url7 = 'http://eclass.dongguk.edu/Board.do?cmd=viewBoardContents&boardInfoDTO.boardInfoId=S2016U0002001UCSE404401Q&boardContentsDTO.boardContentsId=BOAD_160312A142851I5e4fd1&boardContentsDTO.contentsNo=1&boardContentsDTO.gongjiYn=N&gubun=V&curPage=1&typeYn=Y'

    res = opener.open(url7)
    data=res.read().decode('utf-8')
    soup=BeautifulSoup(data,"lxml")
    comlists=soup.find_all('div',{'class':'section_gudieline_frame'})

    content=''
    for comment in comlists:
        content+=comment.text

    fr=codecs.open('prev_assign7.txt','r+','utf-8')
    if content!=fr.read():
        as7=1
    else:
        as7=0
    fr.close()
    fw=codecs.open('prev_assign7.txt','w','utf-8')
    fw.write(content)
    fw.close()

    ## Debug Message ##
    #print('check OK / code :'+str(as1)+str(as2)+str(as3)+str(as4)+str(as5)+str(as6)+str(as7))

    ## Send Message ##
    if as1 or as2 or as3 or as4 or as5 or as6 or as7:
        subprocess.call(["../send_telegram.sh","민혁_정","Some Assignment was changed!"+str(as1)+str(as2)+str(as3)+str(as4)+str(as5)+str(as6)+str(as7), ""])
    time.sleep(10)
