from unittest import TestCase
from cnradical.radical import Radical, RunOption


class TestRadical(TestCase):
    def test_options(self):
        op_lists = [['radical', 'pinyin'],
                    ['Radical', 'pinyin'],
                    ['radical', 'Pinyin']]
        expact_op_obj_list = [RunOption.Radical, RunOption.Pinyin]
        for ops in op_lists:
            ops_obj = Radical._format_options(ops)
            self.assertListEqual(ops_obj, expact_op_obj_list)

    def test_options2(self):
        op_lists = [[RunOption.Radical, 'pinyin'],
                    ['Radical', RunOption.Pinyin]]
        expact_op_obj_list = [RunOption.Radical, RunOption.Pinyin]
        for ops in op_lists:
            ops_obj = Radical._format_options(ops)
            self.assertListEqual(ops_obj, expact_op_obj_list)

    def test_options3(self):
        op_lists = [[RunOption.Radical],
                    ['Radical'],
                    [RunOption.Pinyin],
                    ['pinyin']]
        expact_op_obj_list = [RunOption.Radical, RunOption.Radical, RunOption.Pinyin, RunOption.Pinyin]
        for ops, expact in zip(op_lists, expact_op_obj_list):
            ops_obj = Radical._format_options(ops)
            self.assertListEqual(ops_obj, [expact])

    def test_trans(self):
        trans = Radical('radical')
        rslt = trans.trans_ch('好')
        self.assertEqual(rslt, '女')

    def test_str_trans(self):
        trans = Radical('radical')
        rslt = trans.trans_str('你好')
        self.assertEqual(rslt, '亻女')

    def test_pinyin(self):
        trans = Radical('pinyin')
        rslt = trans.trans_ch('好')
        self.assertEqual(rslt, 'hǎo')

    def test_str_pinyin(self):
        trans = Radical('pinyin')
        rslt = trans.trans_str('你好')
        self.assertEqual(rslt, 'nǐ hǎo')

    def test_multi(self):
        trans = Radical(['radical', 'pinyin'])
        r, p = trans.trans_ch('好')
        self.assertEqual(p, 'hǎo')
        self.assertEqual(r, '女')
