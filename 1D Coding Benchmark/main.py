from math import ceil
import time
benchmarks = []
times = []
starts = time.time()
print("********************************")
print("*Welcome to 1D Coding Benchmark*")
print("********************************")
sample_run = int(input("Enter sample run count(1-5): "))
details = False
command1 = input("Like to see detailed report? (y/n): ")
if command1.lower() == "y":
    details = True
for x in range(sample_run):
    start = time.time()
    a = 0
    sample = 1000000
    for y in range(sample):
        a += 1
        print(" => ",end="\r")
        print(f"    Run:{x+1}> Completed: {'{:.2f}'.format(a/10000)}%",end="\r")
    end = time.time()
    result = end - start
    times.append(result)
    benchmark = (sample/result)
    benchmarks.append(benchmark)
ends = time.time()
total_time = "{:.0f}".format(ends-starts)
time = int(total_time)
hour = time // 3600
time %= 3600
minute = time // 60
time %= 60
seconds = time
final = "{:.0f}".format(sum(benchmarks)/sample_run)
if details == True:
    print("-----------------------------------------")
    for i in range(len(benchmarks)):
        print(f"Run-{i+1}:\n¯¯¯¯¯\nTime taken: {'{:.2f}'.format(times[i])}s\nResult: {'{:.0f}'.format(benchmarks[i])}\n")
    print("-----------------------------------------")
highest = benchmarks[0]
lowest = benchmarks[0]
for z in benchmarks:
    if z > highest:
        highest = z
    if z < lowest:
        lowest = z
if (len(benchmarks) == 1) or (len(benchmarks) == 2 and benchmarks[0] == benchmarks[1]):
    drop = 0
else:
    drop = "{:.2f}".format(100-((lowest/highest)*100))
print("☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐")
if hour > 0:
    print("☐Total time taken:", hour,"hour(s)",minute,"minute(s)",seconds,"second(s)")
elif minute> 0:
    print("☐Total time taken:", minute,"minute(s)",seconds,"second(s)")
else:
    print("☐Total time taken:", seconds,"second(s)")
print("☐Cummulative Benchmark Result:",final)
print(f"☐Highest Performance droped: {drop}%")
print("☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐")