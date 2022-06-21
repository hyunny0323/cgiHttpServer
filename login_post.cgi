import sys
from urllib.parse import parse_qs

qString = sys.stdin.readline()
qVal = parse_qs(qString)
name = qVal['name'][0]
passwd = qVal['passwd'][0]

responseBody = '<HTML><HEAD><META charset="utf-8"></HEAD><BODY><H1> [POST metho>
    '<BR>Hello '+ name +\
    '<BR> Your password is ' + passwd +\
    '</H1>'\
    '<a href="index.html"> Home </a> <BR></BODY></HTML>'

print(responseBody)
