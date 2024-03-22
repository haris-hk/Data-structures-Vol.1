import math 
def initialize_matrix(n: int) -> list[list[int]]:
    """
    A  function that takes an integer n as an argument and returns a 2D array of size n x n with each cell containing None values.
    """
    return [[None for i in range(n)]for i in range(n)]


def length(arr: list[int]) -> int:
    """
    A function that takes a single-dimensional array, arr, as an argument and returns the count of valid data items in it, i.e., the non-None values.
    """
    number = 0
    for element in arr:
        if element is not None:
            number += 1
    return number


def get_maximum(arr: list[int]) -> int:
    """
    A function that takes an array as an argument, and WITHOUT using the built-in functions, returns the maximum value of the array.
    """
    max = -1
    for count in range (length(arr) ):
        if arr > max:
            max = arr[count]
    return max



def insertion_sort(arr: list[int]) -> None:
    """
    A void function that takes a single-dimensional array arr as an argument and applies insertion sort on the valid data items in the array, i.e., the non-None values. This is an in-place function, meaning the original array that was passed as a reference will be updated with the sorted values.
     
    The function should not return anything.
    """
    for i in range(1, length(arr)):
        val = arr[i]
        index = i - 1
        while index >= 0 and arr[index] > val:
            arr[index + 1] = arr[index]
            index -= 1
        arr[index + 1] = val



def partition_and_prevail(arr: list[list[int]]) -> None:
    """
    A void function that takes the array to be sorted as an argument
    and applies the “Partition and Prevail” algorithm to sort the valid
    data items in the array, as explained in the assignment.

    The function should not return anything.
    """
    lnth = length(arr)
    if lnth == 0:
        return 
    matrix = initialize_matrix(lnth)
    
    
    for i in range(lnth):
        x = arr[i] // math.ceil((get_maximum(arr) + 1) / lnth)
        for j in range(lnth):
            if matrix[x][j] is None:
                matrix[x][j] = arr[i]
                break

    for x in matrix:
        insertion_sort(x)
    i = 0
    for x in matrix:
        for item in x:
            if item is not None:
                arr[i] = item
                i += 1
    return arr



def main(filename) -> list[list[int]]:
    """
    - Take input from the given filename one line at a time
    - Apply partition_and_prevail sorting algorithm to get the sorted arrays and returns the output as a two dimensional array.
    """
    with open(filename) as f:
        lines = f.readlines()
    nlst = []
    for line in lines:
        line = line.strip().replace('[', '').replace(']', '').replace(',', '')
        tokens = line.split()
        for i in range(length(tokens)):
            if tokens[i] != "None":
                tokens[i] = int(tokens[i])
            else:
                tokens[i] = None
        nlst.extend(tokens)
    partition_and_prevail(nlst)
    return [ans if ans is not None else None for ans in nlst]
