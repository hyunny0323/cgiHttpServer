import sys
import os
from urllib.parse import parse_qs

qString = os.environ['QUERY_STRING']

#qString = sys.stdin.readline() // for POST method

qVal = parse_qs(qString)
name = qVal['name'][0]
passwd = qVal['passwd'][0]

responseBody = f'<HTML><HEAD><META charset="utf-8"></HEAD>'\
               f'<BODY><H1> [GET method]' \
               f'<BR>Hello {name}'\
               f'<BR> Your password is {passwd} </H1><BR>'\
               f'<a href="index.html"> Home </a> <BR> </BODY></HTML>'

print(responseBody)
