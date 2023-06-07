#!/usr/bin/env python3
#Script: Ops 401 Class 36 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:06/06/2023
# Assistance from Chat GPT

# Main

import requests
import webbrowser

targetsite = "http://www.whatarecookies.com/cookietest.asp" 
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): 
    print('''

      .---. .---.
     :     : o   :    me want cookie!
 _..-:   o :     :-.._    /
.-''  '  `---' `---' "   ``-.
.'   "   '  "  .    "  . '  "  `.
:   '.---.,,.,...,.,.,.,..---.  ' ;
`. " `.                     .' " .'
`.  '`.                   .' ' .'
`.    `-._           _.-' "  .'  .----.
  `. "    '"--...--"'  . ' .'  .'  o   `.
    (.)(.)                 (.)(.)      \o/

    ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Sending cookie back to site
cookie_response = requests.get(targetsite, cookies=cookie)

# Generate an HTML file
with open('response.html', 'w') as f:
    f.write(cookie_response.text)

# Open it with Firefox
webbrowser.get('firefox').open_new_tab('response.html')

# Done