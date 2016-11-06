#!/usr/bin/python3
import codecs
import http.cookiejar
import os
import ssl
import time
import re
import urllib
from bs4 import BeautifulSoup

MAIN_URL = 'http://eclass.dongguk.edu/'
PARSER = 'lxml'

if os.name == 'nt':
    PARSER = 'html.parser'

# LOGIN INFO
LOGIN_URL = 'https://eclass.dongguk.edu/User.do?cmd=loginUser'
LOGIN_INFO = {
        'userDTO.userId': 'YourID',
        'userDTO.password': 'YourPW'
        }

# LOGIN OPERATION
cookie_jar = http.cookiejar.LWPCookieJar()
ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ssl_handler = urllib.request.HTTPSHandler(context=ssl_context)

cj_processor = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(ssl_handler, cj_processor)
urllib.request.install_opener(opener)

login_request = urllib.parse.urlencode(LOGIN_INFO)
req = urllib.request.Request(LOGIN_URL, login_request.encode('UTF-8'))
res = urllib.request.urlopen(req)

# GET STUDY MAIN PAGE
url1 = 'http://eclass.dongguk.edu/Study.do?cmd=viewMyCourse&curriculumType=degree&studyAuthor=class_learner'
res = opener.open(url1)
data = res.read().decode('utf-8')
soup = BeautifulSoup(data, PARSER)

html_semesterform = soup.find('span', {'class': 'selectForm'})
html_semesterlist = html_semesterform.find('span', {'class': 'list'})
html_semesteritems = html_semesterlist.find_all('a')

semester_list = []
semester_href = []
semester_name_regex = re.compile(r'[\s\S]*([0-9]{4}년도 .*학기)[\s\S]*')
for item in html_semesteritems:
    semester_list.append(semester_name_regex.sub(r'\1', item.text))
    semester_href.append(item['href'])

for name, href in zip(semester_list, semester_href):
    print('\n' + name + '에 수강했던 강의 목록\n')
    res = opener.open(MAIN_URL + href)
    data = res.read().decode('utf-8')
    soup = BeautifulSoup(data, PARSER)
    course_list = soup.find_all('div', {'class', 'mystudy_directory first'})
    for course in course_list:
        t = course.find('h4').find('span').text
        b = re.sub(r'\n', r'', t)
        c = re.sub(r'\s*(\S.*)', r'\1', b)
        print(c)
    print('\n' + '-' * 20)
