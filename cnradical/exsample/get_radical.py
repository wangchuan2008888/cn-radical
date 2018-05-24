from cnradical import Radical, RunOption

radical = Radical(RunOption.Radical)
pinyin = Radical(RunOption.Pinyin)

input = '你好,今天早上吃饭了吗'
radical_out = [radical.trans_ch(ele) for ele in input]
pinyin_out = [pinyin.trans_ch(ele) for ele in input]
print(radical_out)
print(pinyin_out)

radical_out = radical.trans_str(input)
pinyin_out = pinyin.trans_str(input)
print(radical_out)
print(pinyin_out)