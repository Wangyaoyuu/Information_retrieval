import json

Index={}
for i in open('tweets.txt'):
    dict = json.loads(i)
    array_text=(dict['text']).lower().split(" ")
    array_username=dict['userName'].lower().split(" ")
    array=array_text+array_username
    array=list(set(array))
    for j in range(len(array)):
        if(array[j] not in Index.keys()):
            Index[array[j]]=[]
        Index[array[j]].append(dict["tweetId"])

length={}
for i in Index.keys():
    Index[i].sort()
    length[i]=len(Index[i])


def And(str1,str2):
    first = list(Index[str1])
    second = list(Index[str2])
    third=and_sort(first,second)
    return third


def Or(str1,str2):
    first = list(Index[str1])
    second = list(Index[str2])
    third = or_sort(first, second)
    return third

def find(str):
    str=str.lower()
    array_str=str.split(" ")
    e=[]

    if(len(array_str)==3):
        if(array_str[1]=="and"):
            e=And(array[0],array[2])

        if(array_str[1]=="or"):
            e=Or(array[0],array[2])
    # A and B and C、A or B or C、(A and B) or C、(A or B) and C
    elif(len(array_str)==5):
        if("(" in array_str[0]):
            a=array_str[0].strip("(")
            b=array_str[2].strip(")")
            c=array_str[4]
            if(array_str[1]=="and"):
                d=and_sort(a,b)
                if(array_str[3]=="and"):
                    e=and_sort(d,c)
                elif(array_str[3]=="or"):
                    e=or_sort(d,c)
            elif(array_str[1]=="or"):
                d=or_sort(a,b)
                if (array_str[3] == "and"):
                    e = and_sort(d, c)
                elif (array_str[3] == "or"):
                    e = or_sort(d, c)

        elif(")" in array_str[4]):
            a = array_str[0]
            b = array_str[2].strip("(")
            c = array_str[4].strip(")")
            if (array_str[3] == "and"):
                d = and_sort(c, b)
                if (array_str[1] == "and"):
                    e = and_sort(d, a)
                elif (array_str[1] == "or"):
                    e = or_sort(d, a)
            elif (array_str[3] == "or"):
                d = or_sort(c, b)
                if (array_str[1] == "and"):
                    e = and_sort(d, a)
                elif (array_str[1] == "or"):
                    e = or_sort(d, a)

        else:
            A = length[array_str[0]]
            B = length[array_str[2]]
            C = length[array_str[4]]
            a = Index[array_str[0]]
            b = Index[array_str[2]]
            c = Index[array_str[4]]

            if(array_str[1]=="and"):
                if(A>=B):
                    if(B>=C):
                        d=and_sort(b,c)
                        e=and_sort(d,a)
                    elif(B<C):
                        if(A>=C):
                            d=and_sort(b,c)
                            e=and_sort(d,a)
                        elif(A<C):
                            d=and_sort(a,b)
                            e=and_sort(d,c)


                elif(A<B):
                    if (B >= C):
                        d=and_sort(b,c)
                        e=and_sort(a,d)
                    elif (B < C):
                        d=and_sort(a,b)
                        e=and_sort(c,d)

            elif(array_str[1]=="or"):
                if (A >= B):
                    if (B >= C):
                        d = or_sort(b, c)
                        e = or_sort(d, a)
                    elif (B < C):
                        if (A >= C):
                            d = or_sort(b, c)
                            e = or_sort(d, a)
                        elif (A < C):
                            d = or_sort(a, b)
                            e = or_sort(d, c)


                elif (A < B):
                    if (B >= C):
                        d = or_sort(b, c)
                        e = or_sort(a, d)
                    elif (B < C):
                        d = or_sort(a, b)
                        e = or_sort(c, d)
    return e



#https://www.cnblogs.com/LanTianYou/p/8976671.html
def or_sort(a, b):
    ret = []
    while len(a)>0 and len(b)>0:
        if a[0] <= b[0]:
            ret.append(a[0])
            a.remove(a[0])
        if a[0] >= b[0]:
            ret.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        ret += b
    if len(b) == 0:
        ret += a
    return ret

def and_sort(a, b):
    ret = []
    while len(a)>0 and len(b)>0:
        if(a[0] == b[0]):
            ret.append(a[0])
            a.remove(a[0])
            b.remove(b[0])
        elif a[0] < b[0]:
            a.remove(a[0])
        elif a[0] > b[0]:
            b.remove(b[0])
    return ret


answer=find("House and may and kill")
print(answer)
