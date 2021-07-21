
import json
from fg import scan
import concurrent.futures

for i in range(0,255):
    for j in range(0,255):
        for k in range(0,255):
            for l in range(0,255):
                ip = f"{i}.{j}.{k}.{l}"
                with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                    for port in range(1,10000):
                        executor.submit(scan,ip,port)

                



    