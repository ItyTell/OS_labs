import threading
import time
import random

class Memory:

    def __init__(self, X):
        self.list = X
        self.mutex = [1]
    
    def take_cell(self):
        time.sleep(random.random()/10)
        while not self.mutex[0]:
            time.sleep(random.random())
        self.mutex[0] = 0
        return self.list[0]
        
    def put_cell(self, value):
        self.list[0] = value
        self.mutex[0] = 1
    

    
def f1(mem, result):
    x = mem.take_cell()
    for i in range(100):
        x += 1
    result.append(x)
    mem.put_cell(x)

def f2(mem, result):
    x = mem.take_cell()
    for i in range(100):
        x += 1
    result.append(x)
    mem.put_cell(x)

X = [0] 
mem = Memory(X)

def main():
    result = []
    p1 = threading.Thread(target=f1,args=[mem, result], daemon=True)
    p2 = threading.Thread(target=f2,args=[mem, result], daemon=True)


    p1.start()
    p2.start()

    time1 = time.time()
    while p1.is_alive() * p2.is_alive():
        if time.time() - time1 > 10:
            ask = input("Continue culculating? y/n \n")
            if ask == "n":
                return "Cululation was not completed" 
            time1 = time.time()

    if p1.is_alive():
        p1, p2 = p2, p1

    if not result[0]:
        return f"The answer is {result[0]}"
    else:
        time1 = time.time()
        while p2.is_alive():
            if time.time() - time1 > 10:
                ask = input("Continue culculating? y/n \n")
                if ask == "n":
                    return "Cululation was not completed" 
                time1 = time.time()
        return f"The answer is {result[0] * result[1]}"


print(main())

