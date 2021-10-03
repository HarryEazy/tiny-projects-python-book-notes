# yapf formats code
# yapf -i hello.py -> formats code in place so original file is replaced
#
# Access boiler plate code
# bin/new.py NAMEOFPROGRAME.py
# can also copy the file to new directory
# cp template/template.py dir/name.py

# use pytest -v test.py to run test program
# -v stands for verbose output
# -x stops on the first test failing
# can combine these as -xv or -vx

# which python3 -> to find directory of python3

# tells os to use path to find python to interpret this program
#! /usr/bin/env python3

# making a program executable
# since we have the shebang, we can execute the program directly and let the os
# figure out that it should use python3
# the advantage of this is that we could copy our program to a directory
# where other programs live and execute it from anywhere on our computer

# first step is to make our program executable using chmod(change mode)
# think of this as turning your program on
# the '+x' will add an executable attribute to the file
# chmod +x hello.py

# now we can run the program like this
# './' is the current directory and it is necessary to run a program when you
# are in the same directory as the program
# ./hello.py

# one of the biggest reasons to put the shebang is so that we can install
# the python program just like other commands and programs
# echo $path is a list of directories the os will look in to find a program
# if your file is in any dir in this list then you can run it from any directory
# even if you are not in the current directory
# so it is a way of telling you os where to look to find executable programs
# you can control both the names of the dirs in the $PATH variable and
# their relative order so that the os will find the programs you need

# it is very common for our programs to be installed into /usr/local/bin
# so we will copy our program to there using 'cp' command
# use rm file_name.txt to delete
# cp hello.py /usr/local/bin

# Altering your $PATH
# create a bin for the home directory
# home directory can be written as '~'
# can also you $HOME/bin where $HOME is the name of your home directory
#
# mkdir ~/bin
# cp 01_hello/hello.py ~/bin
# PATH=~/bin:$PATH
# which hello.py

# although th shabang and the executable stuff may seem like a lot of work
# it allows you to create a python program that can be installed onto your
# computer or anyone else's and run just like any other program

# --help and -h for help
# ./hello.py -h -> should display a message regarding help using program
# most programs have a -h help function

# using the argparse module, we can give inputs to our program
import argparse
# the parser will figure out all the args
# the description will appear in the help message
parser = argparse.ArgumentParser(description='Say hello')
# we need to tell the parser to expect a name that will be the obj of our salutations
parser.add_argument('name', help='Name to greet')
# ask the parser to parse any arguments to the program
args = parser.parse_args()
# print greeting
print(f'Hello, {args.name}!')
# to make the name arg optional we need to use '--name'
# -n for the 'short' and --name for the 'long' it is common to do this
# to make it easy to type the options
# PARAMS that start with '-' are optional
# so we can run ./hello.py --name Terra
# ./hello.py -n Terra
# metavar will show up in the usage to describe the argument
# we also have a default value
parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')

# now we need to add main function
# every program or module in Python has a name that can be accessed through
# __name__
# when executing __name__ is set to __main__.1

# create seperate function to get_args() at the top of file so that we can see
# it straight away when viewing source code
# put the main function straight after it

# if there is a problem with the args or if the user asks for --help the program
# never executes because of argparse

# Make program and Makefiles can be used to execute complicated set of commands
# he created a file called Makefile in every directory
# to show file run cat Makefile on cmd line
.PHONY: test

test:
        pytest -xv test.py

# need to have make installed on computer mine worked and I didnt install anything
# then run make test
# make will look for a Makefile in you current working dir and then look for a
# recipe called 'test' there it will find that the command to run for the 'test'
# target is pytest -xv test.py
# so it will run that command


# he also has a new.py file in bin/new.py to be able to create a new file
# has some boiler plate code
# bin/new.py 01_hello/hello2.py

# remove file
# rm filename
# rm -r folder name
