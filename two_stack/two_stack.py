# Author: Santigie Sankoh


def read_user_input():
    sub = input().strip().split(' ')
    us_inp = int(sub[0])
    
    if len(sub) == 1:
        return (us_inp, None)
    try:
        arg = int(sub[1])
    except ValueError:
        arg = sub[1]
        
    return us_inp, arg

class Stack:
    def __init__(self):
        self.ll = []
        
    def push(self, data):
        self.ll.append(data)
        
    def pop(self):
        return self.ll.pop()
    
    def __len__(self):
        return len(self.ll)
    
    def top(self):
        if self.ll:
            return self.ll[-1]
        return None

class Queue:
    def __init__(self):
        self.qhead = Stack()
        self.qtail = Stack()
    
    def enqueue(self, data):
        self.qtail.push(data)
    
    def dequeue(self):
        if self.qhead:
            return self.qhead.pop()
            
        return self.tail_head().pop()
    
    def peek(self):
        if self.qhead:        
            return self.qhead.top()
            
        return self.tail_head().top()
    
    def tail_head(self):
        while self.qtail:
            self.qhead.push(self.qtail.pop())          
            
        return self.qhead

    
def main():
    
    q = Queue()

    n_commands = int(input().strip())
    for _ in range(n_commands):
        command, arg = read_user_input()
        if command == Enqueue:
            q.enqueue(arg)
        elif command == Dequeue:
            q.dequeue()
        elif command == PRINT:
            print(q.peek())
            
            
  #initiating global variables      
Enqueue = 1
Dequeue = 2
PRINT = 3
if __name__ == '__main__':
    main()
