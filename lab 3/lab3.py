import threading
import time
import random

class Memory:

    def __init__(self, X):
        self.list = X
        self.mutex = [1] * len(X)
    
    def take_cell(self, index):
        time.sleep(random.random()/10)
        while not self.mutex[index]:
            time.sleep(random.random())
        self.mutex[index] = 0
        return self.list[index]
        
    def put_cell(self, index, val):
        if self.mutex[index]:
            self.take_cell(index)
        self.list[index] = val
        self.mutex[index] = 1
    
    def write_val(self, val):
        for index, mut in enumerate(self.mutex):
            if mut:
                self.mutex[index] = 0
                self.list[index] = val
                break
        return index


def f(sleeping_time, index, endable=True):
    time.sleep(sleeping_time)
    while not endable:
        time.sleep(sleeping_time)
    
    
def f1(sleeping_time, return_val, index, X, endable=True):
    f(sleeping_time, index, endable)
    print(f"thred number {index} completed the work")
    #result.append(return_val)


N = 10 # memory len
X = [random.randint(1, 10) for i in range(N)] 
mem = Memory(X)
index = mem.write_val(10.5)
print(index, mem.list)

def main():
    result = []
    p1 = threading.Thread(target=f1,args=[2, 0, result, 0, X, True], daemon=True)
    p2 = threading.Thread(target=f1,args=[20, 1, result, 1, X, True], daemon=True)


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


#print(main())

