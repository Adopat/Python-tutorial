# 主要介绍jieba 分词的一些基本用法
# jieba 分词的三种模式
# 全模式  cut_all = True
# 精确模式 cut_all = False 默认是精确模式，可以不写
# 搜索引擎模式，在精确模式的基础上，对长词再次划分，提高召回率，适合用于搜索引擎分词
import jieba
import collections
print("======使用jieba分词中自定义的字典=========")
print("======全模式=====")
seg = jieba.cut("李小福是创新办主任也是云计算方面的专家",cut_all=True)
print("/".join(seg))
print("======精确模式=====")
seg = jieba.cut("李小福是创新办主任也是云计算方面的专家",cut_all=False) # 李小福/是/创新/办/主任/也/是/云/计算/方面/的/专家
print("/".join(seg))
print("======搜索引擎模式=====")
seg = jieba.cut_for_search("李小福是创新办主任也是云计算方面的专家")
print("/".join(seg))
print("======使用用户自定字典=========")
jieba.load_userdict("cidian1.txt")
seg=jieba.cut("李小福是创新办主任也是云计算方面的专家")
print("/".join(seg)) # 李小福/是/创新办/主任/也/是/云计算/方面/的/专家
print("======对文件内容进行分词并统计词频=======")
# 1. 创建停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath,'r',encoding='utf-8').readlines()]
    return stopwords
# 对句子进行分词
def seg_sentence(sentence):
    jieba.load_userdict("cidian1.txt") # 加载自定义字典
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist(r'hit_stopwords.txt')
    outstr = ""
    for word in sentence_seged:
        if word not in stopwords:
            if word!='\t':
                outstr +=word
                outstr +=" "
    return outstr
with open(r'唐探3.txt','r',encoding='utf-8') as f:
    for line in f:
        lien_seg = seg_sentence(line)
        with open(r'唐探3切词.txt','a',encoding='utf-8') as fq:
            fq.write(lien_seg)
# 统计切词后的词频
with open(r'唐探3切词.txt','r',encoding='utf-8') as f:
    # data = jieba.cut(f.read().replace('...','').replace('\n','').replace(" ",'').replace('，','').replace('。','').replace('\xa0',''))
    data = jieba.cut(f.read())
data = dict(collections.Counter(data).most_common(10))
print(data)


