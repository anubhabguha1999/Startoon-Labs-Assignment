
# Let Ankur has given a large weight W, and a list of smaller weights in an array. He needs to write a code in order to find "can we form weight W or not, using smaller weights". He only knows dp solution. Could you write a code solution for him without using dp.
# Constraint: - list size <= 12

# Sample Input1: - W = 15
# list = {4, 3, 5, 6, 4}
# Output: - True
# Explanation: - 15 =4 + 5 + 6.

# Sample Input2: - W = 9
# list = {4, 1, 3, 7}
# Output: - False.
# Explanation: - There is no way to sum up 7.


# as it was asked in the code that i cannot use Dynamic programming then my approach will be to use Recursion in this case.


def canWeFormWeight(finalWeight, weightsList, pointer=0, presentSum=0):
    # if the PRESENT SUM gets equal to the FINAL WEIGHT then return "True" immediately
    if presentSum == finalWeight:
        return True
    # if the POINTER is at the end of the WEIGHTS LIST then return "False" because it should not perfom more operations
    if pointer == len(weightsList):
        return False

    # if the sum of the PRESENT SUM and the POINTER is less than or equals to the FINAL WEIGHT, then 
    if presentSum + weightsList[pointer] <= finalWeight:
        # if the recursive call returns True, it means that the target weight can be formed by including the current weight in the sum. In this case, the function returns True
        if canWeFormWeight(finalWeight, weightsList, pointer + 1, presentSum + weightsList[pointer]):
            return True

    # Here I have implemented the recurssion where it returns the value of the WEIGHTS LIST, FINAL WEIGHT, POINTER (increased by 1) and the PRESENT SUM
    return canWeFormWeight(finalWeight, weightsList, pointer + 1, presentSum)


# Sample Input 1 as given in the example
finalWeight1 = 15
weightsList1 = [4, 3, 5, 6, 4]
print(canWeFormWeight(finalWeight1, weightsList1))
# Output: True
# Because in the following list 4 + 5 + 6 = 15


# Sample Input 2 given by me:
finalWeight2 = 10
weightsList2 = [0, 1, 3, 3]
print(canWeFormWeight(finalWeight2, weightsList2))
# Output : False
# Because in the following list there is no combination of arrays that can form the sum of 10


# Sample Input 2 as given in the Example
finalWeight2 = 9
weightsList2 = [4, 1, 3, 7]
print(canWeFormWeight(finalWeight2, weightsList2))
# Output: False
# Because in the following list there is no combination of arrays that can form the sum of 9


# Sample Input 4 given by me:
finalWeight4 = 10
weightsList4 = [4, 1, 3, 7]
print(canWeFormWeight(finalWeight4, weightsList4))
# Output : True
# Because in the following list 7 + 3 = 10



