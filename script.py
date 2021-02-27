import FindMattes as fm
import os
import time



SAMPLE_DIR = os.getcwd() + '/samples/'
OUT_DIR =  os.getcwd() + '/out/'
MODEL_DIR = os.getcwd() + '/models/'
TEMP_DIR = os.getcwd() + '/tmp/'
os.environ['TORCH_HOME'] = MODEL_DIR
os.environ['TEMP'] = TEMP_DIR
SIZE = 1000
for current_file in os.listdir(SAMPLE_DIR):
    if(current_file.endswith('.jpg')):
        t = time.perf_counter()
        out_filename = OUT_DIR + str(SIZE) + current_file 
        in_filename = SAMPLE_DIR + current_file
        fm.createMatte(in_filename, out_filename, SIZE)
        print(f"Done, took {time.perf_counter() - t} seconds")