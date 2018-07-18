#-*- coding=gbk -*-
import jieba
import os
import jieba.analyse
#��ȡÿ���ļ���txt��ȫ·��
def readfullnames(file_name):
    fullname_list=[]
    m=os.listdir(file_name)
    #print(m)
    for dir in os.listdir(file_name):
        for filename in os.listdir(file_name+"\\"+dir):
            #print(filename)
            fullname=file_name+"\\"+dir+"\\"+filename
            # print(fullname)
            fullname_list.append(fullname)
    return fullname_list
# def readfullnames():
#     fullname_list=[]
#     m=os.listdir('./testdata')
#     #print(m)
#     for dir in os.listdir('./testdata'):
#         print(dir)
#         for filename in os.listdir('./testdata'+"\\"+dir):
#             #print(filename)
#             fullname='./testdata'+"\\"+dir+"\\"+filename
#
#             fullname_list.append(fullname)
#     return fullname_list
#��ȡÿ���ļ��е��ֵ�·��
def readfillnames():
    fillname_list=[]
    for dir in os.listdir("./txt���"):
        fillname="./txt���\\"+dir+'\\'+dir+'.txt'
        if 'txt.txt' not in fillname:
            fillname_list.append(fillname)
    return fillname_list
#��ȡÿ���ļ��еĴ�Ƶ�ֵ�·��
def readcipin_fullnames():
    fillname_list=[]
    for dir in os.listdir("./txt���"):
        fillname="./txt���\\"+dir+"\\��Ƶ"+dir+".txt"
        if 'txt.txt' not in fillname:
            fillname_list.append(fillname)
    return fillname_list
#��ȡͣ�ôʱ�
def read_stopwords():
    stopwords_list=[]
    f1=open('./stopword.txt','r',encoding='gb18030')
    for line in f1.readlines():
        line=line.strip()
        stopwords_list.append(line)
    return stopwords_list
#д���ļ�������������Ӧ���ļ����ֵ�
def write_words(words_dic,dfs):
    for k in words_dic.items():
        st=''.join(['%s : %s' %k])
        dfs.write(st)
        dfs.write('\n')
#txt ���зִʣ�ͳ�ƴ�Ƶ����������ֵ�ʹ�Ƶ�ֵ�д��ÿ�����У�����Ϊtxt
#ͳ��ÿ�������еĴ��ڶ���ƪ�����г��֣����浽***��txt
def segfile(fullname_list):
    all_stopwords_list = read_stopwords()
    words_dic = {}
    all_words = {}
    name_temp = '��ʷ'
    for fullname in fullname_list:
        dfs = open("./txt���\\" + name_temp + '\\' + name_temp + '.txt', 'w', encoding='gb18030')  # ***.txt
        ddfs = open("./txt���\\" + name_temp + '\\��Ƶ' + name_temp + '.txt', 'w', encoding='gb18030')  # ��Ƶ***.txt
        dirname = fullname.split("/testdata\\")[1].split('\\')[0]
        if name_temp != dirname:
            write_words(words_dic, dfs)
            write_words(all_words, ddfs)
            words_dic.clear()
            all_words.clear()
            name_temp = dirname
        filename = fullname.split('\\')[-1]
        print(fullname + "==============")
        ifs = open(fullname, 'r', encoding='gb18030', errors='ignore')  # �ı��������Ͽ���ÿ�����е�txt
        ofs = open('./txt���\\' + dirname + '\\' + filename, 'w', encoding='gb18030')  # �ִʴ������ļ�д��txt
        words_tmp = []
        for line in ifs.readlines():
            line = line.strip()
            try:
                words = jieba.cut_for_search(line)
            except:
                continue
            for w in words:
                if w.strip() == '':
                    continue
                if w in all_stopwords_list:
                    continue
                if w.isdigit():
                    continue
                if w not in words_tmp:
                    words_tmp.append(w)
                if w not in all_words.keys():
                    all_words[w] = 1
                else:
                    all_words[w] += 1
                #print(w)
                ofs.write(w + ' ')
            ofs.write('\n')
        for t in words_tmp:
            if t not in words_dic.keys():
                words_dic[t] = 1
            else:
                words_dic[t] += 1
        ifs.close()
        ofs.close()
        dfs.close()
        ddfs.close()
    dfs = open('./txt���\\' + name_temp + '\\' + name_temp + '.txt', 'w', encoding='gb18030')  # ***��txt
    write_words(words_dic, dfs)
    dfs.close()
    ddfs = open('./txt���\\' + name_temp + '\\��Ƶ' + name_temp + '.txt', 'w', encoding='gb18030')  # ��Ƶ***.txt
    write_words(all_words, ddfs)
    ddfs.close()
#����ȡ���ֵ�ʹ�Ƶ�ֵ䣬ͳ�����ֵ�
def sumdic(fillname_list):
    dic={}
    fillname_list=readfillnames()
    for file in fillname_list:
        dfs=open(file,'r',encoding='gb18030',errors='ignore')
        for line in dfs.readlines():
            key=line.split(':')[0].strip()
            value=int(line.split(':')[-1].strip())
            if key not in dic.keys():
                dic[key]=value
            else:
                dic[key]+=value
    for t in list(dic.keys()):
        if dic[t]<8:
            del dic[t]
    afs=open('./txt�ֵ�.txt','w',encoding='gb18030')
    write_words(dic,afs)
    afs.close()
#ͳ���ܴ�Ƶ
def sumcipindic():
    cipin_dic={}
    cipin_fullnamelist=readcipin_fullnames()
    for file in cipin_fullnamelist:
        dfs=open(file,'r',encoding='gb18030',errors='ignore')
        for line in dfs.readlines():
            key=line.split(':')[0].strip()
            value=int(line.split(':')[-1].strip())
            if key not  in cipin_dic.keys():
                cipin_dic[key]=value
            else:
                cipin_dic[key]+=value
    afs=open('./txt��Ƶ�ֵ�.txt','w',encoding='gb18030')
    write_words(cipin_dic,afs)
    afs.close()

if __name__=='__main__':
    for dir in os.listdir('./testdata'):
        print(dir)
        if not os.path.exists('./txt���\\'+dir):
            os.mkdir('./txt���/'+dir)
    fullname_list=readfullnames()
    fillname_list=readfillnames()
    segfile(fullname_list)
    sumdic(fillname_list)
    sumcipindic()

