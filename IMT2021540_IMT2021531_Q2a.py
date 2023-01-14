from prettytable import PrettyTable
myTable=PrettyTable([' ','Always Taken','Always Not Taken'])
count_t=0
count_n=0
f=open('file.txt','r')
for i in f:
    s=i.split()
    if(s[1]=='T'):
        count_t+=1
    else:
        count_n+=1
ans1=round(count_t/(count_t+count_n)*100,2)
ans2=round(count_n/(count_t+count_n)*100,2)
myTable.add_row(['No. of mispredictions',count_n,count_t])
myTable.add_row(['Misprediction rate',ans2,ans1])
print("Total branches : {}".format(count_t+count_n))
print(myTable)
print("More accurate model is the \"Always Not Taken\" model")
//project ends
