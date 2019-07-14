import bz2
import progressbar

TOTAL_WORDS = 1868572496 # wc commond in terminal

current_line = 0
corpus_total = bz2.open('en.wikidump.bz2', 'rb')
corpus_1 = bz2.open('en.wikidump_1.bz2', 'wb')
corpus_5 = bz2.open('en.wikidump_5.bz2', 'wb')
corpus_25 = bz2.open('en.wikidump_25.bz2', 'wb')
corpus_50 = bz2.open('en.wikidump_50.bz2', 'wb')
corpus_100 = bz2.open('en.wikidump_100.bz2', 'wb')

with progressbar.ProgressBar(max_value=TOTAL_WORDS) as bar:
    for l in corpus_total:

        if current_line < TOTAL_WORDS/100:
            corpus_1.write(l)

        if current_line < TOTAL_WORDS/20:
            corpus_1.write(l)

        if current_line < TOTAL_WORDS/4:
            corpus_1.write(l)

        if current_line < TOTAL_WORDS/2:
            corpus_1.write(l)

        if current_line > TOTAL_WORDS/2 + 1:
            break

        bar.update(current_line)
        current_line += 1;

print(current_line)

corpus_total.close()
corpus_1.close()
corpus_5.close()
corpus_25.close()
corpus_50.close()
corpus_100.close()