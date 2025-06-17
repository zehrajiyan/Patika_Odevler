score = int(input('Enter your score: '))

if 80 <= score <= 100 :
    print('A')
elif 60 <= score < 80:
    print('B')
elif 40 < score < 60:
    print('C')
else:
    print('F')