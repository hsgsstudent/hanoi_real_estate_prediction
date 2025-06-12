Dự đoán giá đất tháng 5 :D 

-------

Cách crawl dữ liệu : cd vào mục data_price, sau đó sử dụng lệnh sau
```bash
scrapy crawl alonhadat -o ../data/demo.json --set FEED_EXPORT_ENCODING=utf-8
```

-------
Data gồm có 3 phần chính là train.csv, val.csv, test.csv có cùng phân bố, trong đó tập test sẽ không có price thật. Price thật được lưu trong file solution.csv

-------
Link kaggle contest để submit: https://www.kaggle.com/t/f683cdf9b9c80285bcdec807404e116f
