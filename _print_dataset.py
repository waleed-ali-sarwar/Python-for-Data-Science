# printing a built in data sets in Seaborn library
import seaborn as s

print_DataSets = s.get_dataset_names()

print(print_DataSets)

print_DataSets = s.load_dataset('car_crashes')
print(print_DataSets)