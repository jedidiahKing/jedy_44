from datetime import datetime
name = input('What is your name? \n')
age = int(input('How old are you? \n'))
hundred = int((100 - age) + datetime.now().year)
print('Hey there %s. You are %s years old. You will turn 100 years old in %s.' % (name, age, hundred))

print('=========================================================================')



num = int(input('Enter a number:'))
if (num % 2) == 0:
    print('{0} is Even'.format(num))
else:
    print('{0} is Odd'.format(num))

print('=========================================================================')




text = 'One good thing about functions is that they can be easily reused in another program'
def count(text):
    txt = text.split(' ')
    for word in txt:
        if 'is' in txt:
            txt.remove('is')
        if 'that' in txt:
            txt.remove('that')
    print(len(txt))
count(text)
print('=========================================================================')



integer_input = int(input("Enter an integer \n"))
result = integer_input * (1 + 11 + 111)
print(result)
print('=========================================================================')



sampleText = "Here is some dummy string containing numbers 19 and 20"
def count_alpha_num(input_text):
    letterCount = 0
    numberCount = 0
    for word in input_text:
        if word.isalpha():
            letterCount=letterCount + 1
    print("Number of Letter:", letterCount)
    print("Number of Digits:", numberCount)
count_alpha_num(sampleText)

print('=========================================================================')


