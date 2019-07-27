English Nominal Compounds Dataset for Compositionality Tests
------------------------------------------------------------

If you want to use this dataset for research purposes, please refer to the following sources:

- Stephen Tratz. 2011. Semantically-enriched parsing for natural language understanding. Ph.D. thesis, University of Southern California.
- Roland  Schäfer. 2015. Processing  and  querying large  web  corpora  with  the  COW14  architecture. In Proceedings of Challenges in the Management of Large Corpora 3 (CMLC-3),  Lancaster. UCREL, IDS.
- Roland Schäfer and Felix Bildhauer. 2012. Building Large Corpora from the Web Using a New Efficient  Tool  Chain. In Proceedings of the Eight International Conference on Language Resources and Evaluation (LREC’12),  pages 486–493, Istanbul, Turkey. European Language Resources Association (ELRA).
- Christiane Fellbaum. 1998. WordNet. Wiley Online Library.
- Corina Dima, Daniël de Kok, Neele Witte, Erhard Hinrichs. 2019. No word is an island — a transformation weighting model for semantic composition. Transactions of the Association for Computational Linguistics.

The 16,978 English nominal compounds (11,824 train, 3,481 test, 1,673 dev) were extracted from an existing compound dataset (Tratz, 2011). Additionally, a selection of nominal compounds from the English WordNet 3.1 was added. The train/test/dev files have the following format, single parts separated by space:

modifier head compound
(e.g. space center space_center) 

For results of different composition models on this dataset see Dima et al. (2019), No word is an island — a transformation weighting model for semantic composition.
The word embeddings were trained on a subcorpus of the ENCOW16AX treebank (Schäfer  and  Bildhauer, 2012;  Schäfer,  2015), which contains only sentences with a document quality of a or b. The final training corpus for the word embeddings contains 89.0M sentences and 2.2B tokens. The compounds that were separated by a space were merged into a single unit for the embedding training, by artificially connecting the two constituents via an underscore. The embeddings for the single words were trained on the remaining occurrences of the constituents.
If you’re using the dataset or word embeddings for research purposes, please refer to the sources mentioned above.
The word embeddings for all constituents and compounds in this dataset are stored in the word2vec format in encow-sample-compounds.bin. This format can be loaded by several packages (e.g. the gensim package of Řehůřek, Radim and Petr Sojka (2010)). The embeddings for the constituents and compounds were trained with the word2vec package using the skipgram model with negative sampling (Mikolov et al. 2013) with an embedding dimension of 200, symmetric window of 10, 25 negative samples per positive training instance and a sample probability threshold of 0.0001. The minimum frequency cut-off was set to 50 for all words and the vocabulary size amounts 270,940 words.                