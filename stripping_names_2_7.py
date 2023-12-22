'''
2-7 Stripping Names:
Use a variable to represent a person's name, and include some whitespace characters at the beginning and the end of the name. Make sure you use each character combination, "\t" and "\n" at least once
	print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(), rstrip() and strip()
'''

name = '\tTom\t'
print(f'{name}\n{name.lstrip()}\n{name.rstrip()}\n{name.strip()}')