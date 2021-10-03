# if you are reading a large file into memory with the open() then
# it could crash the program as it would use up all available memory
# a way to solve this is to use StreamIO from the io module
# this is particulary useful when technique for testing any code that
# needs to read an input file
# you can use the return from io.StreamIO() as a mock file handle so that
# your code doesn't have to read an actual file, just a given vlaue that can
# produce lines of text


import io
import os

text = io.StringIO('foo\nbar\nbaz\n')
for line in text:
    print(line, end='')

# solution with StreamIO
# check if args.text is a file
# if it is, replace args.text with the file handle created by opening the file
# otherwise, replace args.text with an io.StringIO() value that will act like
# an open file handle. Note that we need to add a newline to the text so that
# it will look like the lines of input coming from an actual file
# read input (whether file handle or io.StringIO()) line by line
# process line as before
if os.path.isfile(args.text):
    args.text = open(args.text)
else:
    args.text = io.StringIO(args.text + '\n')

args = get_args()
out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
for line in args.text:
    out_fh.write(line.upper())
out_fh.close()
