from gensim.models import KeyedVectors

print('Loading models...')
wv_1 = KeyedVectors.load_word2vec_format('../trained_model/fasttext_all_vec_1.bin', binary=True)
print('Loaded model 1')

wv_5 = KeyedVectors.load_word2vec_format('../trained_model/fasttext_all_vec_5.bin', binary=True)
print('Loaded model 5')

wv_25 = KeyedVectors.load_word2vec_format('../trained_model/fasttext_all_vec_25.bin', binary=True)
print('Loaded model 25')

wv_50 = KeyedVectors.load_word2vec_format('../trained_model/fasttext_all_vec_50.bin', binary=True)
print('Loaded model 50')


print('Evaluate word analogies...')
a_1_semrel = wv_1.evaluate_word_analogies('analogy/en_sem-para_SemRel.txt')
a_1_mikolov = wv_1.evaluate_word_analogies('analogy/mikolov_analogies.txt')
print('Word Analogy 1 done')

a_5_semrel = wv_5.evaluate_word_analogies('analogy/en_sem-para_SemRel.txt')
a_5_mikolov = wv_5.evaluate_word_analogies('analogy/mikolov_analogies.txt')
print('Word Analogy 5 done')

a_25_semrel = wv_25.evaluate_word_analogies('analogy/en_sem-para_SemRel.txt')
a_25_mikolov = wv_25.evaluate_word_analogies('analogy/mikolov_analogies.txt')
print('Word Analogy 25 done')

a_50_semrel = wv_50.evaluate_word_analogies('analogy/en_sem-para_SemRel.txt')
a_50_mikolov = wv_50.evaluate_word_analogies('analogy/mikolov_analogies.txt')
print('Word Analogy 50 done')


print('Evaluate word similarity...')
s_1_luong = wv_1.evaluate_word_pairs('ws/luong_rare.txt')
s_1_ws = wv_1.evaluate_word_pairs('ws/ws353.txt')
print('Word Similarity 1 done')

s_5_luong = wv_5.evaluate_word_pairs('ws/luong_rare.txt')
s_5_ws = wv_5.evaluate_word_pairs('ws/ws353.txt')
print('Word Similarity 5 done')

s_25_luong = wv_25.evaluate_word_pairs('ws/luong_rare.txt')
s_25_ws = wv_25.evaluate_word_pairs('ws/ws353.txt')
print('Word Similarity 25 done')

s_50_luong = wv_50.evaluate_word_pairs('ws/luong_rare.txt')
s_50_ws = wv_50.evaluate_word_pairs('ws/ws353.txt')
print('Word Similarity 25 done')

with open('score_all.tsv', 'w+') as fp:
    fp.write('semrel_scores' + '\t')
    fp.write('mikolov_scores' + '\t')
    fp.write('luong_pearson_c' + '\t')
    fp.write('luong_pearson_p' + '\t')
    fp.write('luong_spearman_c' + '\t')
    fp.write('luong_spearman_p' + '\t')
    fp.write('ws_pearson_c' + '\t')
    fp.write('ws_pearson_p' + '\t')
    fp.write('ws_spearman_c' + '\t')
    fp.write('ws_spearman_p' + '\t')
    fp.write('\n')

    fp.write(str(a_1_semrel[0]) + '\t')
    fp.write(str(a_1_mikolov[0]) + '\t')
    fp.write(str(s_1_luong[0][0]) + '\t')
    fp.write(str(s_1_luong[0][1]) + '\t')
    fp.write(str(s_1_luong[1][0]) + '\t')
    fp.write(str(s_1_luong[1][1]) + '\t')
    fp.write(str(s_1_ws[0][0]) + '\t')
    fp.write(str(s_1_ws[0][1]) + '\t')
    fp.write(str(s_1_ws[1][0]) + '\t')
    fp.write(str(s_1_ws[1][1]) + '\t')
    fp.write('\n')

    fp.write(str(a_5_semrel[0]) + '\t')
    fp.write(str(a_5_mikolov[0]) + '\t')
    fp.write(str(s_5_luong[0][0]) + '\t')
    fp.write(str(s_5_luong[0][1]) + '\t')
    fp.write(str(s_5_luong[1][0]) + '\t')
    fp.write(str(s_5_luong[1][1]) + '\t')
    fp.write(str(s_5_ws[0][0]) + '\t')
    fp.write(str(s_5_ws[0][1]) + '\t')
    fp.write(str(s_5_ws[1][0]) + '\t')
    fp.write(str(s_5_ws[1][1]) + '\t')
    fp.write('\n')

    fp.write(str(a_25_semrel[0]) + '\t')
    fp.write(str(a_25_mikolov[0]) + '\t')
    fp.write(str(s_25_luong[0][0]) + '\t')
    fp.write(str(s_25_luong[0][1]) + '\t')
    fp.write(str(s_25_luong[1][0]) + '\t')
    fp.write(str(s_25_luong[1][1]) + '\t')
    fp.write(str(s_25_ws[0][0]) + '\t')
    fp.write(str(s_25_ws[0][1]) + '\t')
    fp.write(str(s_25_ws[1][0]) + '\t')
    fp.write(str(s_25_ws[1][1]) + '\t')
    fp.write('\n')

    fp.write(str(a_50_semrel[0]) + '\t')
    fp.write(str(a_50_mikolov[0]) + '\t')
    fp.write(str(s_50_luong[0][0]) + '\t')
    fp.write(str(s_50_luong[0][1]) + '\t')
    fp.write(str(s_50_luong[1][0]) + '\t')
    fp.write(str(s_50_luong[1][1]) + '\t')
    fp.write(str(s_50_ws[0][0]) + '\t')
    fp.write(str(s_50_ws[0][1]) + '\t')
    fp.write(str(s_50_ws[1][0]) + '\t')
    fp.write(str(s_50_ws[1][1]) + '\t')
    fp.write('\n')


