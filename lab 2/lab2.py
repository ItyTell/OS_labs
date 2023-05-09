import threading
import time
import random



def f1(sleeping_time, return_val, result, index, endable=True):
    time.sleep(sleeping_time)
    while not endable:
        time.sleep(sleeping_time)
    
    time.sleep(random.random() / 10)
    print(f"thred number {index} completed the work")
    result.append(return_val)
    


def main():
    
    result = []
    p1 = threading.Thread(target=f1,args=[4, 0, result, 0, True], daemon=True)
    p2 = threading.Thread(target=f1,args=[15, 1, result, 1, False], daemon=True)


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



