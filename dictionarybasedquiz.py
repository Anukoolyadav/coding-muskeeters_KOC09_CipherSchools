import random
lst = ['What is the capital of Indonesia?', 'Who was the last Tsar of Russia?', 'What country drinks the most coffee per capita?', 'What company was initially known as Blue Ribbon Sports', 'Kratos is the main character of what video game series?', 'What Netflix show had the most streaming views in 2021?', 'What software company is headquartered in Redmond, Washington?',
       'In what country is the Chernobyl nuclear plant located', 'What disease commonly spread on pirate ships?', 'What year was the United Nations established?', 'What artist has the most streams on Spotify?', 'What country has the highest life expectancy?', 'What company was originally called "Cadabra"?', 'What character has both Robert Downey Jr. and Benedict Cumberbatch played?', 'What city is known as The Eternal City?']
lst2 = [['Bali', 'Paris', 'Jakarta', 'Kuala Lumpur'], ['Nicholas 2', 'Nicholas 1', 'Boris Godunov', 'Michael 1'], ['Finland', 'Germany', 'Oman', 'USA'], ['Nike', 'Adidas', 'Dior', 'Burberry'], ['God of War', 'Uncharted', 'Rainbow 6 Siege', 'Fortnite'], ['Squid Game', 'Mirzapur', 'The Queens Gambit', 'Alba'], ['Microsoft', 'Windows', 'DeShawn', 'Apple'], ['Russia', 'Ukraine',
                                                                                                                                                                                                                                                                                                                                                                     'USA', 'Belarus'], ['Scurvy', 'Diabetes', 'Cardiac Arrest', 'Dysentry'], ['1945', '1986', '1921', '1934'], ['Kanye West', 'Drake', 'Taylor Swift', 'Chainsmokers'], ['India', 'Hong Kong', 'Portugal', 'Germany'], ['Amazon', 'Myntra', 'Oracle', 'Tesla'], ['Iron Man', 'Sherlock Holmes', 'Doctor Strange', 'Captain America'], ['Rome', 'Berlin', 'St. Petersburg', 'London']]
lst3 = [3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1]
print("WELCOME TO THE GUESSING GAME!")
Score = 0
QNumber = 0
x = True
v1 = None
while x:
    print('DO YOU WANT TO PLAY THIS GAME?')
    print('1-->Yes')
    print('2-->No')
    x = int(input(""))
    if x == 1:
        x = True
        lst4 = []
        for i in range(10):
            val = random.randint(0, 14)
            if val not in lst4:
                lst4 += val,
            if len(lst4) == 5:
                break
        #print(lst4)
        count = 0
        for i in range(len(lst4)):
            print(f'------------QUESTION {i+1} --------------------')
            v = lst4[i]
            print(lst[v])
            for j in range(len(lst2[v])):
                print(f'{j+1}--> {lst2[v][j]}')
            ans = lst3[lst4[i]]
            # print(ans)
            user = int(input('Give it a guess: '))
            if user == ans:
                count += 1

            print('\n\n')
        print('-'*140)
        print(' '*40, f'Yay! you have scored {count} points out of 5', ' '*40)
        print('-'*140)
        break

    else:
        v1 = 1
        break


if v1 == 1:
    print("Will wait for you")
else:
    print('Thank You ')
