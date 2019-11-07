from multiprocessing import Pool
import os, time, random

def rand_time_task(name):
    print('Run process No_%s' % name)
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('process No_%s Run time is %0.2f' % (name, end - start))

if __name__ == '__main__':
    print('Parent process ID(%s)' % os.getpid())
    p = Pool(4)
    for i in range(8):
        p.apply_async(rand_time_task, args=(i,))
    p.close()
    p.join()
    print('all subprocesses done')

