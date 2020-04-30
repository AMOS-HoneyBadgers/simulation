import os
import logging
import threading
import random

def thread_function(port):
    logging.info("Thread %s: starting", port)
    os.chdir(r"C:\Users\marco\IdeaProjects\demo")
    print(os.getcwd())
    cmd = "mvn spring-boot:run -Dspring-boot.run.arguments=--server.port="+port
    os.system(cmd)
    logging.info("Thread %s: finishing", port)


while 1:
    num1 = random.randint(8080, 10000)
    x = threading.Thread(target=thread_function, args=(str(8080 + p),))
    x.start()


for p in range(10):
    x = threading.Thread(target=thread_function, args=(str(8080+p),))
    x.start()







