from django.http import HttpResponse
from .views import *

def mainpage(request):
    html = "<html>\
            <head>\
            <title>main page</title>\
            </head>\
<body>\
    <p align='center' ><font size='20'>chess</font></p>\
    <p align='center'><font size='12'>hello,wellcome</font></p>\
    <ul>\
    <li><a href='https://www.google.com/' title='Enter'><font size='8'>log in</font></a></li>\
    <p></p>\
    <li><a href='D:\hassan\پروژه\HTML پروژه و\سایت خود\sign up.htm' title='Membership'><font size='8'>sign up</font></a></li>\
    </ul>\
</body>\
</html>"
    return HttpResponse(html)


def login(request):
    html = "<html>\
<head>\
<title>\
    log in\
</title>\
</head>\
<body>\
    <h1 align='center'>log in</h1>\
    <img src='D:\hassan\پروژه\HTML پروژه و\سایت خود\3.jpg' hspace='400' width='500' height='300'/>\
    <form method='post' action='test.cgi'>\
    <p align='center'>name:<input type='text' name='name'/></p>\
    <p align='center'>pessword:<input type='text' name='password'/></p>\
    <p align='center'><input value='play' type='submit'/></p>\
    </form>\
</body>\
</html>"
    return HttpResponse(html)
