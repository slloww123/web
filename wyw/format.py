# coding=utf-8
# use --- to split paragraphs
# use | to split original & meaning each paragraphs

# example
# 子曰:「不仁者...」(《里仁》第四)
# |
# 孔子說:「沒有仁德的人...有智慧的人實行仁德。」
# ---
# 子曰:「富與貴...必於是。」(《里仁》第四)
# |
# 孔子說:「富有和顯貴...受挫折的時候也必定堅持仁德。」
# ---
# 顏淵問仁...請事斯語矣 14。」(《顏淵》第十二)
# |
# 顏淵問怎樣實行仁...請你允許我去實行這番話。」



from re import sub, split

filename = input('what name you create of the file(txt,md) :')

def longtoo(ori,tra):
    if len(ori) > len(tra):
        for index in range(len(tra)-1, len(ori)-1):
            tra.append('')
    elif len(tra) > len(ori):
        for index in range(len(ori)-1, len(tra)-1):
            ori.append('')
    print(len(ori),len(tra))

o = open('%s.txt'%(filename),'r',encoding='utf-8')
al = open('%s.md'%(filename),'w+',encoding='utf-8')
o_split = sub(r'\d+|\s+','',o.read())
o_split = o_split.replace('「','「\n')
o_split = o_split.replace(',','，')
o_split = o_split.replace('，','，\n')
o_split = o_split.replace('。','。\n')
o_split = o_split.replace(';','；')
o_split = o_split.replace('；','；\n')
o_split = o_split.replace('?','？')
o_split = o_split.replace('？','？\n')
o_split = o_split.replace('!','！')
o_split = o_split.replace('！','！\n')
o_split = o_split.replace('(','（')
o_split = o_split.replace('（','（\n')
o_split = o_split.replace(')','）')
o_split = o_split.replace('）','）\n')
o_split = o_split.replace('」','」\n')
# split para(o + t)
for paragra in split(r'-{3}', o_split):
    # split para(o , t)
    para = split(r'\|{1}', paragra)
    ori = para[0]
    tra = para[1]
    ori = split(r'\n', ori)
    tra = split(r'\n', tra)
    longtoo(ori, tra)
    for (indx, tra) in enumerate(tra):
        try:
            al.write('%s|%s  \n'%(ori[indx], tra))
        except:
            al.write('|%s  \n'%(tra))
    al.write('##  \n')
o.close()
al.close()