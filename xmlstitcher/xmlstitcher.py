import os
import sys
import re
import shutil

if os.path.exists("types.xml"):
    os.remove("types.xml")
os.system('touch types.xml')

if os.path.exists("modsxml/README.md"):
    os.remove("modsxml/README.md")
if os.path.exists("originalxml/README.md"):
    os.remove("originalxml/README.md")

f = open('originalxml/types.xml', "r")
copy = open("types.xml", "w")
for line in f:
    if re.match(r'^\s*$', line):
        print('Empty line found, skipping')
    elif re.match(r'</types>', line):
        print('Found </types>, skipping')
        print(line)
    else:
        copy.write(line)
copy.write('\n')
f.close()
copy.close()

listfiles = os.listdir('modsxml')
print('Appending the following files: \n')
print(listfiles)
for xmls in listfiles:
    modlink = "modsxml/" + xmls
    f = open(modlink, "r")
    copy = open("types.xml", "a")
    for line in f:
        if re.match(r'^\s*$', line):
            print('Empty line found, skipping')
        elif re.match(r'<\?xml version', line):
            print('removing headliner')
        elif re.match(r'<types>', line):
            print('Found <types>, skipping')
        elif re.match(r'</types>', line):
            print('removing trailing </types>, skipping')
        else:
            copy.write(line)
    f.close()
copy.write('</types>')
copy.close()