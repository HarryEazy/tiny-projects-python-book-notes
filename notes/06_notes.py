# sys.stdin is the standard place to read input on the cmd line
# we can chain the stdout from one program to the stdin of another
# to create ad hoc programs
# for instance, the 'cat' program will print the contents of a file to stdout
# We can use the pipe operator '|' to funnel that output as input into out program
# via stdin
$ cat ../inputs/fox.txt | ./wc.py

# another option is to use the '<' operator to redirect input from a file
$ ./wc.py < ../inputs/fox.txt

# one of the handiest command-line tools is 'grep'
# which can find patterns of text in files.
# if we wanted to find all the lines of text that contain the word 'scarlet'
# in all the files in the inputs directory, we could use this command
$ grep scarlet ../inputs/*.txt
# on the cmd line the asterisk is a wildcard that will match anything
# so *.txt will match any file ending with .txt

# so to find the lines found by grep we can pipe that output into our wc.py
$ grep scarlet ../inputs/*.txt | ./wc.py
# we can verify
$ grep scarlet ../inputs/*.txt | wc

# nargs='+' indicates 1 or more args
# nargs='*' indicates 0 or more
# nargs='?' indicates 0 or 1

# get argparse to validate the argument and make sure it is a file
# type=argparse.FileType('rt')
# this means argparse takes on all the work to validate the argument

# sys.stdin file handle does not need an open() it is always present and
# available for reading

# because we are using nargs='*' to define our arg, the result will always
# be a list. to set sys.stdin as the default value, we should place it in a list
default=[sys.stdin]

# zero or more of this arg
# if args are provided they mus be readable text files
# the files will be opened by argparse and will be provided as file handles
# the default will be a list containing sys.stdin which is like an open
# file handle to stdin we dont need to open it
parser.add_argument('file',
                    metavar='FILE',
                    nargs='*',
                    default=[sys.stdin],
                    type=argparse.FileType('rt'),
                    help='Input file(s)')

# format using format string
f'Pi is {math.pi:0.02f}'
