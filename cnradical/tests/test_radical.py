from unittest import TestCase
from cnradical.radical import Radical, DictOption


class TestRadical(TestCase):
    def test_options(self):
        op_lists = [['radical', 'pinyin'],
                    ['Radical', 'pinyin'],
                    ['radical', 'Pinyin']]
        expact_op_obj_list = [DictOption.Radical, DictOption.Pinyin]
        for ops in op_lists:
            ops_obj = Radical._format_options(ops)
            self.assertListEqual(ops_obj, expact_op_obj_list)

    def test_options2(self):
        op_lists = [[DictOption.Radical, 'pinyin'],
                    ['Radical', DictOption.Pinyin]]
        expact_op_obj_list = [DictOption.Radical, DictOption.Pinyin]
        for ops in op_lists:
            ops_obj = Radical._format_options(ops)
            self.assertListEqual(ops_obj, expact_op_obj_list)

    def test_options3(self):
        op_lists = [[DictOption.Radical],
                    ['Radical'],
                    [DictOption.Pinyin],
                    ['pinyin']]
        expact_op_obj_list = [DictOption.Radical, DictOption.Radical, DictOption.Pinyin, DictOption.Pinyin]
        for ops, expact in zip(op_lists, expact_op_obj_list):
            ops_obj = Radical._format_options(ops)
            self.assertListEqual(ops_obj, [expact])

    def test_trans(self):
        trans = Radical('radical')
        rslt = trans.trans('好')
        self.assertEqual(rslt, '女')