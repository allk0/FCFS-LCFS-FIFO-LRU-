import random
class process_generator:
    def __init__(self):
        self.processes_array = []
    def getProcesses_array(self, num, arrival_time, burst_time, na_koncu_dlugo = False):
        print('Generator : ', self.processes_array)
        if (len(self.processes_array) == 0):
            print('Tworzenie procesów')
            self.unique_arrival_times = list()
            if arrival_time == 'counter+':
                self.counter_arrival = 0
            else:
                self.counter_arrival = 375
            if burst_time == 'counter+':
                self.counter_burst = 0

            else:
                self.counter_burst = 375

            for i in range(0, int(num)): # od 1 do liczby wskazanych procesów (24, 74, 124)
                self.process = {}
                self.process['number'] = i+1


                if arrival_time == None:
                    while True:
                        self.process['arrival_time'] = random.randint(0,num*2)
                        if self.process['arrival_time'] not in self.unique_arrival_times:
                            self.unique_arrival_times.append(self.process['arrival_time'])
                            break
                elif arrival_time == 'counter+':
                    self.process['arrival_time'] = random.randint(0,5)+self.counter_arrival
                    self.counter_arrival = self.process['arrival_time']
                elif arrival_time == 'counter-':
                    self.process['arrival_time'] = self.counter_arrival - random.randint(2,3)
                    self.counter_arrival = self.process['arrival_time']
                elif arrival_time == 'random(randint(0,100))':
                    self.process['arrival_time'] = random.randint(0,100)
                elif arrival_time == 'random(randint(0,10))':
                    self.process['arrival_time'] = random.randint(0,10)
                elif arrival_time == 'random(randint(5,15))':
                    self.process['arrival_time'] = random.randint(5,15)
                elif arrival_time == 'random(randint(15,25))':
                    self.process['arrival_time'] = random.randint(15,25)
                elif arrival_time == 'random(randint(25,35))':
                    self.process['arrival_time'] = random.randint(25,35)
                else:
                    self.process['arrival_time'] = arrival_time


                if burst_time == None:

                    self.process['burst_time'] = random.randint(1,10)
                elif burst_time == 'counter++':
                    # print('Generator procesow i = ', i)
                    if i//(0.65*int(num)) == 1:
                        print('Generatoe wejście')
                        self.process['burst_time'] = random.randint(30,40)
                    else:
                        self.process['burst_time'] = random.randint(0,10)
                elif burst_time == '++counter':
                    # print('Generator procesow i = ', i)
                    if i//(0.35*int(num)) == 0:
                        print('Generatoe wejście')
                        self.process['burst_time'] = random.randint(30,40)
                    else:
                        self.process['burst_time'] = random.randint(0,10)
                elif burst_time == 'counter+':
                    self.process['burst_time'] = random.randint(0,5)+self.counter_burst
                    self.counter_burst = self.process['burst_time']

                elif burst_time == 'counter-':
                    self.process['burst_time'] = self.counter_burst - random.randint(2,3)
                    self.counter_burst = self.process['burst_time']
                elif burst_time == 'random(randint(0,100))':
                    self.process['burst_time'] = random.randint(0,100)
                elif burst_time == 'random(randint(0,10))':

                    self.process['burst_time'] = random.randint(0,10)
                elif burst_time == 'random(randint(5,15))':
                    self.process['burst_time'] = random.randint(5,15)

                elif burst_time == 'random(randint(15,25))':
                    self.process['burst_time'] = random.randint(15,25)

                elif burst_time == 'random(randint(25,35))':
                    self.process['burst_time'] = random.randint(25,35)

                else:
                    self.process['burst_time'] = burst_time
                self.processes_array.append(self.process)
        print('NIesortowane procesy stworzone')
        self.counter_arrival = 0
        self.counter_burst = 0
        return self.processes_array #zwraca array w postaci [{'number':x, 'arrival_time':y, 'burst_time':z}, {},{}...{n}]


