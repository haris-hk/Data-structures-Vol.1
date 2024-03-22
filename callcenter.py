# DO NOT CHANGE THIS FUNCTION
# Create a basic queue
def create_queue(size: int) -> dict:
    """
    Description: Creates and initializes a basic queue with a specified size.
    Parameters: size - an integer representing the size of the queue.
    Return: A dictionary representing the initialized queue.
    """
    return {
        'data': [None] * size,  # list of elements
        'front': -1,  # index of the first element in the queue
        'rear': -1,  # index of the last element in the queue
        'n': 0,  # number of elements in the queue
        'size': size  # size of the queue
    }

# DO NOT CHANGE THIS FUNCTION
# Create a priority queue
def create_priority_queue(size: int) -> dict:
    """
    Description: Creates and initializes a priority queue with a specified size.
                 Each element in the queue is a tuple consisting of data and priority.
    Parameters: size - an integer representing the size of the priority queue.
    Return: A dictionary representing the initialized priority queue.
    """
    return {
        'data': [(None, float('inf'))] * size,  # list of elements with default priority set to infinity
        'front': -1,  # index of the first element in the queue
        'rear': -1,  # index of the last element in the queue
        'n': 0,  # number of elements in the queue
        'size': size  # size of the queue
    }

# Check if the queue is full
def is_full(queue: dict) -> bool:
    """
    Description: Checks if the given queue is full (reached its maximum capacity).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is full, False otherwise.
    """
    return queue['n'] == queue['size']

# Check if the queue is empty
def is_empty(queue: dict) -> bool:
    """
    Description: Checks if the given queue is empty (contains no elements).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is empty, False otherwise.
    """
    return queue['n'] == 0

# Add an element to the rear of the queue
def enqueue(queue: dict, item):
    """
    Description: Adds an element with the value 'val' to the rear of the queue.
    Parameters: queue - a dictionary representing the queue, val - the value to be added to the queue.
    """
    if  is_full(queue['data']) == True:
        return "Queue is full"
    
    elif is_empty(queue['data']) == True:
        queue['data'][0] = item
        queue['rear'] += 1
        queue['front'] += 1
        queue['n'] += 1
    else:
        queue['rear'] = (queue['rear']+1) % queue['size']
        queue['data'][queue['rear']] = item
        queue['n'] += 1

    return queue
        


# Remove and return the element from the front of the queue
def dequeue(queue: dict) :
    """
    Description: Removes and returns the element from the front of the queue.
    Parameters: queue - a dictionary representing the queue.
    Return: The element from the front of the queue.
    """
    if is_empty(queue['data']):
        return "queue is empty"
    else : 
        removed = queue['data'][queue['front']] 
        queue['front'] = (queue['front'] + 1) % queue['size']
        queue['n'] -= 1
    return removed

# Return the element at the front of the queue without removing it
def peek(queue: dict):
    """
    Description: Returns the element at the front of the queue without removing it.
    Parameters: queue - a dictionary representing the queue.
    Return: The element at the front of the queue.
    """
    return queue['data']['front']
    

# Add an element with priority to the priority queue
def enqueue_priority(priority_queue: dict, item, priority: int):
    """
    Description: Adds an element with the value 'val' and the specified priority to the priority queue.
    Parameters: queue - a dictionary representing the priority queue, val - the value to be added to the queue,
                priority - the priority of the element.
    """
    if  is_full(priority_queue['data']) == True:
        return "Queue is full"
    
    else:
        
        if priority_queue['rear']==-1 and priority_queue['front' ] ==-1:
            priority_queue[ 'rear'] =0
            priority_queue['front' ]=0
            priority_queue[ 'data' ][priority_queue['rear' ]]= (item, priority)
            priority_queue['n' ]+=1
            return priority_queue

        else:
            priority_queue['rear']=(priority_queue[ 'rear']+1)%priority_queue['size']
            priority_queue ['data'] [priority_queue['rear']]=(item,priority)
            priority_queue ['n']+=1 
            return priority_queue


# Remove and return the element with the minimum priority from the priority queue
def dequeue_min_priority(priority_queue: dict):
    """
    Description: Removes and returns the element with the minimum priority from the priority queue.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    min_pr = priority_queue['data'][0][1]
    nameofitem = priority_queue['data'][0][0]
    index = 0
    for i in range(1, priority_queue['n']):
        priority = priority_queue['data'][i][1]

        if  priority < min_pr:

            min_pr = priority
            nameofitem = priority_queue['data'][i][0]
            index = i
    
    for i in range(index, priority_queue['n']-1):

        priority_queue['data'][i]=priority_queue['data'][i+1]
    
    priority_queue['n'] -= 1
    priority_queue['rear']=(priority_queue['rear']-1)%priority_queue["n"]
    priority_queue['data'][priority_queue['n']]=(None, float('inf'))
    return (nameofitem, min_pr)

# Return the element with the minimum priority from the priority queue without removing it
def peek_min_priority(priority_queue: dict):
    """
    Description: Returns the element with the minimum priority from the priority queue without removing it.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    min_pr= priority_queue['data'][0][1]
    nameofitem = priority_queue['data'][0][0]

    for i in range(priority_queue['n']):
        priority = priority_queue['data'][i][1]
        if priority < min_pr:
            min_pr = priority
            nameofitem = priority_queue['data'][i][0]

    return (nameofitem, min_pr)


def CallSimulator(callQueue, agentQueue) -> dict:
    """
    Description: Simulates a call center scenario where calls are processed by agents based on their availability.
    Type: Function
    Parameters: callQueue - a dictionary representing the call queue,
                AgentQueue - a dictionary representing the agent queue.
    Return: A queue containing information about each processed call (callerName, call_start, call_end, wait_time).
    """
    # Simulation parameters
    Simulation = True
    ct = 0
    wt = 0

    # Create a queue to store the call log
    callLog = create_queue(callQueue['size'])

    while Simulation:
        # end simulation if call queue is empty
        if is_empty(callQueue):
            Simulation = False
        
        elif peek(callQueue)[0] > ct:          
            ct += 1

        else:
            agentpriority = peek_min_priority(agentQueue)[1]
            if agentpriority > ct:
                wt += 1
                ct += 1
            
            else:
                call = dequeue(callQueue)
                agent = dequeue_min_priority(agentQueue)
                enqueue_priority(agentQueue, agent, call[0] + call[2] + agentpriority)

                if call[0] == ct:
                    enqueue(callLog, (call[1], call[0], call[0] + call[2], 0))
                else:
                    enqueue(callLog, (call[1], ct, ct + call[2], wt))
                
    

    # Returning the queue containing the call log
    return callLog



def main(filename) -> list:
    """
    Description: Main function to read input data from a file, initialize agent and call queues, simulate call processing using CallSimulator, and return the call log data.
    Parameters: filename - the name of the file containing input data.
    Return: A list representing the call log data.
    """
    
    # Read input data from the file
    # First line contains the list of agents separated by spaces 
    # Second line contains the number of calls to be processed
    # Populate the call queue with call details from the remaining lines contain the call details (start time, caller name, call duration) separated by spaces

    # provide your implementation here 
   
    with open (filename, 'r') as file:
        lines = file.readlines()
    agents = lines [0]. strip().split()
    call_queue = create_queue (len (lines) -2)
    for i in range(2, len(lines)):
        line = lines [i]. strip().split()
        in_time = int (line[0])
        name = line [1]
        duration = int(line [2])
    enqueue (call_queue, (in_time, name, duration))
    agentQueue = create_priority_queue (len(agents) )
    for x in agents:
            enqueue_priority (agentQueue,x,0)
    
    # Simulate call processing using CallSimulato
    call_log = CallSimulator(call_queue, agentQueue)

    # Return the call log data as a list
    return call_log['data']




