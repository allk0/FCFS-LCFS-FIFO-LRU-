from all.page_generator import page_ganerator
from queue import Queue
import os
from tkinter import messagebox
import xlsxwriter
class fifo:
    def __init__(self):
        self.liczba_elementow_w_kolejce = None
        self.page_fault = 0
        self.hits = 0
        self.liczba_stron = None
        self.liczba_wymian = None
        self.lista_stron = []
        self.generator = page_ganerator()
        self.lista_hits = []
        self.lista_page_faults =[]
        self.sheet_name = None
    def get_niposortowane_processy(self):
        return self.lista_stron
    def get_wb_wb_1(self):
        return self.wb, self.wb_1, self.wb_wej, self.wb_1_wej
    def make_random_pages(self, liczba_elementow_w_kolejce, liczba_stron, liczba_wymian):
        self.liczba_elementow_w_kolejce = liczba_elementow_w_kolejce
        self.liczba_wymian = liczba_wymian
        self.lista_stron = []
        self.liczba_stron = liczba_stron
        self.queue_stron = Queue(maxsize=self.liczba_wymian)
        self.queue_elementow = Queue(maxsize=self.liczba_elementow_w_kolejce)
        self.queue_stron = self.generator.make_random_pages(liczba_stron, liczba_wymian )
        for i in range(liczba_wymian):
            self.lista_stron.append(self.queue_stron.queue[i])
            self.wb_1_wej.write(0, i, self.queue_stron.queue[i])
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
        self.sheet_name = sheet_name
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
    def calculatings(self, StartRow=1, StartColumn=1):
        self.column = StartColumn
        self.row = StartRow
        self.lista_elementow = []

        try:
            print(self.queue_stron.queue[0])
        except:
            print('na')
        for i in range(self.liczba_wymian):
            self.wb_1.write(self.row, self.column+i, self.queue_stron.queue[i])
        self.wb_1.write(self.row-1, 0, f'First IN First Out - {self.liczba_elementow_w_kolejce}')
        self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+1, 0, 'hits')
        self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+2, 0, 'page faults')
        self.set = set()
        self.lista = []
        for i in range(self.liczba_wymian):#cala geirka tu sie zaczyna
            strona = self.queue_stron.get()
            if(len(self.set))<self.liczba_elementow_w_kolejce:# set nie jest pełny
                if strona not in self.set:# jeśli w set'ie nie ma strony -> page_fault+=1
                    # print(f'{i}Set nie jest pełny, strony nie ma ale queue_lista jest pełny.Dodawanie {strona} do queue_elementow, ale usuwamy poprzedni')

                    self.lista.append(strona)
                    self.queue_elementow.put(strona)
                    self.set.add(strona)# dodaje do set'u
                    self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+2, self.column+i, '*')
                    self.page_fault+=1
                else: # set nie jest pełny, ale taka strona już istnieje -> hits+=1
                    self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+1, self.column+i, '*')
                    self.hits+=1
            else:# set jest pełny
                if strona not in self.set:
                    # usuwa stronę z kolejki i przenosi do zmiennej 'strona'
                    strona_do_usuniecia_w_secie = self.queue_elementow.get()
                    self.lista[self.lista.index(strona_do_usuniecia_w_secie)] = strona
                    self.queue_elementow.put(strona)
                    self.set.remove(strona_do_usuniecia_w_secie)

                    self.set.add(strona)# dodaje do set'u
                    self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+2, self.column+i, '*')
                    self.page_fault+=1
                else:
                    self.wb_1.write(self.row+self.liczba_elementow_w_kolejce+1 , self.column+i, '*')
                    self.hits+=1

            for j in range(len(self.lista)):
                try:
                    # print('self.wb_1.write(',1+self.row+j,'', self.column+i,'', self.lista[j],')')
                    self.wb_1.write(1+self.row+j, self.column+i, self.lista[j])
                except:
                    break
        self.lista_hits.append(self.hits)
        self.lista_page_faults.append(self.page_fault)
        self.wb_1.write(3+self.row+self.liczba_elementow_w_kolejce, 0, 'hits = ')
        self.wb_1.write(3+self.row+self.liczba_elementow_w_kolejce, 1, self.hits)
        self.wb_1.write(4+self.row+self.liczba_elementow_w_kolejce, 0, 'page faults = ')
        self.wb_1.write(4+self.row+self.liczba_elementow_w_kolejce, 1, self.page_fault)
        self.hits = 0
        self.page_fault = 0
    def add_data_toxlsx(self, sheet_name = 'name'):
         # Create a new chart object.
        self.chart = self.wb.add_chart({'type': 'column'})
        self.chart_name = 'Wyniki'
        self.chart.set_title({'name': f'{self.chart_name}'})
        self.wb_1.write(5, 111, 'Ramki')
        self.wb_1.write(5, 112, 'FIFO H')
        self.wb_1.write(5, 113, 'FIFO PF')
        startIndex = 0
        if self.liczba_elementow_w_kolejce == 15:
            startIndex = 5
        elif self.liczba_elementow_w_kolejce == 50:
            startIndex = 45
        for i in range(len(self.lista_hits)):#wyświetla sprawa tabelkę z hits i page faults

            self.wb_1.write(6+i, 111, i+startIndex )
            self.wb_1.write(6+i, 112, self.lista_hits[i])
            self.wb_1.write(6+i, 113, self.lista_page_faults[i])
        self.chart.add_series({'categories' : f'={self.sheet_name}!$DH$7:$DH{len(self.lista_hits)+7}', 'values': f'={self.sheet_name}!$DI$7:$DI{len(self.lista_hits)+7}', 'name' :'FIFO H', 'fill':   {'color': 'red'}})
        self.chart.add_series({'categories' : f'={self.sheet_name}!$DH$7:$DH{len(self.lista_hits)+7}','values': f'={self.sheet_name}!$DJ$7:$DJ${len(self.lista_hits)+7}','name' :'FIFO PF', 'fill':   {'color': 'black'}})
        self.chart.add_series({'categories' : f'={self.sheet_name}!$DH$7:$DH{len(self.lista_hits)+7}','values': f'={self.sheet_name}!$DK$7:$DK{len(self.lista_hits)+7}', 'name' :'LRU H', 'fill':   {'color': 'blue'}})
        self.chart.add_series({'categories' : f'={self.sheet_name}!$DH$7:$DH{len(self.lista_hits)+7}','values': f'={self.sheet_name}!$DL$7:$DL${len(self.lista_hits)+7}','name' :'LRU PF', 'fill':   {'color': 'orange'}})
        # Insert the chart into the worksheet.
        self.wb_1.insert_chart(f'CZ13', self.chart)



    def close_xlsl_file(self):
        self.wb_wej.close()
        self.wb.close()
