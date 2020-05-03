import numpy as np

class CorpusTransformer:
    def __init__(self, corpus=None, segmentation=None):
        self.corpus = corpus
        self.words = set()
        self.maxlen = 0
        self.word_nums = 0
        self.seg = segmentation or self.simple_seg
        if corpus:
            self.fit_corpus(corpus)
            self.build_dict()

    def transform(self):
        return self.pad_sequence(self.corpus)

    def simple_seg(self, sent):
        return [ch for ch in sent]

    def fit_corpus(self, corpus):
        self.corpus = corpus
        for article in corpus:
            segs = self.seg(article)
            self.words |= set(segs)
            self.maxlen = max(self.maxlen, len(segs) + 2)

    def build_dict(self):
        words = ['[PAD]', '[BEG]', '[END]'] + list(self.words) + ['[UNK]']
        self.word_nums = len(words)
        idx = range(self.word_nums)
        self.w2i = dict(zip(words, idx))
        self.i2w = dict(zip(idx, words))
        self.unk = self.w2i['[UNK]']

    def get_idx(self, word):
        return self.w2i.get(word, self.unk)

    def get_word(self, idx):
        return self.i2w.get(idx, self.i2w[self.unk])

    def mk_sentence(self, seq, join_seg='', clear_pad=True, trim=True):
        seq = join_seg.join(list(map(self.get_word, seq)))

        if clear_pad:
            seq = seq.replace('[PAD]', '')

        if trim:
            seq = seq.replace('[END]', '')
            seq = seq.replace('[BEG]', '')

        return seq

    def mk_sequence(self, sent, tag_beg=False, tag_end=True):
        sent = self.seg(sent)

        if tag_beg:
            sent = ['[BEG]'] + sent

        if tag_end:
            sent += ['[END]']

        sent = list(map(self.get_idx, sent))
        return sent

    def pad_sequence(self, corpus, pad_right=False, tag_beg=False, tag_end=True):
        rtn_seq = np.zeros((len(corpus), self.maxlen), dtype=int)
        for i, article in enumerate(corpus):
            seq = self.mk_sequence(article, tag_beg=tag_beg, tag_end=tag_end)
            if pad_right:
                rtn_seq[i][-len(seq):] = seq
            else:
                rtn_seq[i][:len(seq)] = seq

        return rtn_seq

if __name__ == "__main__":
    corpus = [
        'Hello, today is a good day!',
        'Hi, I am Penut~',
        'Oh yeah, this is my favorite food.'
    ]
    ct = CorpusTransformer()
    ct.fit_corpus(corpus)
    ct.build_dict()
    seq = ct.mk_sequence('Hi, I am Penut! zzzzzz')
    print(seq)
    sent = ct.mk_sentence(seq)
    print(sent)
    seqs = ct.pad_sequence(corpus, pad_right=True)
    print(seqs)
