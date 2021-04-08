import random

a = random.randint(0,20)
b = random.randint(21,30)
c = random.randint(31,40)
d = random.randint(41,50)
e = random.randint(51,60)

number_of_guesses = 0
counter = 4

print("Welcome please pick one of these numbers and you might win\n")

print(a,b,c,d,e)

while number_of_guesses < 4:
    
    x = int(input("\nChoose: "))

    number_of_guesses += 1

    if x == a:
        counter -= 1
        print("Wrong, please try again, remaining tries: ", counter)
    elif x == b:
        counter -= 1
        print("Wrong, please try again, remaining tries: ", counter)
    elif x == d:
        counter -= 1
        print("Wrong, please try again, remaining tries: ", counter)
    elif x == e:
        counter -= 1
        print("Wrong, please try again, remaining tries: ", counter)
    elif x == c:
        print("You won!")
        break
    else:
        counter -= 1
        print("Wrong, your input is not in the list please try again, remaining tries: ", counter)

else:
    print("Sorry you ran out of tries! the correct number is: ", c)
