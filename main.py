faculty_file= open("grades.csv",'r')
all_class_line = faculty_file.readlines()
for class_line in all_class_line:
    loud_line = class_line.upper()
    class_and_name = loud_line.split(":")
    loud_line = loud_line.strip()
    print(class_and_name[:])
    print(" 'Students' names, gpas and their IDs")