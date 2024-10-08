import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
        number = []
        all_name_average = []
        with open(input_file_name) as Fin:
                reader = csv.reader(Fin)
                for row in reader:
                        for i in range(1,len(row)):
                                number.append(float(row[i]))
                        all_name_average.append([row[0],str(mean(number))])
                        del number
                        number = []
        with open(output_file_name,'w',newline='') as Finw:
                writer = csv.writer(Finw)
                for line in all_name_average:
                        writer.writerow(line)
        Finw.close()

def calculate_sorted_averages(input_file_name, output_file_name):
        number = []
        all_name_average = []
        dic = dict()
        with open(input_file_name) as Fin:
                reader = csv.reader(Fin)
                for row in reader:
                        for i in range(1,len(row)):
                                number.append(float(row[i]))
                        dic[mean(number)] = row[0]
                        all_name_average.append((mean(number)))
                        del number
                        number = []
                all_name_average.sort()
        with open(output_file_name,'w',newline='') as Finw:
                writer = csv.writer(Finw)
                for line in all_name_average:
                        writer.writerow([dic[line],str(line)])
        Finw.close()

def calculate_three_best(input_file_name, output_file_name):
        number = []
        all_name_average = []
        dic = dict()
        with open(input_file_name) as Fin:
                reader = csv.reader(Fin)
                for row in reader:
                        for i in range(1,len(row)):
                                number.append(float(row[i]))
                        dic[mean(number)] = row[0]
                        all_name_average.append((mean(number)))
                        del number
                        number = []
                all_name_average.sort(reverse = True)
        with open(output_file_name,'w',newline='') as Finw:
                for line in all_name_average[0:3]:
                        Finw.write(dic[line]+",")
                        Finw.write(str(line))
                        if (line != all_name_average[2]):
                                Finw.write("\n")                
        Finw.close()

def calculate_three_worst(input_file_name, output_file_name):
        number = []
        all_name_average = []
        dic = dict()
        with open(input_file_name) as Fin:
                reader = csv.reader(Fin)
                for row in reader:
                        for i in range(1,len(row)):
                                number.append(float(row[i]))
                        dic[mean(number)] = row[0]
                        all_name_average.append((mean(number)))
                        del number
                        number = []
                all_name_average.sort()
        with open(output_file_name,'w',newline='') as Finw:
                writer = csv.writer(Finw)
                for line in all_name_average[0:3]:
                        writer.writerow([str(line)])
        Finw.close()

def calculate_average_of_averages(input_file_name, output_file_name):
        number = []
        average = []
        with open(input_file_name) as Fin:
                reader = csv.reader(Fin)
                for row in reader:
                        for i in range(1,len(row)):
                                number.append(float(row[i]))
                        average.append(mean(number))
                        del number
                        number = []
        with open(output_file_name,'w',newline='') as Finw:
               Finw.write(str(mean(average)))
        Finw.close()


    