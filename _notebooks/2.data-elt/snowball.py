from datetime import datetime
import requests
import pandas as pd


def get_stock(code):
    response = requests.get(
        "https://stock.xueqiu.com/v5/stock/chart/kline.json",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        },
        params=(
            ("symbol", code),
            ("begin", int(datetime.now().timestamp() * 1000)),
            ("period", "day"),
            ("type", "before"),
            ("count", "-5000"),
            ("indicator", "kline"),
        ),
        cookies={"xq_a_token": "328f8bbf7903261db206d83de7b85c58e4486dda",},
    )

    if response.ok:
        d = response.json()["data"]
        data = pd.DataFrame(data=d["item"], columns=d["column"])
        data.index = data.timestamp.apply(
            lambda _: pd.Timestamp(_, unit="ms", tz="Asia/Shanghai")
        )
        return data
    else:
        print("stock error")
