import threading
import time

class TenedorFilosofo(threading.Thread):
    def __init__(self, tenedores, filosofosNum):
        threading.Thread.__init__(self)
        self.tenedores = tenedores
        self.filosofosNum = filosofosNum
        self.datoTemporal =  self.filosofosNum  % 5
   
    def hilosFilosofos(self):
        while True:
            try:
                print(f'Filosofo iniciando {self.filosofosNum}  dato: {self.datoTemporal}')
                time.sleep(2)
                print("Filosofo ", self.filosofosNum, "pasando tenedor del lado izquierdo")
                self.tenedores[self.filosofosNum].acquire()
                time.sleep(2)
                self.tenedores[self.filosofosNum].release()
                print("Filosofo ", self.filosofosNum, "recoge tenedor del lado derecho")
                self.tenedores[self.datoTemporal].acquire()
                time.sleep(2)
                print(f'Filosofo {self.filosofosNum} está comiendo ...')
                self.tenedores[self.datoTemporal].release()
                print("Filosofo ", self.filosofosNum, "libre derecho")
                time.sleep(2)
                print("Filosofo ", self.filosofosNum, "libre izquierdo\n")
            finally:
                break   

    def run(self):
        self.hilosFilosofos()

tenedorArray = [1,1,1,1,1]

for i in range(5):
    tenedorArray[i] = threading.BoundedSemaphore(1)

for i in range(5):
    total = TenedorFilosofo(tenedorArray, i)
    total.start() 
    total.join()