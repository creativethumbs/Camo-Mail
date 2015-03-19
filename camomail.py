import string
 
output = []
line_list = []
email_content = open('email.txt', 'r')
camo = open('output.txt', 'w')

for line in email_content: 
    line_list.append(line)

for i in range(len(line_list)): 
    currline = line_list[i] 
    for j in range(len(currline)):
        output.append(currline[j]) 
        if currline[j] != '\n':
            output.append(' ')

print ''.join(output)
