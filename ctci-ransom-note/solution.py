def ransom_note(magazine, ransom):
    freq = {}
    for word in magazine:
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    for word in ransom:
        if word not in freq:
            return False
        if freq[word] <= 0:
            return False
        freq[word] -= 1
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
