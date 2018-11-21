#Below is the function to count number of lines in file
def count_lines():
    temp=0
    fp=open("data.txt","r")
    while True :
        line = fp.readline()
        if ("" == line):
            break
        temp=temp+1
    return temp
#below is the function to get turnaround time of each process
def get_turn():
    count = count_lines()
    f = open("data.txt", "r")
    p = []
    for i in range(count):
        p.append(f.readline())

    #print(p)

    process_name = []
    arrival_time = []
    burst_time = []
    waiting_time = []
    turnaround_time = []
    wt = 0
    for i in range(count):
        a, b, c = p[i].split(" ")
        process_name.append(a)
        arrival_time.append(int(b))
        burst_time.append(int(c))
        waiting_time.append(int(wt))
        tat = int(c) + wt
        turnaround_time.append(int(tat))
        wt += int(c)
    # print(process_name)
    # print(arrival_time)
    # print(burst_time)
    # print(waiting_time)
    print("Process Name   " + "Arrival Time   " + "Burst Time   " + "Waiting Time   " + "Turnaround Time   ")
    for x in range(len(process_name)):
            print(process_name[x] + "\t\t" + str(arrival_time[x]) + "\t\t" + str(burst_time[x]) + "\t\t" + str(waiting_time[x])+ "\t\t" + str(turnaround_time[x]))
    print("\n")
    avg_wt = 0
    avg_tat = 0
    sum1 = sum2 = 0

    for i in range(count):
        sum1 += waiting_time[i]
        sum2 += turnaround_time[i]

    avg_wt = sum1/count
    avg_tat = sum2/count

    print("Average Waiting time: " + str(avg_wt))
    print("Average Turnaround time: " + str(avg_tat))


#count lines
counter=count_lines()
#print(counter)
p_list=[]
a_list=[]
b_list=[]    
fp1=open("data.txt","r") 
al=[]
#Below is the loop to add all processes in al list
for i in range(counter):
    al.append(fp1.readline())

#print(al)
#Below is the loop to add processes name,arrival time and burst in different lists.cl
for i in range(counter):
    a,b,c=al[i].split()
    p_list.append(a)
    a_list.append(b)
    b_list.append(c)

print(p_list)
print(a_list)
print(b_list)
a_list.sort()
#function to get current process id
def get_process(j):
    fpp1=open("data.txt","r")
    tt1=count_lines()
    for i in range(tt1):
        pl=[]
        aal=fpp1.readline();
        a,b,c=aal.split()
        if a_list[j]==b:
            return a
#function to get current process Burst time
def get_burst(j):
    fpp=open("data.txt","r")
    tt=count_lines()
    for var in range(tt):
        pl=[]
        aal=fpp.readline();
        a1,b1,c1=aal.split()
        if a_list[j]==b1:
            return c1
a_list.sort()
xx=counter
#function to print graph
def print_graph():
    for i in range(4):
        
        ii=int(a_list[i])
        x=int(get_burst(ii))
        #sum=sum+x;
        ss=str(get_process(ii))
        for j in range(x):
            print("* ",end="")
        print(ss,end="")
        print("(",end="")
        print(x,end="")
        print(")",end="")
    print("\n")
print("----------------------------\nBelow is the graph for FCFS\n----------------------------\n\n")
print_graph()   
print("--------------------------------------------------------\nBelow is the waiting time and turnaround time for FCFS\n--------------------------------------------------------\n\n") 
get_turn()        