word = input("").upper()
alpha = list(set(word))
count_list = []

for w in alpha:
    cnt = word.count(w)
    count_list.append(cnt)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    max_index = count_list.index(max(count_list))
    print(alpha[max_index])