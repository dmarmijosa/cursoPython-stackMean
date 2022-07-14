import _thread
import time

def horaActual(nombreDeThread,tiempoEspera):
   i=0
   while i<5:
    time.sleep(tiempoEspera)
    i+=1
    print(f"hilo: {nombreDeThread}- {time.ctime(time.time())}")

   

_thread.start_new_thread(horaActual,("thread_1",1))
_thread.start_new_thread(horaActual,("thread_2",2))

while True:
    time.sleep(0.1)