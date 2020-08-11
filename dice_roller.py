import random
def main():
  player = str(input("Enter your name "))
  dice_rolls = 2
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    if roll == 1:
      print(f'{player} You rolled a {roll}! Critical Fail')
    elif roll == 6:
      print(f'{player} You rolled a {roll}! Critical Success!')
    else:
      print(f'{player} You rolled a {roll}')
  print(f'{player} You have rolled a total of {dice_sum}')
if __name__== "__main__":
  main()
        