


contacts = []

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    header = lines.pop(0).split(',')
    # print(header)

    for line in lines:
        split_line = line.split(',')
        #print(split_line)
        contact = {}
        contact['name'] = split_line[0]
        contact['favorite color'] = split_line[1]
        contact['favorite fruit'] = split_line[2]
        contacts.append(contact)
print(contacts)







