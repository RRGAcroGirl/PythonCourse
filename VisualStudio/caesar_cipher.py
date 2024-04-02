#alpha = "abcdefghijklmnopqrstuvwxyz"
#calpha = "fghijklmnopqrstuvwxyzabcde"
#cipher = {}
#for l in alpha:
#    cipher[l] = calpha[alpha.index(l)]
#print(cipher)

sentence = input("Please enter a sentence:")
sentence = sentence.lower()
cipher = {'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e'}
ans = ""
for l in sentence:
    ans += cipher.get(l,l)

print(ans)