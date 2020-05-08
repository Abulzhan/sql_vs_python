f=open('person.txt', encoding='utf-8')

content=f.read()
lines=content.split(('\n'))
cnt=0
for line in lines:
    tokens=line.split('\t')
    if int(tokens[2])>1978:


        print(tokens)

f.close()