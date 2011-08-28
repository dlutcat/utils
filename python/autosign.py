#!/usr/bin/python
# -*- coding: utf-8 -*-
#title       : autosign.py
#description : Autosign file metadata ahead of file.
#author      : Patto (pat.inside@gmail.com)
#date        : 2011-08-28

# Import the modules needed to run the script.
import os, sys
import getopt
from os.path import exists
from time import strftime

# Support file types
FILE_TYPES = {
  'python':     'py',
  'javascript': 'js',
  'c':          'c' 
}

def parse_args(args):
  """ Parse args given to program. """

  try:
    opts = getopt.getopt(args, 'ht:', ['help'])[0]
  except:
    print_help()
    sys.exit(1)

  return_args = {
    'type': 'python'
  }

  for opt, val in opts:
    if opt in ("-h", "--help"):
      print_help()
      sys.exit(1)
    elif opt in ('-t', '--type'):
      return_args['type'] = val

  return return_args

def print_help():
  """ Print help information """

  print_head()
  print
  print_usage()

def print_head():
  print "Autosign - Auto sign programmer information when file created!"
  print "Made by Patto (pat.inside@gmail.com)"
    
def print_usage():
  print "Usage: %s [-h | --help] - display help information." % sys.args[0]
  print
  print "-t | --type: specifies the file type that is to be created."
  print "             Support python, javascript, c now."
  print 
  print " Valid example:"
  print " %s -t python" % sys.args[0]
  print " %s --type=python" % sys.args[0]
  print " %s -t javascript" % sys.args[0]
  print " %s --type=javascript" % sys.args[0]
  print " %s -t c" % sys.args[0]
  print " %s --type=c" % sys.args[0]

def main(type):
  """ Main logic"""

  title = raw_input("Enter a title for your script: ")
  descrpt = raw_input("Enter a description: ")
  name = raw_input("Enter author: ")
  #ver = raw_input("Enter the version number: ")

  # Add extend name to the end of the script.
  title = title + '.' + FILE_TYPES[type]

  # Check to see if the file exists to not overwrite it.
  if exists(title):
      print "\nA script with this name already exists."
      exit(1)

  # Create a file that can be written to.
  filename = open(title, 'w')

  # Set the date automatically.
  date = strftime("%Y-%m-%d")

  # Write the data to the file. 
  if type == 'python':
    filename.write('#!/usr/bin/python')
    filename.write('\n# -*- coding: utf-8 -*-')
    filename.write('\n#title       : ' + title)
    filename.write('\n#description : ' + descrpt)
    filename.write('\n#author      : ' + name)
    filename.write('\n#date        : ' + date)
    filename.write('\n')
    filename.write('\n')

  elif type in ('javascript', 'c'):
    filename.write('/*')
    filename.write('\n * @title       : ' + title)
    filename.write('\n * @description : ' + descrpt)
    filename.write('\n * @author      : ' + name)
    filename.write('\n * @date        : ' + date)
    filename.write('\n *')
    filename.write('\n */')
    filename.write('\n')
    filename.write('\n')

  # Close the file after writing to it.
  filename.close()

  # Open the file using the editor vim.
  os.system("vim +12 " + title)
  ## end of http://code.activestate.com/recipes/577846/ }}}

if __name__ == '__main__':
  try:
    args = parse_args(sys.argv[1:])
  except:
    print_usage()
    sys.exit(1)

  main(type=args['type'])
