myString = "hello world"

print("Original string:", repr(myString))
print("=" * 50)

# Case conversion methods
print("capitalize():", myString.capitalize())
print("casefold():", myString.casefold())
print("lower():", myString.lower())
print("upper():", myString.upper())
print("swapcase():", myString.swapcase())
print("title():", myString.title())

print("-" * 50)

# Alignment and padding methods
print("center(20, '*'):", myString.center(20, '*'))
print("ljust(20, '-'):", myString.ljust(20, '-'))
print("rjust(20, '-'):", myString.rjust(20, '-'))
print("zfill(20):", myString.zfill(20))

print("-" * 50)

# Search and find methods
print("count('l'):", myString.count('l'))
print("find('world'):", myString.find('world'))
print("find('xyz'):", myString.find('xyz'))
print("rfind('l'):", myString.rfind('l'))
print("index('world'):", myString.index('world'))
print("rindex('l'):", myString.rindex('l'))

print("-" * 50)

# Boolean check methods
print("startswith('hello'):", myString.startswith('hello'))
print("endswith('world'):", myString.endswith('world'))
print("isalnum():", myString.isalnum())
print("isalpha():", myString.isalpha())
print("isascii():", myString.isascii())
print("isdecimal():", myString.isdecimal())
print("isdigit():", myString.isdigit())
print("isidentifier():", myString.isidentifier())
print("islower():", myString.islower())
print("isnumeric():", myString.isnumeric())
print("isprintable():", myString.isprintable())
print("isspace():", myString.isspace())
print("istitle():", myString.istitle())
print("isupper():", myString.isupper())

print("-" * 50)

# Strip methods
paddedString = "  hello world  "
print("Original padded:", repr(paddedString))
print("strip():", repr(paddedString.strip()))
print("lstrip():", repr(paddedString.lstrip()))
print("rstrip():", repr(paddedString.rstrip()))

print("-" * 50)

# Split and join methods
print("split():", myString.split())
print("split('o'):", myString.split('o'))
print("rsplit('l', 1):", myString.rsplit('l', 1))
print("splitlines():", "hello\nworld".splitlines())
print("partition('o'):", myString.partition('o'))
print("rpartition('o'):", myString.rpartition('o'))
print("join('-'):", '-'.join(myString))

print("-" * 50)

# Replace and translate methods
print("replace('world', 'python'):", myString.replace('world', 'python'))
print("expandtabs():", "hello\tworld".expandtabs(4))

table = str.maketrans('helo', 'HELO')
print("translate(h->H, e->E, l->L, o->O):", myString.translate(table))

print("-" * 50)

# Encoding method
print("encode('utf-8'):", myString.encode('utf-8'))

print("-" * 50)

# Format methods
print("format example:", "{} {}".format("hello", "world"))
print("format_map example:", "{greeting} {target}".format_map(
    {'greeting': 'hello', 'target': 'world'}
))

print("-" * 50)

# Prefix/suffix removal (Python 3.9+)
print("removeprefix('hello'):", myString.removeprefix('hello'))
print("removesuffix('world'):", myString.removesuffix('world'))

print("-" * 50)

# String representation
print("len():", len(myString))
print("list(myString):", list(myString))
print("reversed:", ''.join(reversed(myString)))
print("slicing [0:5]:", myString[0:5])
print("'hello' in myString:", 'hello' in myString)
print("concatenation:", myString + "!")
print("repetition (* 3):", myString * 3)
