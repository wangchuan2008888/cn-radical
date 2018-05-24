import pickle
import os
import six
from enum import Enum


class RunOption(Enum):
    Radical = 1
    Pinyin = 2


all_option = list(RunOption)


class Radical(object):
    _dictionary_file_name = 'dictionary.pickle'
    _dict_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

    def __init__(self, options):
        self.dictionary_file_name = os.path.join(self._dict_dir, self._dictionary_file_name)
        self.diction = None
        if options is None:
            options = RunOption.Radical
        self.options = self._format_options(options)

    @staticmethod
    def _format_options(options):
        if not isinstance(options, (list, tuple)):
            options = [options]
        rslt = []
        all_option_name = [op.name.lower() for op in all_option]
        for option in options:
            if option in all_option:
                rslt.append(option)
                continue
            if isinstance(option, six.string_types) and option.lower() in all_option_name:
                rslt.append(RunOption[option.capitalize()])
        return rslt

    def get_dict(self):
        dictionray = None
        with open(self.dictionary_file_name, 'rb') as f:
            dictionray = pickle.load(f)
        if dictionray is None:
            raise IOError('cannot find dictionary file {fname}'.format(fname=self.dictionary_file_name))
        for op in all_option:
            if op not in self.options:
                del dictionray[op.name.lower()]
        return dictionray

    def trans_ch(self, ch=''):
        """
        :param ch:待转换的单个字符
        :return: 转换的字符
        """
        if self.diction is None:
            self.diction = self.get_dict()
        if len(ch) > 1:
            raise Exception('this function used to transform single character. see trans_str')
        rslt = []
        for op in self.options:
            rslt.append(self.diction[op.name.lower()].get(ch))
        if len(rslt) == 1:
            rslt = rslt[0]
        return rslt

    def trans_str(self, _str=''):
        """
        :param _str:待转化的字符串
        :return: 转化后的字符串
        """
        if self.diction is None:
            self.diction = self.get_dict()
        rslt = []
        for op in self.options:
            join_str = self._get_join_str(op)
            rslt.append(join_str.join([self.diction[op.name.lower()].get(ch, ch) for ch in _str]))
        if len(rslt) == 1:
            rslt = rslt[0]
        return rslt

    @staticmethod
    def _get_join_str(op):
        if op == RunOption.Pinyin:
            return ' '
        else:
            return ''
