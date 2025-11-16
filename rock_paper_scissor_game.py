
# rules

# rock =1
# paper =0
# scissor =-1

# Rock beats Scissors: Rock crushes scissors.
# Scissors beats Paper: Scissors cuts paper.
# Paper beats Rock: Paper covers rock.
# If both players choose the same shape, the game is a tie and is usually replayed until there is a winner. 

import random
print("Lets Play a Rock-Paper-scissor" )

your_choice=  (input("Enter your choice : "))


your_dict ={
    "scissor" :-1,
    "rock": 1,
    "paper": 0,
}
if your_choice  not in your_dict:
   print("Invalid choice! Please choose only rock, paper, or scissor.")
user_choice = your_dict[your_choice]



reverse_dict={
    -1: "scissor" ,
    1:"rock",
    0: "paper",
}



computer_choice = random.choice([1,-1,0])

print(f"YOur choice : {your_choice}\ncomputer choice : {reverse_dict[computer_choice]}")



if(user_choice==computer_choice):
    print("The match is tie!")
else:
    if(user_choice==1 and computer_choice==0):
        print("you lose ")
        
    elif(user_choice==1 and computer_choice==-1):
          print("you win ")
          
    elif(user_choice==0 and computer_choice==1):
      print("you lose ")

    elif(user_choice==0 and computer_choice==-1):
      print("you win ")
      
    elif(user_choice==-1 and computer_choice==0):
      print("you win ")
      
    elif(user_choice==-1 and computer_choice==1):
      print("you lose ")
     
    else:
       print("U are done some mistake")





    

