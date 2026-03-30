# python file
def recursive(s):
    if len(s) <= 1:
        return s
    return recursive(s[1:]) + s[0]


print(recursive("abc"))

stringer = "abc"

print(stringer[::-1])
