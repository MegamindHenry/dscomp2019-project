import gzip
import progressbar

TOTAL_WORDS = 88952365

current_line = 0
corpus_total = gzip.open('en.wiki.tacl-compounds.txt.gz', 'rb')
corpus_1 = gzip.open('en_1.txt.gz', 'wb')
corpus_5 = gzip.open('en_5.txt.gz', 'wb')
corpus_25 = gzip.open('en_25.txt.gz', 'wb')
corpus_50 = gzip.open('en_50.txt.gz', 'wb')
corpus_100 = gzip.open('en_100.txt.gz', 'wb')

with progressbar.ProgressBar(max_value=TOTAL_WORDS) as bar:
    for l in corpus_total:

        if current_line < TOTAL_WORDS/100:
            corpus_1.write(l)

        if current_line < TOTAL_WORDS/20:
            corpus_5.write(l)

        if current_line < TOTAL_WORDS/4:
            corpus_25.write(l)

        if current_line < TOTAL_WORDS/2:
            corpus_50.write(l)

        if current_line < TOTAL_WORDS:
            corpus_100.write(l)

        # if current_line > TOTAL_WORDS/100 + 1:
        #     break

        bar.update(current_line)
        current_line += 1;

print(current_line)

corpus_total.close()
corpus_1.close()
corpus_5.close()
corpus_25.close()
corpus_50.close()
corpus_100.close()