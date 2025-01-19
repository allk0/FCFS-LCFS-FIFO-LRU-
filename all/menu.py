import random
from tkinter import *
from tkinter import ttk
from all.eksperymenty import eksperymenty
from tkinter import messagebox
from all.fcfs import fcfs
from all.lcfs import lcfs
from all.fifo import fifo
from all.lru import lru
from random import randint
import os
class menu:
    def __init__(self):
# create main window and label
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.parent_dir = os.path.dirname(self.current_dir)
        self.algorytm_name = None
        self.alg = None
        self.root = Tk()
        self.root.title("Combobox Example")
        self.root.geometry('400x450')
        self.selected_option = None
        self.selected_index = None
        self.LabelProjektSystemy = ttk.Label(self.root, text='Projekt systemy')
        self.LabelProjektSystemy.grid(row = 0, column=1)
        self.LabelProjektSystemy = ttk.Label(self.root, text='\t \t ')
        self.LabelProjektSystemy.grid(row = 1, column=0)
        self.combo = ttk.Combobox(self.root, values=["1. FCFS - First Come First Serve", "2. LCFS - Last Come First Serve", "3. FIFO - First In First Out", "4. LRU - Least Recently Used", "Eksperymenty"])
        self.combo.grid(row = 1, column = 1)
        self.StartButton = ttk.Button(text = 'Start', command=lambda: self.StartButtonClicked(self.combo.current()))
        self.StartButton.grid(row = 2, column=1, padx=10, pady=10)
        self.StartButton = ttk.Button(text = 'Start', command=lambda: self.StartButtonClicked(self.combo.current()))
        self.StartButton.grid(row = 2, column=1, padx=10, pady=10)

        self.radioButtonOption = IntVar()
        self.radioButtonOptionEks = IntVar()
        self.EntryLiczbaStronVar = IntVar()
        self.EntryLiczbaStronVar.set(random.randint(5,7))
        self.EntryLiczbaElementowVar = IntVar()
        self.EntryLiczbaElementowVar.set(random.randint(2,5))
        self.EntryLiczbaWymianVar = IntVar()
        self.EntryLiczbaWymianVar.set(random.randint(40,50))

        self.widgets_of_processes = []
        self.r1 = ttk.Radiobutton(self.root, text='25', var=self.radioButtonOption, value=25, state=ACTIVE)
        self.widgets_of_processes.append(self.r1)
        self.r2 = ttk.Radiobutton(self.root, text='75', var=self.radioButtonOption, value=75, state=ACTIVE)
        self.widgets_of_processes.append(self.r2)
        self.r3 = ttk.Radiobutton(self.root, text='125', var=self.radioButtonOption, value=125, state=ACTIVE)
        self.widgets_of_processes.append(self.r3)
        self.LabelRadioText = ttk.Label(self.root, text = 'Wybierz liczbę procesów')        
        self.widgets_of_processes.append(self.LabelRadioText)
        self.widgets_of_strony = []
        self.LabelEntryText = ttk.Label(self.root, text='Wpisz liczbę \nramek :')
        self.LabelEntryText2 = ttk.Label(self.root, text='Wpisz liczbę \nstron :')
        self.LabelEntryText3 = ttk.Label(self.root, text='Wpisz liczbę\n wymiany \nstron :')
        self.widgets_of_strony.append(self.LabelEntryText)
        self.widgets_of_strony.append(self.LabelEntryText2)
        self.widgets_of_strony.append(self.LabelEntryText3)

        self.liczba_elementow_w_kolejce = None
        self.liczba_stron = None
        self.liczba_wymian = None

        self.EntryLiczbaElementow = ttk.Entry(textvariable = self.EntryLiczbaElementowVar, width=5)
        self.EntryLiczbaStron = ttk.Entry(textvariable = self.EntryLiczbaStronVar, width=5)
        self.EntryLiczbaWymianyStron = ttk.Entry(textvariable = self.EntryLiczbaWymianVar, width=5)
        self.widgets_of_strony.append(self.EntryLiczbaElementow)
        self.widgets_of_strony.append(self.EntryLiczbaStron)
        self.widgets_of_strony.append(self.EntryLiczbaWymianyStron)

        self.widgets_of_ekserymenty = []
        self.RadioEksperyment1 = ttk.Radiobutton(self.root, text='25, 75, 125 procesów o wzrastającym czasie nadejścia,\n ale u ostatnich procesów większy czas wykonywania', var=self.radioButtonOptionEks, value=1, state=ACTIVE)
        self.RadioEksperyment2 = ttk.Radiobutton(self.root, text='25, 75, 125 procesów o wzrastającym czasie nadejścia\n i wzrastającym czasie wykonywania', var=self.radioButtonOptionEks, value=2, state=ACTIVE)
        self.RadioEksperyment3 = ttk.Radiobutton(self.root, text='25, 75, 125 procesów o wzrastającym czasie nadejścia\n i malejącym czasie wykonywania', var=self.radioButtonOptionEks, value=3, state=ACTIVE)
        self.RadioEksperyment4 = ttk.Radiobutton(self.root, text='25, 75, 125 procesów o wzrastającym czasie nadejścia,\n ale u pierwszych procesów większy czas wykonywania', var=self.radioButtonOptionEks, value=4, state=ACTIVE)
        self.RadioEksperyment5 = ttk.Radiobutton(self.root, text='25, 75, 125 procesów o losowym czasie nadejścia od 0 100\n i losowym czasie wykonywania od 0 do 10', var=self.radioButtonOptionEks, value=5, state=ACTIVE)
        self.RadioEksperyment6 = ttk.Radiobutton(self.root, text='25 stron z  liczbą ramek od 5 do 15\n liczba wymian - 100', var=self.radioButtonOptionEks, value=6, state=ACTIVE)
        self.RadioEksperyment7 = ttk.Radiobutton(self.root, text='125 stron z liczbą ramek 5 do 15 \nliczba wymian - 100', var=self.radioButtonOptionEks, value=7, state=ACTIVE)

        self.RadioEksperyment9 = ttk.Radiobutton(self.root, text='225 stron z liczbą ramek 45-50 \nliczba wymian - 100', var=self.radioButtonOptionEks, value=8, state=ACTIVE)

        self.widgets_of_ekserymenty.append(self.RadioEksperyment1)
        self.widgets_of_ekserymenty.append(self.RadioEksperyment2)
        self.widgets_of_ekserymenty.append(self.RadioEksperyment3)
        self.widgets_of_ekserymenty.append(self.RadioEksperyment4)
        self.widgets_of_ekserymenty.append(self.RadioEksperyment5)
        self.widgets_of_ekserymenty.append(self.RadioEksperyment6)
        self.widgets_of_ekserymenty.append(self.RadioEksperyment7)

        self.widgets_of_ekserymenty.append(self.RadioEksperyment9)
        def option_selected(event):
           if self.combo.current() == 0 or self.combo.current() == 1:

                for widget in self.widgets_of_strony:
                    widget.grid_forget()

                for widget in self.widgets_of_ekserymenty:
                    widget.grid_forget()

                self.LabelRadioText.grid(row = 3, column=1)
                self.r1.grid(row = 4, column=0)
                self.r2.grid(row = 4, column=1)
                self.r3.grid(row = 4, column=2)

           elif self.combo.current() == 2 or self.combo.current() == 3:

                for widget in self.widgets_of_processes:
                    widget.grid_forget()

                for widget in self.widgets_of_ekserymenty:
                    widget.grid_forget()

                self.LabelEntryText.grid(row = 3, column=0)
                self.LabelEntryText2.grid(row = 3, column=1)
                self.LabelEntryText3.grid(row = 3, column=2)
                self.EntryLiczbaElementow.grid(row = 4, column =0 )
                self.EntryLiczbaWymianyStron.grid(row = 4, column =2 )
                self.EntryLiczbaStron.grid(row = 4, column =1 )
           elif self.combo.current() == 4:

               for widget in self.widgets_of_processes:
                   widget.grid_forget()

               for widget in self.widgets_of_strony:
                   widget.grid_forget()

               self.RadioEksperyment1.grid(row=3, column=0, columnspan = 3, sticky =W)
               self.RadioEksperyment2.grid(row=4, column=0, columnspan = 3, sticky =W)
               self.RadioEksperyment3.grid(row=5, column=0, columnspan = 3, sticky =W)
               self.RadioEksperyment4.grid(row=6, column=0, columnspan = 3, sticky =W)
               self.RadioEksperyment5.grid(row=7, column=0, columnspan = 3, sticky =W)
               self.RadioEksperyment6.grid(row=8, column=0, columnspan = 3, sticky =W)
               self.RadioEksperyment7.grid(row=9, column=0, columnspan = 3, sticky =W)
               self.RadioEksperyment9.grid(row=10, column=0, columnspan = 3, sticky =W)

           self.selected_option = self.combo.get()
           self.selected_index = self.combo.current()
           print("Wybrany algorytm:", self.selected_option, '\n index wybranego algorytmu: ', self.selected_index)
        self.combo.bind("<<ComboboxSelected>>", option_selected)

        self.root.mainloop()
    def resource_path(self, relative_path):

        return os.path.join(self.parent_dir, relative_path)
    def StartButtonClicked(self, index):
        if index == 0:
            self.algorytm_name = 'FCFS'
            print(f'Uruchomiony proces: {self.algorytm_name} - First Come First Serve')
            self.liczbaprocesow = self.radioButtonOption.get()
            print('Wybrana liczba procesów: ', self.liczbaprocesow)
            messagebox._show('Info',f'Uruchomiony proces: {self.algorytm_name} - First Come First Serve\n Wybrana liczba procesó: {self.liczbaprocesow}' )
            self.alg = fcfs()
            self.alg.make_random_processes(self.liczbaprocesow)#zwraca N procesów z losowymi arrival_time i burst_time

            self.directory = "Algorytmy"
            self.path = os.path.join(self.parent_dir, self.directory)

            try:
                os.mkdir(self.path)
            except:
                print(f'{self.path} już stworzony')
            self.final_file_path = self.path + f'\{self.algorytm_name}_{self.liczbaprocesow}.xlsx' #tworzenie pliku xlsx
            self.final_file_path_wej = self.path + f'\{self.algorytm_name}_{self.liczbaprocesow}wej.xlsx'
            self.alg.make_xlsx_file(self.final_file_path,self.final_file_path_wej, 'First Come First Serve')
            self.alg.make_xlsx_random()
            self.alg.calculatings()
            self.alg.make_xlsx_sorted()
            self.alg.close_xlsl_file()
        if index == 1:
            self.algorytm_name = 'LCFS'
            print(f'Uruchomiony proces: {self.algorytm_name} - Last Come First Serve')
            self.liczbaprocesow = self.radioButtonOption.get()
            print('Wybrana liczba procesów: ', self.liczbaprocesow)
            messagebox._show('Info',f'Uruchomiony proces: {self.algorytm_name} - Last Come First Serve\n Wybrana liczba procesó: {self.liczbaprocesow}' )
            self.alg = lcfs()
            self.alg.make_random_processes(self.liczbaprocesow)#zwraca N procesów z losowymi arrival_time i burst_time
            self.directory = "Algorytmy"
            self.path = os.path.join(self.parent_dir, self.directory)
            try:
                os.mkdir(self.path)
            except:
                print(f'{self.path} już stworzony')
            self.final_file_path = self.path + f'\{self.algorytm_name}_{self.liczbaprocesow}.xlsx' #tworzenie pliku xlsx
            self.final_file_path_wej = self.path + f'\{self.algorytm_name}_{self.liczbaprocesow}wej.xlsx'
            self.alg.make_xlsx_file(self.final_file_path,self.final_file_path_wej, 'First Come First Serve')
            self.alg.make_xlsx_random()
            self.alg.calculatings()
            self.alg.make_xlsx_sorted()
            self.alg.close_xlsl_file()
        elif index == 2:
            self.algorytm_name = 'FIFO'
            print(f'Uruchomiony algorytm: {self.algorytm_name}')
            self.liczba_elementow_w_kolejce = self.EntryLiczbaElementowVar.get()
            self.liczba_stron = self.EntryLiczbaStronVar.get()
            self.liczba_wymian = self.EntryLiczbaWymianVar.get()
            print('Wybrana liczba elementów w kolejce: ', self.liczba_elementow_w_kolejce)
            messagebox._show('Info',f'Uruchomiony proces: {self.algorytm_name} - '
                                    f'\n Wybrana liczba elementów : {self.liczba_elementow_w_kolejce}\n'
                                    f'Wybrana liczba stron :{self.liczba_stron} '
                                    f'Wybrana liczba wymian :{self.liczba_wymian}', )
            self.alg = fifo()

            self.directory = "Algorytmy"
            self.path = os.path.join(self.parent_dir, self.directory)
            try:
                os.mkdir(self.path)
            except:
                print(f'{self.path} już stworzony')
            self.final_file_path = self.path + f'\{self.algorytm_name}_{self.liczba_elementow_w_kolejce}_{self.liczba_stron}_{self.liczba_wymian}.xlsx' #tworzenie pliku xlsx
            self.final_file_path_wej = self.path + f'\{self.algorytm_name}_{self.liczba_elementow_w_kolejce}_{self.liczba_stron}_{self.liczba_wymian}.xlsx'
            self.alg.make_xlsx(self.final_file_path,self.final_file_path_wej, 'First Come First Serve')
            self.alg.make_random_pages(liczba_stron=self.liczba_stron, liczba_wymian=self.liczba_wymian, liczba_elementow_w_kolejce=self.liczba_elementow_w_kolejce)#zwraca N procesów
            self.alg.calculatings()
            self.alg.close_xlsl_file()
        elif index == 3:
            self.algorytm_name = 'LRU'
            print(f'Uruchomiony algorytm: {self.algorytm_name}')
            self.liczba_elementow_w_kolejce = self.EntryLiczbaElementowVar.get()
            self.liczba_stron = self.EntryLiczbaStronVar.get()
            self.liczba_wymian = self.EntryLiczbaWymianVar.get()
            print('Wybrana liczba elementów w kolejce: ', self.liczba_elementow_w_kolejce)
            messagebox._show('Info',f'Uruchomiony proces: {self.algorytm_name} - '
                                    f'\n Wybrana liczba elementów : {self.liczba_elementow_w_kolejce}\n'
                                    f'Wybrana liczba stron :{self.liczba_stron} '
                                    f'Wybrana liczba wymian :{self.liczba_wymian}', )
            self.alg = lru()
            self.alg.make_random_pages(liczba_elementow_w_kolejce=self.liczba_elementow_w_kolejce,liczba_stron=self.liczba_stron, liczba_wymian=self.liczba_wymian,)#zwraca N procesów
            self.directory = "Algorytmy"
            self.path = os.path.join(self.parent_dir, self.directory)
            try:
                os.mkdir(self.path)
            except:
                print(f'{self.path} już stworzony')
            self.final_file_path = self.path + f'\{self.algorytm_name}_{self.liczba_elementow_w_kolejce}_{self.liczba_stron}_{self.liczba_wymian}.xlsx'
            self.final_file_path_wej = self.path + f'\{self.algorytm_name}_{self.liczba_elementow_w_kolejce}_{self.liczba_stron}_{self.liczba_wymian}.xlsx'
            self.alg.make_xlsx(self.final_file_path,self.final_file_path_wej, 'First Come First Serve')
            self.alg.calculatings()
            self.alg.close_xlsl_file()
        if index == 4 or index == 5 or index == 6 or index == 7 or index == 8:
            print('index = ', index)
            print(self.radioButtonOptionEks.get(), 'radioButtonOptionEks')
            self.algorytm_name = 'Eksperymenty'
            self.eksperyment = eksperymenty(self.radioButtonOptionEks.get())

