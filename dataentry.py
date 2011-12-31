#this is a very very basic python program that ask some questions and recalls the aswers i am makeing this and posting it on github because i am taking the learn python the hard way course and in one of the exercises it asks you to go look for code and i could not find any simple code so I made some! there will more likely be some more code to come so look for it thanks.
prompt = '>'
print 'To contine press ENTER, to quit press CTRL- C (^C)'
raw_input(prompt)
print 'What is your name?'
name = raw_input(prompt)
print 'How old are you?'
age = raw_input(prompt)
print 'Do you like basic python?'
answer = raw_input(prompt)

print '''
Hello, %r.
Your %r years old.
Do you like basic python: %r''' % (name, age, answer)
