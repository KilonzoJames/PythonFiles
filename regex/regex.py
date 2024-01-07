import re 

# RegEx Example Using the search() Method

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'

res = re.search(my_regex, my_txt, re.IGNORECASE)
print(res)
print("The first occurrence is located at index ", res.start())
print("The first occurrence is located between index", res.start(), "and index", res.end()) # The first occurrence is located between index 6 and index 12

# RegEx Example Using the findall() Method
my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'
res = re.findall(my_regex, my_txt, re.IGNORECASE)

print(res)

#RegEx Example Using the sub() Method
# re.sub(pattern, replacement, string, count, flags)

my_txt = 'Every Friday, we have a standup meeting. The only reason why we might not have a meeting on a Friday is public holiday. That Friday, we talk about what we did in the previous week, and what we are going to do in the week starting from that Friday.'

my_regex = 'friday'

res = re.sub(my_regex, "Monday", my_txt, 4, re.IGNORECASE)
print(res) 

# RegEx Example Using the split() Method
my_txt = "Python and JavaScript and C# and Java and Golang and F#"
my_regex = 'and'

res = re.split(my_regex, my_txt)
print(res) # ['Python ', ' JavaScript ', ' C# ', ' Java ', ' Golang ', ' F#']

# RegEx Example Using the match() Method
my_txt = 'freeCodeCamp'
my_regex_1 = '^freecodecamp$'

res = re.match(my_regex_1, my_txt, re.IGNORECASE)
print(res) #Output: <re.Match object; span=(0, 12), match='freeCodeCamp'>