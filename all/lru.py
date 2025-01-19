from all.page_generator import page_ganerator
from queue import Queue
import os
from tkinter import messagebox
import xlsxwriter
class lru:
    def __init__(self):

        self.page_fault = 0
        self.hits = 0
        self.lista_hits = []
        self.lista_page_faults = []
        self.queue_stron = Queue()
        self.generator = page_ganerator()


    def copy_random_pages(self, random_pages_lista, liczba_elementow_w_kolejce, liczba_stron, liczba_wymian):
        self.queue_stron = Queue(maxsize=liczba_wymian)
        count = 0
        for strona in random_pages_lista:
            count+=1
            self.queue_stron.put(strona)

        self.liczba_elementow_w_kolejce = liczba_elementow_w_kolejce
        self.liczba_stron = liczba_stron
        self.liczba_wymian = liczba_wymian
    def make_random_pages(self, liczba_elementow_w_kolejce, liczba_stron, liczba_wymian):
        self.queue_stron = Queue(maxsize=liczba_wymian)
        self.liczba_elementow_w_kolejce = liczba_elementow_w_kolejce
        self.liczba_stron = liczba_stron
        self.liczba_wymian = liczba_wymian
        self.queue_stron = self.generator.make_random_pages( self.liczba_stron, self.liczba_wymian)
    def make_xlsx(self, final_file_path, final_file_path_wej, sheet_name):
        if os.path.exists(final_file_path):
                os.remove(final_file_path)
                messagebox._show("Info",f'{final_file_path} już istnieje, usuwam\n ')

        messagebox._show("Info",f'{final_file_path} nie istnieje, tworzę')

        try:
            print(final_file_path, ' Został stworzony')
            self.wb = xlsxwriter.Workbook(f'{final_file_path}')
            messagebox._show("Success",f'{final_file_path}')
        except Exception as e:
            print(f"An error occurred: {e}")
            self.errorbox('Error', f'{final_file_path}')
        self.wb_1 = self.wb.add_worksheet(f'{sheet_name}')

        if os.path.exists(final_file_path_wej):
                os.remove(final_file_path_wej)
                messagebox._show("Info",f'{final_file_path_wej} już istnieje, usuwam\n ')

        messagebox._show("Info",f'{final_file_path_wej} nie istnieje, tworzę')

        try:
            print(final_file_path_wej, ' Został stworzony')
            self.wb_wej = xlsxwriter.Workbook(f'{final_file_path_wej}')
            messagebox._show("Success",f'{final_file_path_wej}')
        except Exception as e:
            print(f"An error occurred: {e}")
            self.errorbox('Error', f'{final_file_path_wej}')
        self.wb_1_wej = self.wb_wej.add_worksheet(f'{sheet_name}')
    def connect_to_wb_wb_1(self, wb, wb_1, wb_wej, wb_1_wej):
        self.wb = wb
        self.wb_1 = wb_1
        self.wb_1_wej = wb_1_wej
        self.wb_wej = wb_wej
    def calculatings(self, StartRow=1, StartColumn=1):
        self.set = set()

        self.queue_lista = list()
        self.lista = list()
        self.column = StartColumn
        self.row = StartRow
        for i in range(self.liczba_wymian):
            self.wb_1.write(self.row, self.column+i, self.queue_stron.queue[i])
            # print(('self.queue_stron.queue[i] = ',self.queue_stron.queue[i]))
        self.wb_1.write(self.row-1, 0, f'Least Recently Used - {self.liczba_elementow_w_kolejce}')
        self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+1, 0, 'hits')
        self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+1+1, 0, 'page faults')
        for i in range(self.liczba_wymian):#cala geirka tu sie zaczyna
            strona = self.queue_stron.get()# pobieranie strony z kolejki i jej usunięcie z kolejki
            if(len(self.set))<self.liczba_elementow_w_kolejce:# set nie jest pełny
                if strona not in self.set:# jeśli w set'ie nie ma strony -> page_fault+=1
                    if len(self.queue_lista) == self.liczba_elementow_w_kolejce:
                        # print(f'{i}Set nie jest pełny, strony nie ma ale queue_lista jest pełny.Dodawanie {strona} do queue_elementow, ale usuwamy poprzedni')
                        wyrzucone_z_kolejki = self.queue_lista.pop(0)
                        self.lista[self.lista.index(wyrzucone_z_kolejki)] = strona
                        self.queue_lista.append(strona)
                        self.set.add(strona)
                        self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+2, self.column+i, '*')
                        self.page_fault+=1
                    else:
                        # print(f'{i}Set nie jest pełny, strony nie ma, queue_lista nie jest pełny.Dodawanie {strona} do queue_elementow, ale usuwamy poprzedni')
                        self.queue_lista.append(strona)
                        self.lista.append(strona)
                        self.set.add(strona)# dodaje stronę do set'u
                        self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+2, self.column+i, '*')
                        self.page_fault+=1
                else: # set nie jest pełny, ale taka strona już istnieje -> hits+=1
                    if len(self.queue_lista) == self.liczba_elementow_w_kolejce:
                        # print(f'{i}Set nie jest pełny, ale taka strona już istnieje, queue_lista jest pełny. Dodawanie {strona} do queue_elementow')
                        self.queue_lista.pop(self.queue_lista.index(strona))#wyrzucamy stronę z kolejki
                        self.queue_lista.append(strona)#dodajemy stronę na sam koniec kolejki
                        self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+1, self.column+i, '*')
                        self.hits+=1
                    else:
                        # print(f'{i}Set nie jest pełny, ale taka strona już istnieje, queue_lista nie jest pełny. Dodawanie {strona} do queue_elementow')
                        self.queue_lista.pop(self.queue_lista.index(strona))#wyrzucamy stronę z kolejki
                        self.queue_lista.append(strona)#dodajemy stronę na sam koniec kolejki
                        self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+1, self.column+i, '*')
                        self.hits+=1
            else:# set jest pełny
                if strona not in self.set:
                    strona_do_usuniecia_w_secie = self.queue_lista.pop(0)
                    self.lista[self.lista.index(strona_do_usuniecia_w_secie)] = strona # usuwamy stronę z queue_lista i zapisujemy strone w lista na poprawnym miejscu
                    # print(f'{i}Set jest pełny, ale taka strona nie istnieje, queue_elemntów jest pełny. Dodawanie {strona} do queue_elementow')
                    self.queue_lista.append(strona)
                    try:
                        self.set.remove(strona_do_usuniecia_w_secie)
                    except:

                        continue
                    self.set.add(strona)# dodaje do set'u
                    self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+2, self.column+i, '*')
                    self.page_fault+=1
                else:
                    # print(f'{i}Set  jest pełny, ale taka strona już istnieje, queue_elemntów jest pełny. Dodawanie {strona} do queue_elementow')

                    self.queue_lista.pop(self.queue_lista.index(strona))#usuwamy stronę
                    self.queue_lista.append(strona)#aby wrzucic ję na sam koniec kolejki

                    self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+1 , self.column+i, '*')
                    self.hits+=1
            for j in range(self.liczba_elementow_w_kolejce):
                try:
                    self.wb_1.write(1+self.row+j, self.column+i, self.lista[j])
                except:
                    break
            print(len(self.lista))
        self.lista_hits.append(self.hits)
        self.lista_page_faults.append(self.page_fault)
        self.wb_1.write(3+self.row+self.liczba_elementow_w_kolejce, 0, 'hits = ')
        self.wb_1.write(3+self.row+self.liczba_elementow_w_kolejce, 1, self.hits)
        self.wb_1.write(4+self.row+self.liczba_elementow_w_kolejce, 0, 'page faults = ')
        self.wb_1.write(4+self.row+self.liczba_elementow_w_kolejce, 1, self.page_fault)
        self.page_fault = 0
        self.hits = 0
    def add_data_toxlsx(self):

        self.wb_1.write(5, 114, 'LRU H')
        self.wb_1.write(5, 115, 'LRU PF')

        for i in range(len(self.lista_hits)):

            self.wb_1.write(6+i, 114, self.lista_hits[i])
            self.wb_1.write(6+i, 115, self.lista_page_faults[i])
        self.lista_hits = []
        self.lista_page_faults = []
    def close_xlsl_file(self):
        self.wb_wej.close()
        self.wb.close()
