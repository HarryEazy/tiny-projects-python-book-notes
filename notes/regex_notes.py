import re

pattern = 'abcdefg'
text = 'acxt'
# search() will match starting anywhere in the text
re.search(pattern, text)
# match() starts from the beginning of the text
re.match(pattern, text)

# to match 1 or more '+' after pattern
match = re.match(f'([{pattern}]+)', text)
# <re.Match object; span=(0, 2), match='ac'> - return None if not successfull

# use groups to capture groups if the regex matches successfully
match.groups()
# ('ac',)

# to capture everything that comes after the match we can use a period '.'
# here we also use '+' sign to get 1 or more
match = re.match(f'([{pattern}]+)(.+)', text)
# ('ac', 'xt')

# because regex returns none when no match has been made
# we can use '?' to indicate optional match
match = re.match(f'([{pattern}]+)?(.+)', text)
match.groups()
# (None, 'apple')

# to get a group
match.group(1)
match.group(2)

# to specify case-insensitive searching use IGNORECASE
match = re.match(f'([{pattern}]+)?(.+)', text, re.IGNORECASE)

# (.*) '*' zero or more

# shorthand expressions
# \d -> means any digit '[0123456789]'
# \s -> whitespace -> \t\n\r\x0b\x0c same as string.whitespace
# \w word characters -> [a-zA-Z0-9_-]
# ^ to negate basically ~ not
# \D+ -> matches one or more non-digits
# \W -> matches non-word characters
# \S Not white space

# pylint will complain using \W so we need to use raw string instead
# re.split(r'\W', 'abc123')
# re.split() omits those strings matching the pattern
# help(re.split) :
# if capturing parentheses are used in [the] pattern, then the text of all
# groups in the pattern are also returned as part of the resulting string
# so we need to wrap the expression in ()
# re.split(r'(\W'), 'abc123')


