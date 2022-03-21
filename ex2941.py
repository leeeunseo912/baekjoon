croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

sentence = input()

for i in croatia:
    sentence = sentence.replace(i,'*')

print(len(sentence))
