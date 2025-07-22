import threading
import time


def calc_square(num):
    print("Calculate square number")
    for n in num:
        time.sleep(0.5)
        print("square: ",n*n)

def calc_cube(num):
    print("Calculate cube number")
    for n in num:
        time.sleep(0.5)
        print("cube: ", n * n)

num = [2,3,8,9]
start = time.time()

t1 = threading.Thread(target=calc_square, args=(num,))
t2 = threading.Thread(target=calc_cube, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in :", time.time() - start)
print("all work done")