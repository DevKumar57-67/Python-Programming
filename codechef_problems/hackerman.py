'''
Hackerman
Hackerman wants to know who is the better player between Bob and Alice with the help of a game.

The game proceeds as follows:

First, Alice throws a die and gets the number 
A
A
Then, Bob throws a die and gets the number 
B
B
Alice wins the game if the sum on the dice is a prime number; and Bob wins otherwise.
Given 
A
A and 
B
B, determine who wins the game.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
The first and only line of each test case contains two space-separated integers 
A
A and 
B
B.
Output Format
For each test case, output on a new line the winner of the game: Alice or Bob.

Each letter of the output may be printed in either uppercase or lowercase, i.e, Alice, ALICE, AlIce and aLIcE will all be considered equivalent.

'''


#This is a classic prime number problem with some constraints and also mixed up as a game theory problem 
# algorithm: simple solution is to make the prime number checking approach 
# if n <= 2 || No 
# if n % i == 0  yes
# else no 


#Code

def prime(n):
    if n < 2:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False
    return True


#Calling the function



a,b = map(int,input("Enter the value:").split())
total = a+b
result = prime(total)
print(result)
