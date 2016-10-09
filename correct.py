import enchant

d = enchant.Dict('en_US')


def corrections(x):
    x=x.encode('ascii','ignore')
    print "this is ->>>text  ",x," ",type(x)
    x=x.split("\n")

    for i in range(len(x)):
        if x[i]!='' and d.check(x[i])==False:
            x[i]=''
    while x.count(''):
        x.remove('')

    s=''
    for i in x:
        s+=i
    return s
