import random
import sys
ran_num = random.randint(1000,9999);

print("Hi there");
print("-" * 30);
print("I´ve generated a random 4 digit number for you. Let´s play a game of Bulls a Cows");
print("-" * 30);
print("Enter a number:");
print("-" * 30);

ran_num_set = set(str(ran_num));
while len(ran_num_set) != len(str(ran_num)):
  ran_num = random.randint(1000,9999)
  ran_num_set = set(str(ran_num));
bull = 0
tries = 0
print(ran_num)
while bull != 4:
  tries += 1
  bull = 0
  cow = 0
  play_num = input("guess: ")
  play_num_set = set(str(play_num))
  if len(play_num_set) != len(str(ran_num)):
    print("Enter a 4 digit number with no repeating digits only");
    break
    exit();
  if 1000 > int(play_num) or int(play_num) > 9999:
    print("number must be between 1000 - 9999")
    break
    exit();


  if play_num[0] == str(ran_num)[0]:
    bull += 1;
  if play_num[1] == str(ran_num)[1]:
    bull += 1;
  if play_num[2] == str(ran_num)[2]:
    bull += 1;
  if play_num[3] == str(ran_num)[3]:
    bull += 1;
  if play_num[0] in str(ran_num):
    cow += 1;
  if play_num[1] in str(ran_num):
    cow += 1;
  if play_num[2] in str(ran_num):
    cow += 1;
  if play_num[3] in str(ran_num):
    cow += 1;
  cow = cow - bull;

  if bull == 1:
    print(str(bull) + " bull")
  else:
    print(str(bull) + " bulls");
  if cow == 1:
    print(str(cow) + " cow")
  else:
    print(str(cow) + " cows");
  if bull == 4 and tries == 1:
    print("Correct! you got it first try!")
  elif bull == 4:
    print("it took you " + str(tries) + " attempts");
