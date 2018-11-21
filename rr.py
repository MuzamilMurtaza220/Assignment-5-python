class process:

    arrivalTime = 0
    finishTime = 0
    burstTime = 0
    remaining_burstTime = 0
    startTime = 0
    processId = 0
    startAssign = False
    timeSlice = 0
    waitingTime = 0
    waitingInterrupt = 0
    saveTime = 0
    remaining_waitingTime = 0

    def __init__(self):
        arrivalTime = 0
        finishTime = 0
        burstTime = 0
        remaining_burstTime = 0
        startTime = 0
        processId = 0
        timeSlice = 0
        startAssign = False
        waitingTime = 0
        waitingInterrupt = 0
        saveTime = 0
        remaining_waitingTime = 0


def show_output_queue(queue, process_no):
    calTurnAround = 0
    print ("\nProcessID     Start Time    Finish Time   Turn Around Time ")
    size = queue.qsize()
    for index in range(size):

        Process = outputQueue.get()
        ProcessTurnAround = (Process.finishTime - Process.arrivalTime)
        calTurnAround += ProcessTurnAround
        print ("P", Process.processId, '       |     ', Process.startTime, "      |      "\
            , Process.finishTime, "      |      ", ProcessTurnAround)

    print ("\nThe average Turn Around time :", calTurnAround / process_no)
##############################################################################################################


def show_queue(queue):
    print ("ProcessID   Arrival Time   Burst Time   Slice Time   waiting Time   waiting Interrupt ")
    size = queue.qsize()
    for index in range(size):
        Process = readyQueue._get()
        print ("  P", Process.processId, "  |     ", Process.arrivalTime, "      |      ", Process.burstTime, \
            "     |      ", Process.timeSlice, "     |      ", Process.waitingTime, "     |      ",\
            Process.waitingInterrupt)
        readyQueue._put(Process)
##################################################################################################################


def take_input_save_in_queue(queue, time_slice, waiting_Interrupt, waiting_time,process_no):
    previous_arrival_t = 0
    for index in range(process_no):
        while 1:
            print ("Enter arrival time of process ", index+1, " :",)
            arrival_input = int(input())
            if 0 <= arrival_input >= previous_arrival_t:
                break

        while 1:
            print ("Enter burst time of process ", index+1, " :",)
            burst_input = int(input())
            if burst_input >= 0:
                break

        Process = process()
        Process.processId = index+1
        Process.arrivalTime = arrival_input
        previous_arrival_t = arrival_input

        Process.timeSlice = time_slice
        Process.burstTime = burst_input
        Process.remaining_burstTime = burst_input
        Process.waitingTime = waiting_time
        Process.remaining_waitingTime = waiting_time
        Process.waitingInterrupt = waiting_Interrupt
        queue.put(Process)
############################################################################################################


#readyQueue = Queue()
processes = 0
time_slice = 0
wait_Interrupt = 0
waiting_time = 0

while 1:
    processes = int(input('Enter no. of process :  '))
    if processes > 0:
        break
while 1:
    time_slice = int(input('Enter time slice :  '))
    if time_slice > 0:
        break
while 1:
    waiting_Interrupt = int(input('Enter I/O interrupt  :  '))
    if waiting_Interrupt > 0:
        break
while 1:
    waiting_time = int(input('Enter I/O wait  :  '))
    if waiting_time > 0:
        break

TotalProcesses = processes
take_input_save_in_queue(readyQueue, time_slice, waiting_Interrupt, waiting_time, processes)
show_queue(readyQueue)

outputQueue = Queue()
waitingQueue = Queue()
Time = 0
BurstTime_Calculate = 0
wait_Interrupt = 0

while 1:
    if processes is 0:
        break

    if readyQueue.qsize() is 0:
        while 1:

            size = waitingQueue.qsize()
            for index in range(size):
                wait_process = waitingQueue._get()
                if wait_process.saveTime + wait_process.waitingTime <= Time:
                    readyQueue._put(wait_process)
                else:
                    waitingQueue._put(wait_process)
            if readyQueue.qsize() > 0:
                break
            Time += 1

    running_process = readyQueue.get()
    wait_Interrupt = running_process.waitingInterrupt
    BurstTime_Calculate = 0

    while 1:
        if processes is 0:
            break

        if running_process.arrivalTime <= Time:

            if running_process.startAssign is False:

                running_process.startTime = Time
                running_process.startAssign = True

            if running_process.remaining_burstTime == BurstTime_Calculate:

                running_process.finishTime = Time
                outputQueue._put(running_process)
                processes -= 1
                break

            if wait_Interrupt == 0:

                running_process.saveTime = Time
                running_process.timeSlice -= BurstTime_Calculate
                running_process.remaining_burstTime -= running_process.waitingInterrupt
                waitingQueue._put(running_process)

                break

            if running_process.timeSlice is BurstTime_Calculate:
                size = waitingQueue.qsize()
                for index in range(size):
                    wait_process = waitingQueue._get()
                    if wait_process.saveTime + wait_process.waitingTime <= Time:
                        readyQueue._put(wait_process)
                    else:
                        waitingQueue._put(wait_process)

                update_burst = running_process.burstTime - running_process.timeSlice
                running_process.burstTime = update_burst
                running_process.waitingInterrupt -= running_process.timeSlice
                running_process.timeSlice = time_slice
                readyQueue._put(running_process)
                size = waitingQueue.qsize()
                break

            BurstTime_Calculate += 1
            wait_Interrupt -= 1
        Time += 1

show_output_queue(outputQueue,TotalProcesses)