import time
import multiprocessing

def Single_core_test():
    def worker(id):
        print("Preformance Test Running...")
        while True:
            # Keep the CPU core busy
            x = 2**30
            x = x**30

    if __name__ == "__main__":
        start_time = time.time()
        
        # Start a worker process
        p = multiprocessing.Process(target=worker, args=(1,))
        p.start()
        
        # Keep the main process busy for a certain time
        time.sleep(60)
        
        # Stop the worker process
        p.terminate()
        p.join()
        
        end_time = time.time()
        
        # Calculate the CPU performance score
        score = (end_time - start_time) / 60
        
        print(f"CPU performance score: {score}")


Single_core_test()