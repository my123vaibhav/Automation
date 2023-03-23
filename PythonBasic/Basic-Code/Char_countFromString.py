s = 'nishant'
st=list(s)

for i in range(len(st)):
    count = 1
    for j in range(i + 1, len(st)):
        if st[i] == st[j]:
            count = count+1
            st[j] = '-'

    if count >= 1 and st[i] != '-':
        print('Char name: ', st[i], "count is :", count)
