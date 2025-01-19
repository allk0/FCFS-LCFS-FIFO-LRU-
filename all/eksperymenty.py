from all.fcfs import fcfs
from all.lcfs import lcfs
from all.fifo import fifo
from all.lru import lru
import os
class eksperymenty():
    def __init__(self, choose):
        self.choose = choose
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.parent_dir = os.path.dirname(self.current_dir)
        self.directory = "Eksperymenty"
        self.path = os.path.join(self.parent_dir, self.directory)
        try:
            os.mkdir(self.path)
        except:
            print(f'{self.path} już stworzony')
        match self.choose:
            case 1:
                '''
                25/75/125 arrival_time = counter+
                          burst_time = na końcu dużo
                '''
                print('Enksperyment ', choose, 'started')
                self.alg = lcfs()
                self.alg2 = fcfs()

                self.final_file_path =self.path + f'\Eksperyment_{self.choose}_test.xlsx' #tworzenie pliku xlsx
                self.final_file_path_wej =self.path + f'\Eksperyment_{self.choose}_wej_test.xlsx' #tworzenie pliku xlsx
                self.alg.make_xlsx_file(final_file_path=self.final_file_path,final_file_path_wej=self.final_file_path_wej, sheet_name = f'Eksperyment_{choose}')#tworzenie .xlsx pliku
                self.liczba_procesow1 = 25
                self.alg.make_random_processes(self.liczba_procesow1, arrival_time= 'counter+', burst_time='counter++')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1


                self.alg.make_xlsx_random(2, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(2, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(2, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(2, 22, True)#wypisuje do .xlsx posortowane procesy
                self.alg.make_graph(3,27, 'Eksperyment_1')


                self.liczba_procesow2 = 75
                self.alg.make_random_processes(self.liczba_procesow2, arrival_time= 'counter+', burst_time='counter++')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1

                self.alg.make_xlsx_random(31, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(31, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(31, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(31, 22, True)#wypisuje do .xlsx posortowane procesy
                self.alg.make_graph(32,106,'Eksperyment_1')

                self.liczba_procesow3 = 125
                self.alg.make_random_processes(self.liczba_procesow3, arrival_time= 'counter+', burst_time='counter++')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1
                self.alg.make_xlsx_random(109, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(109, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(109, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(109, 22, True)#wypisuje do .xlsx posortowane procesy
                self.alg.make_graph(110,234,'Eksperyment_1')


                self.alg.close_xlsl_file()

            case 2:
                '''
                25/75/125 arrival_time = 10/20/30
                          burst_time = 10/20/30
                '''
                print('Enksperyment ', choose, 'started')
                self.alg = lcfs()
                self.alg2 = fcfs()
                self.final_file_path =self.path + f'\Eksperyment_{self.choose}_test.xlsx' #tworzenie pliku xlsx
                self.final_file_path_wej =self.path + f'\Eksperyment_{self.choose}_wej_test.xlsx' #tworzenie pliku xlsx
                self.alg.make_xlsx_file(final_file_path=self.final_file_path,final_file_path_wej=self.final_file_path_wej, sheet_name = f'Eksperyment_{choose}')#tworzenie .xlsx pliku
                self.liczba_procesow1 = 25

                self.alg.make_random_processes(self.liczba_procesow1, arrival_time= 'counter+', burst_time='counter+')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1


                self.alg.make_xlsx_random(2, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(2, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(2, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(2, 22, True)#wypisuje do .xlsx posortowane procesy
                self.alg.make_graph(3,27,'Eksperyment_2')


                self.liczba_procesow2 = 75
                self.alg.make_random_processes(self.liczba_procesow2, arrival_time= 'counter+', burst_time='counter+')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1

                self.alg.make_xlsx_random(31, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(31, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(31, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(31, 22, True)#wypisuje do .xlsx posortowane procesy
                self.alg.make_graph(32,106,'Eksperyment_2')
                self.liczba_procesow3 = 125
                self.alg.make_random_processes(self.liczba_procesow3,arrival_time= 'counter+', burst_time='counter+')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1
                self.alg.make_xlsx_random(109, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(109, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(109, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(109, 22, True)#wypisuje do .xlsx posortowane procesy
                self.alg.make_graph(110,234,'Eksperyment_2')

                self.alg.close_xlsl_file()
            case 3:
                '''
                25/75/125 arrival_time = counter+
                          burst_time = counter-
                '''
                print('Enksperyment ', choose, 'started')
                self.alg = lcfs()
                self.alg2 = fcfs()
                self.final_file_path =self.path + f'\Eksperyment_{self.choose}_test.xlsx' #tworzenie pliku xlsx
                self.final_file_path_wej =self.path + f'\Eksperyment_{self.choose}_wej_test.xlsx' #tworzenie pliku xlsx
                self.alg.make_xlsx_file(final_file_path=self.final_file_path,final_file_path_wej=self.final_file_path_wej, sheet_name = f'Eksperyment_{choose}')#tworzenie .xlsx pliku

                self.liczba_procesow1 = 25
                self.alg.make_random_processes(self.liczba_procesow1, arrival_time= 'counter+', burst_time='counter-')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1


                self.alg.make_xlsx_random(2, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(2, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(2, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(2, 22, True)#wypisuje do .xlsx posortowane procesy
                self.alg.make_graph(3,27,'Eksperyment_3')


                self.liczba_procesow2 = 75
                self.alg.make_random_processes(self.liczba_procesow2,arrival_time= 'counter+', burst_time='counter-')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1

                self.alg.make_xlsx_random(31, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(31, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(31, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(31, 22, True)#wypisuje do .xlsx posortowane procesy
                self.alg.make_graph(32,106,'Eksperyment_3')
                self.liczba_procesow3 = 125
                self.alg.make_random_processes(self.liczba_procesow3, arrival_time= 'counter+', burst_time='counter-')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1
                self.alg.make_xlsx_random(109, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(109, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(109, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(109, 22, True)#wypisuje do .xlsx posortowane procesy
                self.alg.make_graph(110,234,'Eksperyment_3')

                self.alg.close_xlsl_file()
            case 4:
                '''
                25/75/125 arrival_time = random(randint(5,15))/random(randint(15,25))/random(randint(25,35))
                          burst_time = random(randint(5,15))/random(randint(15,25))/random(randint(25,35))
                '''
                print('Enksperyment ', choose, 'started')
                self.alg = lcfs()
                self.alg2 = fcfs()
                self.final_file_path =self.path + f'\Eksperyment_{self.choose}_test.xlsx' #tworzenie pliku xlsx
                self.final_file_path_wej =self.path + f'\Eksperyment_{self.choose}_wej_test.xlsx' #tworzenie pliku xlsx
                self.alg.make_xlsx_file(final_file_path=self.final_file_path,final_file_path_wej=self.final_file_path_wej, sheet_name = f'Eksperyment_{choose}')#tworzenie .xlsx pliku

                self.liczba_procesow1 = 25
                self.alg.make_random_processes(self.liczba_procesow1, arrival_time= 'counter+', burst_time='++counter')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1
                self.alg.make_graph(3,27,'Eksperyment_4')

                self.alg.make_xlsx_random(2, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(2, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(2, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(2, 22, True)#wypisuje do .xlsx posortowane procesy


                self.liczba_procesow2 = 75
                self.alg.make_random_processes(self.liczba_procesow2, arrival_time= 'counter+', burst_time='++counter')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1

                self.alg.make_xlsx_random(31, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(31, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(31, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(31, 22, True)#wypisuje do .xlsx posortowane procesy

                self.alg.make_graph(32,106,'Eksperyment_4')
                self.liczba_procesow3 = 125
                self.alg.make_random_processes(self.liczba_procesow3, arrival_time= 'counter+', burst_time='++counter')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1
                self.alg.make_xlsx_random(109, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(109, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(109, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(109, 22, True)#wypisuje do .xlsx posortowane procesy

                self.alg.make_graph(110,234,'Eksperyment_4')

                self.alg.close_xlsl_file()
            case 5:
                '''
                25/75/125 arrival_time = random(randint(0,100))
                          burst_time = random(randint(0,10))
                '''
                print('Enksperyment ', choose, 'started')
                self.alg = lcfs()
                self.alg2 = fcfs()
                self.final_file_path =self.path + f'\Eksperyment_{self.choose}_test.xlsx' #tworzenie pliku xlsx
                self.final_file_path_wej =self.path + f'\Eksperyment_{self.choose}_wej_test.xlsx' #tworzenie pliku xlsx
                self.alg.make_xlsx_file(final_file_path=self.final_file_path,final_file_path_wej=self.final_file_path_wej, sheet_name = f'Eksperyment_{choose}')#tworzenie .xlsx pliku

                self.liczba_procesow1 = 25
                self.alg.make_random_processes(self.liczba_procesow1, arrival_time= 'random(randint(0,100))', burst_time= 'random(randint(0,100))')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1


                self.alg.make_xlsx_random(2, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(2, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(2, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(2, 22, True)#wypisuje do .xlsx posortowane procesy

                self.alg.make_graph(3,27,'Eksperyment_5')


                self.liczba_procesow2 = 75
                self.alg.make_random_processes(self.liczba_procesow2, arrival_time=  'random(randint(0,100))', burst_time= 'random(randint(0,10))')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1

                self.alg.make_xlsx_random(31, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(31, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(31, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(31, 22, True)#wypisuje do .xlsx posortowane procesy

                self.alg.make_graph(32,106,'Eksperyment_5')
                self.liczba_procesow3 = 125
                self.alg.make_random_processes(self.liczba_procesow3, arrival_time=  'random(randint(0,100))', burst_time= 'random(randint(0,10))')#zwraca N procesów z losowymi arrival_time i burst_time
                self.nieposortowane_procesy = self.alg.get_niposortowane_processy()
                self.alg2.copy_random_processes(self.nieposortowane_procesy)#copiuje niposortowane procesy od alg 1
                self.alg.make_xlsx_random(109, 1, True)#wypisuje do .xlsx nisortowane procesy
                self.alg.calculatings()
                self.alg.make_xlsx_sorted(109, 7,True)#wypisuje do .xlsx posortowane procesy

                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym

                self.alg2.make_xlsx_random(109, 16, True)#wypisuje do .xlsx nisortowane procesy
                self.alg2.calculatings()
                self.alg2.make_xlsx_sorted(109, 22, True)#wypisuje do .xlsx posortowane procesy

                self.alg.make_graph(110,234,'Eksperyment_5')

                self.alg.close_xlsl_file()
            case 6:
                '''
                25 stron z  liczbą ramek od 5 do 15\n liczba wymian - 100
                
                '''
                self.alg = fifo()
                self.alg2 = lru()
                self.final_file_path =self.path + f'\Eksperyment_{self.choose}_test.xlsx' #tworzenie pliku xlsx
                self.final_file_path_wej =self.path + f'\Eksperyment_{self.choose}_wej_test.xlsx' #tworzenie pliku xlsx
                self.alg.make_xlsx(final_file_path=self.final_file_path,final_file_path_wej=self.final_file_path_wej, sheet_name = f'Eksperyment_{choose}')#tworzenie .xlsx pliku
                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym
                self.column = 1
                self.row = 1
                for liczba_elementow_w_kolejce in range(5,16):

                    self.alg.make_random_pages(liczba_elementow_w_kolejce=liczba_elementow_w_kolejce,liczba_stron=25, liczba_wymian=100)

                    li=self.alg.get_niposortowane_processy()
                    
                    self.alg2.copy_random_pages(random_pages_lista=li, liczba_elementow_w_kolejce=liczba_elementow_w_kolejce,liczba_stron=25, liczba_wymian=100)
                    self.alg.calculatings(StartRow=self.row, StartColumn=self.column)
                    self.alg2.calculatings(StartRow=(self.row+6+liczba_elementow_w_kolejce), StartColumn=self.column)

                    self.row+=liczba_elementow_w_kolejce*2+20+2
                self.alg2.add_data_toxlsx()
                self.alg.add_data_toxlsx()


                self.alg.close_xlsl_file()
            case 7:
                '''
                125 stron z liczbą ramek 5 - 15 \nliczba wymian - 100
                '''
                self.alg = fifo()
                self.alg2 = lru()
                self.final_file_path =self.path + f'\Eksperyment_{self.choose}_test.xlsx' #tworzenie pliku xlsx
                self.final_file_path_wej =self.path + f'\Eksperyment_{self.choose}_wej_test.xlsx' #tworzenie pliku xlsx
                self.alg.make_xlsx(final_file_path=self.final_file_path,final_file_path_wej=self.final_file_path_wej, sheet_name = f'Eksperyment_{choose}')#tworzenie .xlsx pliku
                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym
                self.column = 1
                self.row = 1
                for liczba_elementow_w_kolejce in range(5,16):

                    self.alg.make_random_pages(liczba_elementow_w_kolejce=liczba_elementow_w_kolejce,liczba_stron=125, liczba_wymian=100)

                    li=self.alg.get_niposortowane_processy()

                    self.alg2.copy_random_pages(random_pages_lista=li, liczba_elementow_w_kolejce=liczba_elementow_w_kolejce,liczba_stron=125, liczba_wymian=100)
                    self.alg.calculatings(StartRow=self.row, StartColumn=self.column)
                    self.alg2.calculatings(StartRow=(self.row+6+liczba_elementow_w_kolejce), StartColumn=self.column)

                    self.row+=liczba_elementow_w_kolejce*2+20+2
                self.alg2.add_data_toxlsx()
                self.alg.add_data_toxlsx()

                self.alg.close_xlsl_file()


            case 8:
                '''
                225 stron z liczbą ramek 45-50 \nliczba wymian - 100
                '''
                self.alg = fifo()
                self.alg2 = lru()
                self.final_file_path =self.path + f'\Eksperyment_{self.choose}_test.xlsx' #tworzenie pliku xlsx
                self.final_file_path_wej =self.path + f'\Eksperyment_{self.choose}_wej_test.xlsx' #tworzenie pliku xlsx
                self.alg.make_xlsx(final_file_path=self.final_file_path,final_file_path_wej=self.final_file_path_wej, sheet_name = f'Eksperyment_{choose}')#tworzenie .xlsx pliku
                self.wb, self.wb_1, self.wb_wej, self.wb_1_wej = self.alg.get_wb_wb_1()
                self.alg2.connect_to_wb_wb_1(self.wb, self.wb_1, self.wb_wej, self.wb_1_wej)#łączy alg2 z arkuszem kalkulacyjnym
                self.column = 1
                self.row = 1
                for liczba_elementow_w_kolejce in range(45,51):

                    self.alg.make_random_pages(liczba_elementow_w_kolejce=liczba_elementow_w_kolejce,liczba_stron=225, liczba_wymian=100)

                    li=self.alg.get_niposortowane_processy()

                    self.alg2.copy_random_pages(random_pages_lista=li, liczba_elementow_w_kolejce=liczba_elementow_w_kolejce,liczba_stron=225, liczba_wymian=100)
                    self.alg.calculatings(StartRow=self.row, StartColumn=self.column)
                    self.alg2.calculatings(StartRow=(self.row+6+liczba_elementow_w_kolejce), StartColumn=self.column)

                    self.row+=liczba_elementow_w_kolejce*2+20+2
                self.alg2.add_data_toxlsx()
                self.alg.add_data_toxlsx()

                self.alg.close_xlsl_file()
