import math
def init_matrix(rows: int, cols: int) -> list[list[int]]:
    """
    Creates a 2D array (matrix) based on the input rows and columns.

    Parameter(s):
    - rows (int): Specifies the rows of the 2D array to be created.
    - cols (int): Specifies the columns of the 2D array to be created.

    Returns:
    - 2D array (int): This is the 2D array that is created using the input rows and cols.
    """
    return [[None for _ in range(cols)] for _ in range(rows)]

def column_major(i: int, j: int, lst: list[int], size=None) -> any:
    size = size or int(math.sqrt(len(lst) ))
    return lst[i + j * size]

def filter_image(image: list[list[int]], kernel: list[int]) -> list[list[int]]:
    val  =  int(math.sqrt(len(kernel) )//2)
    
    """
    Perform the convolution operation by applying the kernel over the input image.

    Parameter(s):
    - 2D array (int): This is the image on which you have to apply the kernel/filter and perform convolution. 
    - 1D array (int): The first entry in this array is the width of the kernel and the remaining entries are the values of the kernel.

    Returns:
    - 2D array (int): This is the matrix that is obtained after performing convolution.
    """
    lst = init_matrix(len(image), len(image[0]))
    for i in range(len(image)):
        for j in range(len(image[0])):
            sum = 0
            for a in range(-val, val+1):
                for b in range(-val, val+1):
                    if i+a <= -1 or i+a >= len(image) or j+b <= -1 or j+b >=len(image[0]):
                        continue
                    sum += image[i+a][j+b] * column_major(val+a, val+b, kernel)
            lst[i][j] = sum

    return lst

    # for i in range(len(image)):
    #     for j in range(len(image[0])):
    #         sum = 0
    #         for count in range(3):
    #             for a in range(-1,2):
    #                 for b in range(0,len(kernel),3):
                        
    #                         try:
    #                             pixel = image[i+count][j+a]
    #                             print(pixel)
    #                             sum += pixel*kernel[b+count]
    #                             print(sum)
    #                         except IndexError:
    #                             break       
        
    #         lst[i][j] = sum
    # print(lst)
    # will try to complete later

def main(file_name: str) -> list[list[int]]:
    """
    The main driver function that will run the entire program. 
    It should extract the image and the kernel from the file and pass them to filter_image(...).

    Parameter(s):
    - file_name (.txt file): Path to a text file that contains the image (2D array) and the kernel (1D array).

    Returns:
    - 2D array (int): This is the matrix that is obtained after executing filter_image(...)
    """
    with open(file_name) as f:
        image = [[int(ans) for ans in f.readline().strip().split()] for _ in range(int(f.readline().strip().split()[0]))]
        kernel = [int(ans) for ans in f.readline().strip().split()[1:]]

    

    # Initialize the variables, image and kernel.
    
    # Pass those variables to filter_image(...)
    return filter_image(image, kernel)
   
#filter_image([[10 ,10, 10, 10, 10],[20, 20 ,20 ,20 ,20],[80, 80, 80, 80 ,80],[60, 60 ,60 ,60 ,60],[70, 70 ,70 ,70, 70]], [3, 4 ,5 ,2 ,3, 4, 1 ,2 ,3])

    
