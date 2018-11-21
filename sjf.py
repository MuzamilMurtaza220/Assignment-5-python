fp=open("data.txt","r")
all_records=fp.read()
arr=[]
arr=all_records.split("\n")
#print(arr)
p_name=[]
b_time=[]
for i in range(len(arr)):
    a,b,c=arr[i].split(" ")
    p_name.append(a)
    b_time.append(int(c))
print(p_name)
print(b_time)  
n=len(arr)   
#Below is the function to sort processes according to their burst time
def sort_processes():
    for i in range(0,len(b_time)-1): 
        for j in range(0,len(b_time)-i-1):
            if(b_time[j]>b_time[j+1]):
                temp=b_time[j]
                b_time[j]=b_time[j+1]
                b_time[j+1]=temp
                temp=p_name[j]
                p_name[j]=p_name[j+1]
                p_name[j+1]=temp
            #print(p_name[j])
sort_processes()
w_time=[]    
aw_time=0
ta_time=[] 
at_time=0 
w_time.insert(0,0)
ta_time.insert(0,b_time[0])
def find_all_times():
    aw_time=0
    at_time=0
    for i in range(1,len(b_time)):  
        w_time.insert(i,w_time[i-1]+b_time[i-1])
        ta_time.insert(i,w_time[i]+b_time[i])
        aw_time+=w_time[i]
        at_time+=ta_time[i]
    aw_time=float(aw_time)/n
    avg_turn_arount_time=float(at_time)/n
    print("\n")
    print("Process\t  Arrival Time\t Burst Time\t  Waiting Time\t  Turn Around Time")
    for i in range(0,n):
        print(str(p_name[i])+"\t\t"+"0\t\t" +str(b_time[i])+"\t\t"+str(w_time[i])+"\t\t"+str(ta_time[i]))
        #print("\n")
    print("Average Waiting time is: "+str(aw_time))
    print("Average Turn Arount Time is: "+str(at_time))
    print("-------------\nGant Chart:\n------------- ")
    print(str(w_time[0]), end = "")
    for i in range(len(arr)):
        print("-----" + str(ta_time[i]) + "(" + p_name[i] + ")", end = "")
    print("\n")
find_all_times()
