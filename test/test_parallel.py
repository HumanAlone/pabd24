import time
from multiprocessing import Pool
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
# endpoint = "http://127.0.0.1:5000/predict"
# endpoint = "http://149.154.70.253:8000/predict"
endpoint = "http://127.0.0.1:8080/predict"
HEADERS = {"Authorization": f"Bearer {config['APP_TOKEN']}"}


def do_request(params):
    area, mode, n = params
    data = {"area": area, "mode": mode, "n": n}
    t0 = time.time()
    resp = requests.post(endpoint, json=data, headers=HEADERS, timeout=45).text
    t = time.time() - t0
    return f"Waited {t:0.2f} sec " + resp


def test_10(mode, n):
    with Pool(10) as p:
        print(*p.map(do_request, [(i, mode, n) for i in range(10, 110, 10)]))


if __name__ == "__main__":
    modes = [("io", None), ("cpu", 5_000_000), ("multithread", 5_000_000)]
    for mode, n in modes:
        test_10(mode, n)
