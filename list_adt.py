def create_list(size):
    """
    Creates a deque-like data structure with a fixed-size list.

    Parameters:
    - size: The fixed size of the deque.

    Returns:
    A dictionary representing the deque:
    {
        'size': size,    # Fixed size of the deque
        'data': [None] * size,    # List to store elements
        'n': 0,    # Number of elements in the deque
        'i': 0    # Index for circular storage of elements
    }
    """
    return {'size': size, 'data': [None]* size, 'n': 0, 'i': 0}

def is_empty(listADT):
    """
    Checks if the deque is empty.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is empty, False otherwise.
    """
    # for count in range(len(listADT)):
    #     if listADT[count] is not None:
    #         return False
    return listADT['n'] == 0

def is_full(listADT):
    """
    Checks if the deque is full.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is full, False otherwise.
    """
    return listADT['n'] == listADT['size']

def get(i, listADT):
    """
    Gets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to retrieve.
    - listADT: The deque data structure.

    Returns:
    The element at the specified index.
    """
    return listADT['data'][i]

def set(i, e, listADT):
    """
    Sets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to set.
    - e: The element to be set.
    - listADT: The deque data structure.
    """
    
    listADT['data'][i] = e
    return listADT

def length(listADT):
    """
    Gets the number of elements in the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The number of elements in the deque.
    """
    number = 0
    for element in listADT['data']:
        if element is not None:
            number += 1
    return number


def add(i, e, listADT):
    """
    Adds an element at the specified index in the deque.

    Parameters:
    - i: The index at which to add the element.
    - e: The element to be added.
    - listADT: The deque data structure.
    """
    if i < 0 or i > listADT['size']:
        raise IndexError("Index out of range")

    if listADT['n'] == listADT['size']:
        raise ValueError("Deque is full")

    if i < listADT['n'] // 2:
        for j in range(i):
            listADT['data'][(listADT['i'] + j) % listADT['size']] = listADT['data'][(listADT['i'] + j - 1) % listADT['size']]
        listADT['data'][(listADT['i'] + i) % listADT['size']] = e
        listADT['i'] = (listADT['i'] - 1) % listADT['size']
    else:
        for j in range(listADT['n'], i, -1):
            listADT['data'][(listADT['i'] + j) % listADT['size']] = listADT['data'][(listADT['i'] + j - 1) % listADT['size']]
        listADT['data'][(listADT['i'] + i) % listADT['size']] = e

    listADT['n']+=1

def remove(i, listADT):
    """
    Removes the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to remove.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        return "List is full"
    for j in range(len(listADT['data']), i, -1):
        listADT['data'][j] = listADT['data'][j - 1]

def insert_last(e, listADT):
    """
    Inserts an element at the last position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    if is_full(listADT) == False:
        
        listADT['data'][(listADT['i'] + listADT['n']) % listADT['size']] = e
        listADT['n'] = listADT['n'] + 1
    return listADT

def remove_last(listADT):
    """
    Removes the last element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    listADT['n'] -= 1
    listADT['data'][(listADT['i'] + listADT['n']) % listADT['size']] = None
    return listADT

def insert_first(e, listADT):
    """
    Inserts an element at the first position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    listADT['data'][(listADT['i']-1) % listADT['size']] = e
    listADT['i'] = (listADT['i']-1) % listADT['size']
    listADT['n'] += 1
    return listADT

def remove_first(listADT):
    """
    Removes the first element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    listADT['data'][(listADT['i']-1) % listADT['size']] = None
    listADT['i'] = (listADT['i']+1) % listADT['size']
    listADT['n'] += 1
    return listADT

def get_first(listADT):
    """
    Gets the first element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The first element in the deque.
    """
    return listADT['data'][listADT['i']] 
    

def get_last(listADT):
    """
    Gets the last element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The last element in the deque.
    """
    return listADT['data'][(listADT['i'] + (length(listADT)-1)) % listADT['size']]
