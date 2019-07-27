import matplotlib.pyplot as plt

data = {}
semrel = []
mikolov = []
ws_pearson = []
ws_spearman = []
luong_pearson = []
luong_spearman = []

semrel_all = []
mikolov_all = []
ws_pearson_all = []
ws_spearman_all = []
luong_pearson_all = []
luong_spearman_all = []

with open('../intrinsically/score.tsv', 'r') as fp:
    fp.readline()
    for l in fp:
        parts = l.strip().split('\t')
        semrel.append(float(parts[0]))
        mikolov.append(float(parts[1]))
        luong_pearson.append(float(parts[2]))
        luong_spearman.append(float(parts[4]))
        ws_pearson.append(float(parts[6]))
        ws_spearman.append(float(parts[8]))


with open('../intrinsically/score_all.tsv', 'r') as fp:
    fp.readline()
    for l in fp:
        parts = l.strip().split('\t')
        semrel_all.append(float(parts[0]))
        mikolov_all.append(float(parts[1]))
        luong_pearson_all.append(float(parts[2]))
        luong_spearman_all.append(float(parts[4]))
        ws_pearson_all.append(float(parts[6]))
        ws_spearman_all.append(float(parts[8]))



data['semrel'] = semrel
data['mikolov'] = mikolov
data['ws_pearson'] = ws_pearson
data['ws_spearman'] = ws_spearman
data['luong_pearson'] = luong_pearson
data['luong_spearman'] = luong_spearman

data['semrel sub-word'] = semrel_all
data['mikolov sub-word'] = mikolov_all
data['ws_pearson sub-word'] = ws_pearson_all
data['ws_spearman sub-word'] = ws_spearman_all
data['luong_pearson sub-word'] = luong_pearson_all
data['luong_spearman sub-word'] = luong_spearman_all

plt.plot(data['semrel'], label='semrel', color='g', linestyle=':')
plt.plot(data['semrel sub-word'], label='semrel sub-word', color='g', linestyle='-')

plt.plot(data['mikolov'], label='mikolov', color='y', linestyle=':')
plt.plot(data['mikolov sub-word'], label='mikolov sub-word', color='y', linestyle='-')

plt.plot(data['ws_pearson'], label='ws_pearson', color='r', linestyle=':')
plt.plot(data['ws_pearson sub-word'], label='ws_pearson sub-word', color='r', linestyle='-')

plt.plot(data['ws_spearman'], label='ws_spearman', color='b', linestyle=':')
plt.plot(data['ws_spearman sub-word'], label='ws_spearman sub-word', color='b', linestyle='-')

plt.plot(data['luong_pearson'], label='luong_pearson', color='c', linestyle=':')
plt.plot(data['luong_pearson sub-word'], label='luong_pearson sub-word', color='c', linestyle='-')

plt.plot(data['luong_spearman'], label='luong_spearman', color='m', linestyle=':')
plt.plot(data['luong_spearman sub-word'], label='luong_spearman sub-word', color='m', linestyle='-')

plt.xticks([0, 1, 2, 3], ['1%', '5%', '25%', '50%'])
plt.ylabel('Scores and Correlations')
plt.legend(fontsize='xx-small', loc='right', bbox_to_anchor=(1, 0.3))
# plt.show()
plt.savefig('score.png')