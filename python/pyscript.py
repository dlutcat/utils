#!/usr/bin/python
#title           :pyscript.py
#description     :This will create a header for a python script.
#author          :bgw
#date            :20110805
#version         :0.2    
#usage           :python pyscript.py
#notes           :       
#python_version  :2.6.6  
#==============================================================================

# Import the modules needed to run the script.
import os
from os.path import exists
from time import strftime

title = raw_input("Enter a title for your script: ")
descrpt = raw_input("Enter a description: ")
name = raw_input("Enter your name: ")
ver = raw_input("Enter the version number: ")
div = '======================================='

# Add .py to the end of the script.
title = title + '.py'

# Check to see if the file exists to not overwrite it.
if exists(title):
    print "\nA script with this name already exists."
    exit(1)

# Create a file that can be written to.
filename = open(title, 'w')

# Set the date automatically.
date = strftime("%Y%m%d")

# Write the data to the file. 
filename.write('#!/usr/bin/python')
filename.write('\n#title\t\t\t:' + title)
filename.write('\n#description\t:' + descrpt)
filename.write('\n#author\t\t\t:' + name)
filename.write('\n#date\t\t\t:' + date)
filename.write('\n#version\t\t:' + ver)
filename.write('\n#usage\t\t\t:' + 'python ' + title)
filename.write('\n#notes\t\t\t:')
filename.write('\n#python_version\t:2.6.6')
filename.write('\n#' + div * 2 + '\n')
filename.write('\n')
filename.write('\n')

# Close the file after writing to it.
filename.close()

# Open the file using the editor vim.
os.system("vim +12 " + title)
## end of http://code.activestate.com/recipes/577846/ }}}
