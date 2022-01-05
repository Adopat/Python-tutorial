# 批量重命名Excel 文件
import os
list1 = os.listdir('E:\\test_excel\\')
for i in list1:
    os.rename('E:\\test_excel\\'+i,'E:\\test_excel\\'+'AP BU_'+i)