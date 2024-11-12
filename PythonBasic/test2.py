s = 'A4B3C4D7E9'
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        di = int(ch)
        output = output + x * di

print(output)