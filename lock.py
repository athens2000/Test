def lock(data):
    final = []
    string = ""
    for alphabet in data:
        alphabet = ord(alphabet)
        temp = (alphabet+64)%127
        temp = chr(temp)
        final.append(temp)

    return(string.join(final))

def key(data):
    final = []
    string = ""
    for alphabet in data:
        alphabet = ord(alphabet)
        if (alphabet >=0 and alphabet < 64):
            alphabet = alphabet + 163
        if (alphabet >= 64 and alphabet < 127):
            alphabet = alphabet%64
        alphabet = chr(alphabet)
        final.append(alphabet)

    return(string.join(final))

    
d = lock("https://xhamster.com/videos/japanese-8859353#mlrelated")
k = key(d)
print(k)
        
