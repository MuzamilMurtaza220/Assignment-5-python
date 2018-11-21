fp=open("pri.txt","r")
all_records=fp.read()
arr=[]
arr=all_records.split("\n")
#print(arr)
p_name=[]
b_time=[]
pri_list=[]
for i in range(len(arr)):
    a,b,c=arr[i].split(" ")
    p_name.append(a)
    b_time.append(int(b))
    pri_list.append(int(c))
print(p_name)
print(b_time)  
print(pri_list)
n=len(arr)
#print(n)
#....................................

ta_time=[]
w_time=[]
 #Below is the function to sort processes using their priority
def sort_using_pri():
    for i in range(0,len(pri_list)-1):
        for j in range(0,len(pri_list)-i-1):
            if(pri_list[j]>pri_list[j+1]):
                temp=pri_list[j]
                pri_list[j]=pri_list[j+1]
                pri_list[j+1]=temp
                temp=b_time[j]
                b_time[j]=b_time[j+1]
                b_time[j+1]=temp
                temp=p_name[j]
                p_name[j]=p_name[j+1]
                p_name[j+1]=temp
sort_using_pri() 
#Below is the function to initialize all time
def init_time_lists():
    w_time.insert(0,0)
    ta_time.insert(0,b_time[0])
    for i in range(1,len(p_name)):
        w_time.insert(i,w_time[i-1]+b_time[i-1])
        ta_time.insert(i,w_time[i]+b_time[i])

init_time_lists()
#Below is the function to print gantt chart
def get_print_chart():
    avg_ta_time=0
    avg_w_time=0
    for i in range(0,len(p_name)):
        avg_w_time=avg_w_time+w_time[i]
        avg_ta_time=avg_ta_time+ta_time[i]
        avg_w_time=float(avg_w_time)/n
        avg_w_time=float(avg_ta_time)/n
    print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
    for i in range(0,n):
        print(str(p_name[i])+"\t\t"+str(b_time[i])+"\t\t"+str(w_time[i])+"\t\t"+str(ta_time[i]))
        #print("\n")
    print("Average Waiting time is: "+str(avg_w_time))
    print("Average Turn Around Time is: "+str(avg_ta_time))
get_print_chart()