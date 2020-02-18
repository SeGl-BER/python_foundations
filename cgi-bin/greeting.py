#!/usr/bin/python

import cgi

print("Content-type: text/html")
print ("")

form = cgi.FieldStorage()

name = form.getvalue('username')

print("""
<html>
<body>
<p style="font-family: Verdana, Geneva, sans-serif;">
Welcome to your personal site, %s
</p>
</body>
</html>
""" % name)