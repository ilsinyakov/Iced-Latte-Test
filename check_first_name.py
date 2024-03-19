import string


first_name = str(input("Please, input First Name: "))
pattern = string.ascii_letters + ' ' + '-'

assert len(first_name) >= 2 and len(first_name) <= 128, "The length of the fist name must be from 2 to 128 symbols"

for char in first_name:
    assert char in pattern, "First name can only contain Latin letters, spaces, and hyphens"
