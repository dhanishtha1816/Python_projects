print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. Follow through the story by making different choices to see if you find the treasure, or lose it!")
ready= input('Ready? Y/N\n')
if ready.lower()== 'y':
  lorr=input('''You're at a crossroad. Where do you want to go? Type "left" or "right" or "straight"\n''')
  if lorr.lower()=='left':
    lake= input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if lake.lower()=='wait':
      doors=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
      if doors.lower()=='yellow':
        print('A true treasurer! YOU WIN!')
      elif doors.lower()=='blue':
        print('Ohh oh, you are burnt- rare medium.')
      elif doors.lower()=='red':
        print('Unlucky you, but lucky is the red faced beast- it surely had a great lunch today!')
    else:
      print('You didnt win the treasure, but surely fed a really hungry crocodile. Game over.')
  elif lorr.lower()=='right':
    print('You fell off the cliff. Game over.')
  elif lorr.lower()=='straight':
    forest= input('You reach a dark scary forest. where you see a wolf trapped in a snare. help him? Y/N\n')
    if forest.lower()== 'y' :
        paths = input('Good!, A kind human has the tendency to win. Next, you see 2 paths. Which one will you choose? "Left" or "Right"\n')
        if paths.lower()=='left':
            lake= input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
            if lake.lower()=='wait':
                doors=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
                if doors.lower()=='yellow':
                     print('A true treasurer! YOU WIN!')
                elif doors.lower()=='blue':
                     print('Ohh oh, you are burnt- rare medium.')
                elif doors.lower()=='red':
                     print('Unlucky you, but lucky is the red faced beast- it surely had a great lunch today!')
            else:
                print('You didnt win the treasure, but surely fed a really hungry crocodile. Game over.')
        else:
            enter=input('''You encounter a giant monster! You find an axe and try to fight him. The wolf you saved helps you, and you barely win.
You see a small hut and a well full of water a few steps away. "Enter hut" or "drink water"?\n ''')
            if enter.lower()== 'enter hut':
              woman= input('''You go inside the hut and find a woman with 2 boxes. She asks you to chose one of the 2 boxes. One of them has the key to the treasure.
              "Box1" or "Box2"?\n''')
              if woman.lower()=='box1':
                print('Congrats you win the treasure!')
              else:
                print('You win a broken skull and a broken life.')
            elif enter.lower()== 'drink water' or enter.lower()=='well':
                print('The water was poisonous. You died.')
    else:
         paths = input('Next, you see 2 paths. Which one will you choose? "Left" or "Right"\n')
         if paths.lower()=='left':
               lake= input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
               if lake.lower()=='wait':
                doors=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
                if doors.lower() == 'yellow':
                     print('A true treasurer! YOU WIN!')
                elif doors.lower()=='blue':
                     print('Ohh oh, you are burnt- rare medium.')
                elif doors.lower()=='red':
                     print('Unlucky you, but lucky is the red faced beast- it surely had a great lunch today!')
               else:
                    print('You didnt win the treasure, but surely fed a really hungry crocodile. Game over.')
         else:
           box=input('''You encounter a giant monster! You find an axe and try to fight him. The wolf you left in the forest could have helped you, but now you are dead. Game over''')
else:
  print('Coward. Game over.')
