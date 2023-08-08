import random

def test(word, guess):
    result = list()
    index = 0
    for letter in word:
        index +=1
        if letter == guess:
            result.append(index-1)
      
    return result

word_list = ["jajko", "cheleb", "cukinia", "pomidor", "drzewo", "dom", "las"]

choice = random.randint(1,len(word_list)-1)
word = word_list[choice]
lives = 8
blanks = [ "_" for x in range(len(word))]
status = False
solution = list()
word_to_show = str()

while lives == 0 or status != True:
    
    guess = input("What letter maybe in magic word?\n")
    if(len(test(word, guess))) == 0:
        print(f"you lost one live and have {lives} left")
        lives -= 1
    else:
        solution.extend(test(word, guess))
    for elem in solution:
        blanks[elem] = word[elem]
    
    for i in range(len(blanks)):
        word_to_show = word_to_show + str(blanks[i])
    
    if word == word_to_show:
        status = True
        print(status)
    else:
        print(word_to_show + f" you have {lives} left")
        word_to_show = ""
if status == False:
    print("You lost")
else:
    print(f"You have WON with {lives} lives and the word was '{word}' ")