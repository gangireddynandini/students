def fun(rollno,name,crs='python',cnt='india',**marks):
    print('rollno:{}'.format(rollno))
    print('name:{}'.format(name))
    print('course:{}'.format(crs))
    tot=0
    for v,m in marks.items():
        print('\t{}\t{}'.format(v,m))
        tot=tot+m
    else:
        print('total marks:{}'.format(tot))
fun(1,'dff',eng=34,hin=30,mat=43)
fun(name='hj',rollno=3,marks=67)
