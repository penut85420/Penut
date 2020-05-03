import re

def parse_pos_seg(sent, split_return=False):
    segs = re.findall(' ?([^(]+)\((\w+)\)', sent, re.M)
    if split_return:
        seg = [s[0] for s in segs]
        pos = [s[1] for s in segs]
        return seg, pos
    return segs

if __name__ == "__main__":
    ss = '蘇東坡(Nb) 在(P) 中國(Nc) 歷史(Na) 上(Ng) ，(COMMACATEGORY) 是(SHI) 哪(Nep) 一(Neu) 個(Nf) 朝代(Na) 的(DE) 人(Na) ？(QUESTIONCATEGORY)'
    print(parse_pos_seg(ss))
    print(parse_pos_seg(ss, split_return=True))
