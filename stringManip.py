#String Manip

#get single char
text = "Hello"
print(text[1])

#get substring
print(text[2:4])

#remove any space from beggining and end
text = " Eduardo Warick  "
print(text)
print(text.strip())

#get length of string
print(len(text))

#Lower and Upper case string
print(text.lower())
print(text.upper())

#replace string
print(text.replace("d", "I"))

#Split string if it finds the separator
text = "a, b, c, d, e"
print(text.split(","))
