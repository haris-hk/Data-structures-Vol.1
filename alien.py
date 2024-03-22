import list_adt as listadt

def create_alien():
    """
    Creates an 'alien' dictionary with a list to store messages.
    You can add other attributes if required

    Returns:
    A dictionary representing an 'alien' with a list to store messages:
    {
        'messages': listadt.create_list(100)    # List to store messages with a maximum capacity of 100
    }
    """
    messages = listadt.create_list(100)
    messages["max_seq"] = 1000
    messages["min_seq"] = -1
    messages['last_str_rear'] = None 
    return messages
    # provide other required implementation here
    

def add(seq: int, msg: str, alienList: dict):
    """
    Parameters:
    - seq: The sequence number of the message.
    - msg: The message to be added.
    - alienList: The 'alien' dictionary containing the messages list.
    """
    if listadt.is_full(alienList) == False:
        if listadt.is_empty(alienList) == True:
            listadt.add((alienList['size'])//2, msg, alienList)
            alienList['max_seq'] = seq
            alienList['min_seq'] = seq
            alienList['last_str_rear'] = True 
            alienList['i'] = (alienList['size'])//2
        else:
            if seq < alienList['min_seq']:
                listadt.insert_first(msg, alienList)
                alienList['last_str_rear'] = False
                alienList['min_seq'] = seq
            elif seq > alienList['max_seq']:
                listadt.insert_last(msg, alienList)
                alienList['max_seq'] = seq
                alienList['last_str_rear'] = True
    return alienList


    # provide implementation here
    

def delete(seq: int, msg: str, alienList: dict):
    """

    Parameters:
    - seq: The sequence number of the message to be deleted.
    - msg: The message to be deleted.
    - alienList: The 'alien' dictionary containing the messages list.
    """
    
    # provide implementation here
    if seq == -1:
        if listadt.is_empty(alienList) == False:
            if alienList['last_str_rear'] == True:
                listadt.remove_last(alienList)
                #alienList['max_seq'] = alienList['data'][(alienList['i'] + alienList['n']) % alienList['size']][0]
            #print(isdigit(alienList['data'][(alienList['i'] + alienList['n']) % alienList['size']][0]))
            if alienList['last_str_rear'] == False:
                #alienList['min_seq'] = alienList['data'][(alienList['i'] + 1)% alienList['size']][0]
                listadt.remove_first(alienList)
    return alienList

def get_messages(alienList: dict) -> list[str]:
    """
    
    Parameters:
    - alienList: The 'alien' dictionary containing the messages list.

    Returns:
    A list of all messages in the conversation.
    """
    lst = ["" for i in range(alienList['n'])]
    index = 0
    i = alienList['i']
    while i != ((alienList['i'] + alienList['n']) % alienList['size']):
        lst[index] = (listadt.get(i, alienList))
        i = (i+1) % alienList['size']
        index += 1
    return lst

    
    # provide implementation here
    


def main(filename) -> list[str]:
    """
    Reads data from a file, processes it, and returns the conversation as a list.

    Data is provided in the following format:
    There can be multiple lines in the file, each line containing an integer and an optional string separated by a space. The integer represents the sequence number of the message, and the string represents the message itself. If the string is not provided, it is assumed to be an empty string. The sequence number 0 indicates the end of the conversation.

    Process the data as follows:
    - If the sequence number is 0, stop processing the file.
    - If the sequence number is positive, add the message to the conversation.
    - If the sequence number is negative, delete the message from the conversation.
    
    Parameters:
    - filename: The name of the file to read data from.

    Returns:
    A list representing the conversation obtained from the file.
    """
    messages = create_alien()
    with open (filename) as f:
        lines = f. readlines ()
    input = []
    
    for line in lines :
        line = line . strip () # remove leading and trailing spaces
        tokens = line . split () # split the line into tokens
        
        input . append ( tokens) # add the first token to the input list
    # main ( input ) # call the main function
    for i in range (0, len (input)):
        #print(input) 
        if int(input[i][0]) > 0:
            # print(1)
            if int(input[i][0]) < int(messages['max_seq']) or int(input[i][0]) > int(messages['min_seq']):
                add(int(input[i][0]), input[i][1], messages)
        elif int(input[i][0]) == -1:
            #print(input[i])
            delete(int(input[i][0]),input[i][0],messages)
        elif int(input[i][0]) == 0:
            out = get_messages(messages)
            output = ""
            for i in range (len(out)):
                output += out[i] + " "
            return(output[:-1])
        
    

    # Provide your implementation here

    

(main("Inputs/alien01.txt"))
(main("Inputs/alien02.txt"))