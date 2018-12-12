import csv, sys

if (len(sys.argv) != 6):
    print("format: python3 join_csv.py OUT-FILE FILE-1 KEY-INDEX-1 FILE-2 KEY-INDEX-2")
    exit()

with open(sys.argv[2], 'rb') as file:

    reader = csv.reader(file, delimiter=",", quotechar='"')
    
    with open(sys.argv[4]) as file2:
        
        reader2 = csv.reader(file2, delimiter=",", quotechar='"')

        for a1 in reader:
            
            for a2 in reader2:
                a = reader[a1]
                aa = reader[a2]
                if a[int(sys.argv[3])] == aa[int(sys.argv[5])]:
                    
                    a.extend(aa[int(sys.argv[5])+1:])

                    with open(sys.argv[1], 'wb') as csvfile:
                        print(reader)
                        spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

                        spamwriter.writerow(a)
                        
                    continue


