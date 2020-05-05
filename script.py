import os
import threading
import random
import time
import multiprocessing
import signal



def thread_function(port):
    os.chdir(r"C:\Users\marco\IdeaProjects\demo")
    print(os.getcwd())
    cmd = "mvn spring-boot:run -Dspring-boot.run.arguments=--server.port="+port
    os.system(cmd)


if __name__ == "__main__":
    list_threads = []

    # starting with 10 thread which all start spring boot instances at a random port
    for p in range(10):
        num1 = random.randint(8080, 10000)
        x = multiprocessing.Process(target=thread_function, args=(str(num1),))
        x.start()
        list_threads.append(x)

    #loop which starts and terminates 1 random spring boot instance
    while 1:
        # Generating a Thread which starts a spring boot instances at random port
        num1 = random.randint(8080, 10000)
        #x = threading.Thread(target=thread_function, args=(str(num1),))
        x = multiprocessing.Process(target=thread_function, args=(str(num1),))
        x.start()
        #append is threadsafe
        list_threads.append(x)


        #Random Sleep Until a random thread is killed and another thread is started again
        numsleep = random.randint(15, 60)
        time.sleep(numsleep)
        threadtokill = random.choice(list_threads)
        print(threadtokill)
        threadtokill.terminate()
        time.sleep(numsleep)
















