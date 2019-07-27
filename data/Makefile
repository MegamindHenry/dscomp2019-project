output_1	:= fasttext_1
input_1		:= en1.txt
output_5	:= fasttext_5
input_5		:= en5.txt
output_25	:= fasttext_25
input_25	:= en25.txt
output_50	:= fasttext_50
input_50	:= en50.txt
output_100	:= fasttext_100
input_100	:= en100.txt

fasttext	:= ~/Documents/Github/fastText/fasttext

threads		:= 6

fasttext1:
	time $(fasttext) skipgram -input $(input_1) \
	-output $(output_1) -lr 0.05 -dim 300 -ws 10 \
	-neg 5 -loss ns -thread $(threads) -minCount 50 \
	-epoch 5 -t 1e-5 -minn 3 -maxn 6

fasttext5:
	time $(fasttext) skipgram -input $(input_5) \
	-output $(output_5) -lr 0.05 -dim 300 -ws 10 \
	-neg 5 -loss ns -thread $(threads) -minCount 50 \
	-epoch 5 -t 1e-5 -minn 3 -maxn 6

fasttext25:
	time $(fasttext) skipgram -input $(input_25) \
	-output $(output_25) -lr 0.05 -dim 300 -ws 10 \
	-neg 5 -loss ns -thread $(threads) -minCount 50 \
	-epoch 5 -t 1e-5 -minn 3 -maxn 6

fasttext50:
	time $(fasttext) skipgram -input $(input_50) \
	-output $(output_50) -lr 0.05 -dim 300 -ws 10 \
	-neg 5 -loss ns -thread $(threads) -minCount 50 \
	-epoch 5 -t 1e-5 -minn 3 -maxn 6

fasttext100:
	time $(fasttext) skipgram -input $(input_100) \
	-output $(output_100) -lr 0.05 -dim 300 -ws 10 \
	-neg 5 -loss ns -thread $(threads) -minCount 50 \
	-epoch 5 -t 1e-5 -minn 3 -maxn 6


