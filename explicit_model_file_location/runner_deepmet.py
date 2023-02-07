import os
from collections import OrderedDict
import subprocess

commands = OrderedDict()
#commands['deepmet'] = "perf_analyzer -m deepmet --percentile=95 -u localhost:8021 -i grpc --async -p 10000 --concurrency-range 4:4 --input-data zero -b"
commands['deepmet_trt'] = "perf_analyzer -m deepmet_trt --percentile=95 -u localhost:8021 -i grpc --async -p 10000 --concurrency-range 4:4 --input-data zero -b"

outdir = "/output/"

for model, command in commands.items():
    outdir = f"./{model}"
    if not os.path.isdir(outdir):
        subprocess.run(f"mkdir -p {outdir}", shell=True)
    for batch in [1, 2, 4, 8, 16, 32, 64, 128, 256]:
        tmp = command
        tmp += f" {batch} -f {outdir}/{model}_batch{batch}.csv"
        print(tmp)
        subprocess.run(f"{tmp}", shell=True)
