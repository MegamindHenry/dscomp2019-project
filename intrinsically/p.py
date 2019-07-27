from gensim.models import KeyedVectors

wv_50 = KeyedVectors.load_word2vec_format('../trained_model/fasttext_vec_1.bin', binary=True)
print('1111')

s_50_luong = wv_50.evaluate_word_pairs('ws/luong_rare.txt')
s_50_ws = wv_50.evaluate_word_pairs('ws/ws353.txt')
print('1111')

with open('score_222.tsv', 'w+') as fp:
    fp.write(str(s_50_luong[0][0]) + '\t')
    fp.write(str(s_50_luong[0][1]) + '\t')
    fp.write(str(s_50_luong[1][0]) + '\t')
    fp.write(str(s_50_luong[1][1]) + '\t')
    fp.write(str(s_50_ws[0][0]) + '\t')
    fp.write(str(s_50_ws[0][1]) + '\t')
    fp.write(str(s_50_ws[1][0]) + '\t')
    fp.write(str(s_50_ws[1][1]) + '\t')
    fp.write('\n')
print('1111')

wv_50_all = KeyedVectors.load_word2vec_format('../trained_model/fasttext_all_vec_1.bin', binary=True)
print('1111')


s_50_luong_all = wv_50_all.evaluate_word_pairs('ws/luong_rare.txt')
s_50_ws_all = wv_50_all.evaluate_word_pairs('ws/ws353.txt')
print('1111')

with open('score_all_222.tsv', 'w+') as fp:
    fp.write(str(s_50_luong_all[0][0]) + '\t')
    fp.write(str(s_50_luong_all[0][1]) + '\t')
    fp.write(str(s_50_luong_all[1][0]) + '\t')
    fp.write(str(s_50_luong_all[1][1]) + '\t')
    fp.write(str(s_50_ws_all[0][0]) + '\t')
    fp.write(str(s_50_ws_all[0][1]) + '\t')
    fp.write(str(s_50_ws_all[1][0]) + '\t')
    fp.write(str(s_50_ws_all[1][1]) + '\t')
    fp.write('\n')

print('1111')