import csv

with open('names.csv', 'r') as csv_file:
    #csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file)


    with open('new_names.csv', 'w') as new_file:
        #fieldnames = ['first_name', 'last_name', 'email']
        fieldnames = ['first_name', 'last_name']

        #csv_writer = csv.writer(new_file, delimiter='-')
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        #next(csv_reader)

        for line in csv_reader:
            #print(line[2])
            del line['email']
            csv_writer.writerow(line)