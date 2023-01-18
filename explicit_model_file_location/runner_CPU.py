import os
from collections import OrderedDict
import subprocess

commands = OrderedDict()
commands['particlenet_AK4'] = "perf_analyzer -m particlenet_AK4 --percentile=95 -u localhost:8021 --shape pf_points:2,100 --shape pf_features:20,100 --shape pf_mask:1,100 --shape sv_points:2,10 --shape sv_features:11,10 --shape sv_mask:1,10 -i grpc --async -p 30000 --concurrency-range 4:4 -b"
commands['particlenet_AK4_TRT'] = "perf_analyzer -m particlenet_AK4_TRT --percentile=95 -u localhost:8021 --shape pf_points:2,100 --shape pf_features:20,100 --shape pf_mask:1,100 --shape sv_points:2,10 --shape sv_features:11,10 --shape sv_mask:1,10 -i grpc --async -p 30000 --concurrency-range 4:4 -b"
commands['particlenet_AK4_PT'] = "perf_analyzer -m particlenet_AK4_PT --percentile=95 -u localhost:8021 --shape pf_points__0:2,100 --shape pf_features__1:20,100 --shape pf_mask__2:1,100 --shape sv_points__3:2,10 --shape sv_features__4:11,10 --shape sv_mask__5:1,10 -i grpc --async -p 30000 --concurrency-range 4:4 -b"


outdir = "/output/"

for model, command in commands.items():
    outdir = f"/output/{model}_CPU"
    if not os.path.isdir(outdir):
        subprocess.run(f"mkdir -p {outdir}_CPU", shell=True)
    for batch in [1, 4, 8, 16, 32, 64, 128, 256]:
        tmp = command
        tmp += f" {batch} -f {outdir}_CPU/{model}_batch{batch}.csv"
        print(tmp)
        subprocess.run(f"{tmp}", shell=True)
