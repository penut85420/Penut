import unittest

class PenutTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_timecost(self):
        import time
        from penut import TimeCost
        with TimeCost('Sleep Time'):
            time.sleep(1)
        ts = TimeCost('Custom Format', verbose_fmt=lambda msg, tts: f'Hello {msg}, you cost {tts:.2f}s!!')
        with ts:
            time.sleep(1)

    def test_io_test(self):
        import os
        import penut.io as pio

        # JSON IO
        def json_test(d):
            pio.dump(d, 'a.json', is_ascii=True)
            pio.dump(d, 'b.json', is_ascii=False)
            assert pio.load('a.json') == pio.load('b.json')

        # Pickle IO
        def pkl_test(d):
            pio.dump(d, 'a.pkl')
            assert d == pio.load('a.pkl')

        # Numpy IO
        def npy_test(d):
            import numpy as np
            d = np.array(d)
            pio.dump(d, 'a.npy')
            assert (d == pio.load('a.npy')).all()

        # CSV IO
        def csv_test(d):
            pio.dump(d, 'a.csv')
            pio.load('a.csv')

        # Cross Compare
        def cross_compare(d):
            pio.dump(d, 'a.json')
            pio.dump(d, 'a.pkl')
            assert pio.load('a.json') == pio.load('a.pkl')

        # Array Testing
        d = [1, 2, 3]
        json_test(d)
        print('JSON Array IO Pass')
        pkl_test(d)
        print('Pickle Array IO Pass')
        csv_test(d)
        print('CSV Array IO Pass')
        npy_test(d)
        print('Numpy Array IO Pass')
        cross_compare(d)
        print('Array IO Cross Comparison Pass')

        # Dictionary Testing
        d = {'Name': 'Testing', 'Arr': [1, 2, 3], '測試': '項目'}

        json_test(d)
        print('JSON Dict IO Pass')
        pkl_test(d)
        print('Pickle Dict IO Pass')
        csv_test(d)
        print('CSV Dict IO Pass')
        cross_compare(d)
        print('Dict IO Cross Comparison Pass')

        ## Remove Files
        os.remove('a.csv')
        os.remove('a.pkl')
        os.remove('a.npy')
        os.remove('a.json')
        os.remove('b.json')

    def test_walk_dir(self):
        from penut import walk_dir

        for fp in walk_dir('./'):
            self.assertIs(type(fp), str)

        for fp, fn in walk_dir('./', True):
            self.assertIs(type(fp), str)
            self.assertIs(type(fn), str)

        for fp, fn, dn in walk_dir('./', True, True):
            self.assertIs(type(fp), str)
            self.assertIs(type(fn), str)
            self.assertIs(type(dn), str)

    def test_td2s(self):
        from penut import td2s
        import datetime as dt
        a = dt.datetime(2021, 1, 6, 11, 32, 23)
        b = dt.datetime(2021, 1, 7, 12, 38, 17)
        d = b - a
        print(td2s(d))
        fmt = lambda h, m, s: f'{h} 小時 {m} 分 {s} 秒'
        print(td2s(d, fmt=fmt))

if __name__ == "__main__":
    unittest.main()
