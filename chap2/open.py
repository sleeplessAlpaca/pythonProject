fp = open('note.txt', 'w')  # 打开文件write
print('hellow world 你好', file=fp)  # 输出
fp.close()  # 关闭文件
