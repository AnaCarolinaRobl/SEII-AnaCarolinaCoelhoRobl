import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    #csv_data = csv.reader(data_file)
    csv_data = csv.DictReader(data_file)

    #print(csv_data)
    #print(list(csv_data))

#Usando o reader
    # next(csv_data)
    # next(csv_data)
    # for line in csv_data:
    #     #print(line)
    #     if line['0'] == 'No Reward':
    #         break
    #     names.append(f"{line[0]} {line[1]}")

#Usando o DicReader
    next(csv_data)
    for line in csv_data:
        #print(item)
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'
html_output += '\n<ul>'
#print(html_output)

for name in names:
    #print(name)
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)