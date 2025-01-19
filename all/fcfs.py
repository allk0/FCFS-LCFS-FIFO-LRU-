from all.process_generator import process_generator
import os
import xlsxwriter
from tkinter import messagebox
"""
fcfs importuje process_generator 
process_generator oddaje listę postaci generated_processes = [{'number':x, 'arrival_time':y, 'burst_time':z}, {}, {}, ...]
lista jest niesortowana

fcfs sortuje 
"""
class fcfs(process_generator):
    def __init__(self):
        self.ct_array = list()
        self.tat_array = list()
        self.wt_array = list()
        self.sorted_number_array = list()
        self.sorted_arrival_time_array= list()
        self.sorted_burst_time_array= list()
        self.generator = process_generator()
        self.nieposortowane_procesy = list()
        self.posortowane_procesy = list()
        self.avg_burst_Time = None
        self.avg_completed_time = None
        self.avg_turn_around_time = None
        self.avg_waiting_time = None
    def make_random_processes(self, num):
        self.nieposortowane_procesy = self.generator.getProcesses_array(num, arrival_time= None, burst_time= None)
    def copy_random_processes(self, array):
        self.nieposortowane_procesy = array.copy()
    def connect_to_wb_wb_1(self, wb, wb_1, wb_wej, wb_1_wej):
        self.wb = wb
        self.wb_1 = wb_1
        self.wb_1_wej = wb_1_wej
        self.wb_wej = wb_wej
    def calculatings(self):
            self.current_time = 0

            self.index_p = 0
            while self.nieposortowane_procesy:
                print('len(nieposort) = ', len(self.nieposortowane_procesy))
                self.min_arrival_time = float('inf')
                self.index = None
                for i in range(len(self.nieposortowane_procesy)):
                    if self.min_arrival_time > self.nieposortowane_procesy[i]['arrival_time'] and self.nieposortowane_procesy[i]['arrival_time']<= self.current_time:
                        self.min_arrival_time = self.nieposortowane_procesy[i]['arrival_time']
                        self.index = i
                if self.index is not None:
                    process = self.nieposortowane_procesy[self.index]
                    self.posortowane_procesy.append(process)
                    self.posortowane_procesy[self.index_p]['completed_time'] = process['burst_time']+self.current_time

                    self.current_time += process['burst_time']
                    self.posortowane_procesy[self.index_p]['turn_around_time'] = self.posortowane_procesy[self.index_p]['completed_time']- process['arrival_time']
                    self.posortowane_procesy[self.index_p]['waiting_time'] = self.posortowane_procesy[self.index_p]['turn_around_time'] - process['burst_time']
                    self.posortowane_procesy[self.index_p]['current_time'] = self.current_time
                    self.index_p+=1

                    self.nieposortowane_procesy.pop(self.index)
                else:
                    self.current_time += 1

    def make_xlsx_file(self, final_file_path, final_file_path_wej, sheet_name):
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

    def make_xlsx_random(self, StartRow = 2, StartColumn = 1, EkspBool = False):
        self.row = StartRow
        self.column = StartColumn
        print('fcfs,make_xlsx_random, row = ',self.row, 'column = ', self.column, 'EkspBool = ', EkspBool)
        headers = ['number', 'AT', 'BT']
        self.wb_1.write(self.row-2, self.column, f'First Come First Serve, liczba procesów - {len(self.nieposortowane_procesy)}')
        self.wb_1_wej.write(self.row-2, self.column, f'First Come First Serve, liczba procesów - {len(self.nieposortowane_procesy)}')

        for col_num, header in enumerate(headers):
            self.wb_1.write(self.row-1, col_num+self.column, header)
            self.wb_1_wej.write(self.row-1, col_num+self.column, header)

        for process in range(len(self.nieposortowane_procesy)):
            self.wb_1.write(self.row+process, self.column, self.nieposortowane_procesy[process]['number'])
            self.wb_1.write(self.row+process, self.column+1, self.nieposortowane_procesy[process]['arrival_time'])
            self.wb_1.write(self.row+process, self.column+2, self.nieposortowane_procesy[process]['burst_time'])
            self.wb_1_wej.write(self.row+process, self.column, self.nieposortowane_procesy[process]['number'])
            self.wb_1_wej.write(self.row+process, self.column+1, self.nieposortowane_procesy[process]['arrival_time'])
            self.wb_1_wej.write(self.row+process, self.column+2, self.nieposortowane_procesy[process]['burst_time'])

    def make_xlsx_sorted(self, StartRow = 2, StartColumn = 5, EkspBool = False):
        self.row = StartRow
        self.column = StartColumn
        print('fcfs,make_xlsx_random, row = ',self.row, 'column = ', self.column, 'EkspBool = ', EkspBool)
        headers = ['number','arrival_time', 'burst_time', 'completed_time', 'turn_around_time', 'waiting_time']

        for col_num, header in enumerate(headers):
            self.wb_1.write(self.row-1, col_num+self.column, header)

        print('Po kalkulacji:')
        self.calculatings()


        self.sorted_pandas_numbers, self.sorted_pandas_arrival_time, self.sorted_pandas_burst_time, self.pandas_ct_array, self.pandas_tat_array, self.pandas_wt_array = self.Convert_to_pandas_nr_at_bt_ct_tat_wt(self.posortowane_procesy)

        counter = 0
        for key in self.posortowane_procesy[0].keys():

            self.wb_1.write(self.row, self.column+counter, key)
            counter+=1

        self.sum_completed_time = 0
        self.sum_turn_around_time = 0
        self.sum_burst_time = 0
        self.sum_waiting_time = 0
        for process in range(len(self.posortowane_procesy)):
            self.wb_1.write(self.row+process, self.column, self.posortowane_procesy[process]['number'])
            self.wb_1.write(self.row+process, self.column+1, self.posortowane_procesy[process]['arrival_time'])
            self.wb_1.write(self.row+process, self.column+2, self.posortowane_procesy[process]['burst_time'])
            self.sum_burst_time+=self.posortowane_procesy[process]['burst_time']
            self.wb_1.write(self.row+process, self.column+3, self.posortowane_procesy[process]['completed_time'])
            self.sum_completed_time+=self.posortowane_procesy[process]['completed_time']
            self.wb_1.write(self.row+process, self.column+4, self.posortowane_procesy[process]['turn_around_time'])
            self.sum_turn_around_time+=self.posortowane_procesy[process]['turn_around_time']
            self.wb_1.write(self.row+process, self.column+5, self.posortowane_procesy[process]['waiting_time'])
            self.sum_waiting_time+=self.posortowane_procesy[process]['waiting_time']
            self.wb_1.write(self.row+process, self.column+6, self.posortowane_procesy[process]['current_time'])
            if process == len(self.posortowane_procesy)-1:# wpisuje srednie wartosci
                self.avg_burst_Time = self.sum_burst_time/len(self.posortowane_procesy)
                self.avg_completed_time = self.sum_completed_time/len(self.posortowane_procesy)
                self.avg_turn_around_time = self.sum_turn_around_time/len(self.posortowane_procesy)
                self.avg_waiting_time = self.sum_waiting_time/len(self.posortowane_procesy)

                self.wb_1.write(self.row+process+1, self.column, 'AVG Values')
                self.wb_1.write(self.row+process+1, self.column+2, self.avg_burst_Time)
                self.wb_1.write(self.row+process+1, self.column+3, self.avg_completed_time)
                self.wb_1.write(self.row+process+1, self.column+4, self.avg_turn_around_time)
                self.wb_1.write(self.row+process+1, self.column+5, self.avg_waiting_time)
            headers = [ 'number', 'BT', 'CT', 'TAT', 'WT' ]
            for col_num, header in enumerate(headers):
                self.wb_1.write(1, col_num+57, header)
            self.wb_1.write(0, 57, 'FCFS')
            self.wb_1.write(0, 58, 'AVG Values')
            self.wb_1.write(len(self.posortowane_procesy)//50+2, 57, len(self.posortowane_procesy))
            self.wb_1.write(len(self.posortowane_procesy)//50+2, 58, self.avg_burst_Time)
            self.wb_1.write(len(self.posortowane_procesy)//50+2, 59, self.avg_completed_time)
            self.wb_1.write(len(self.posortowane_procesy)//50+2, 60, self.avg_turn_around_time)
            self.wb_1.write(len(self.posortowane_procesy)//50+2, 61, self.avg_waiting_time)
        self.posortowane_procesy = []
    def close_xlsl_file(self):
        self.wb_wej.close()
        self.wb.close()

    def Convert_to_pandas_nr_at_bt_ct_tat_wt(self, array):
        for process in array:

            self.sorted_number_array.append(process['number'])
            self.sorted_arrival_time_array.append(process['arrival_time'])
            self.sorted_burst_time_array.append(process['burst_time'])
            self.ct_array.append(process['completed_time'])
            self.tat_array.append(process['turn_around_time'])
            self.wt_array.append(process['waiting_time'])
        return self.sorted_number_array, self.sorted_arrival_time_array, self.sorted_burst_time_array, self.ct_array, self.tat_array, self.wt_array


