#Leetcode Problem 11 Container with the most water is a classic array, two pointer and greedy based problem 


'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104



'''


#Approach to the problem
# The core part for the solution or the heart of the solution is this mathematical equation:
# area = (j-1) * min(height[i], height[j])

#Algorithm
# step 1: we will take two pointers i and j initilize them i = 0, j = len(height)-1 and max_area = 0
# step 2: then we will use a while loop with the condition i < j the loop will run for this condition
# step 3: then we will use the formula stated above and calculate the area 
# step 5: then we will store the value of area calcuated by the formula  
# step 6: then we will find the maximum area using function max(max_area, area)
# step 7: then we will give condition to move the pointer as if height[i] < height[j]   make i +=1 else make j -=1
# step 8: now we are done return the max_area


#code


def max_water(height):
    i = 0
    j = len(height)-1
    max_area= 0
    while i<j:
         area= (j-i) * min(height[i], height[j])
         max_area = max(max_area, area)
         if height[i] < height[j]:
              i +=1
         else:
             j -=1
    return max_area


#Calling the function

height = list(map(int,input("Enter the values: ").split()))
result = max_water(height)
print("The max_water is :", result)
