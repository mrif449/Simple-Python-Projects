import multiprocessing
import time

def cpu_bound_task():
    while True:
        pass

def measure_cpu_power():
    start_time = time.time()
    process_list = []
    num_cpus = multiprocessing.cpu_count()
    for i in range(num_cpus):
        p = multiprocessing.Process(target=cpu_bound_task)
        process_list.append(p)
        p.start()

    # run the task for 60 seconds
    time.sleep(60)

    # stop all processes
    for p in process_list:
        p.terminate()

    end_time = time.time()
    elapsed_time = end_time - start_time
    score = num_cpus * elapsed_time
    print("CPU Power Score: ", round(score,3))

if __name__ == '__main__':
    measure_cpu_power()


