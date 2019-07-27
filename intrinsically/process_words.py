def add_word(fp, words):
    for l in fp:
        parts = l.strip().split()
        words.add(parts[0])
        words.add(parts[1])

    return words


words = set()

luong = open('ws/luong_rare.txt' , 'r')
ws = open('ws/ws353.txt', 'r')
semrel = open('analogy/en_sem-para_SemRel.txt', 'r')
mikolov = open('analogy/mikolov_analogies.txt', 'r')
words = add_word(luong, words)
words = add_word(ws, words)
words = add_word(semrel, words)
words = add_word(mikolov, words)

with open('all_words.txt', 'w+') as fp:
    for w in words:
        fp.write(w)
        fp.write('\n')
