Dự đoán giá đất tháng 5 :D 

-------
Cách crawl dữ liệu : 
```bash
scrapy crawl alonhadat -o ../data/demo.json --set FEED_EXPORT_ENCODING=utf-8
```

-------
Data gồm có 3 phần chính là train.csv, val.csv, test.csv có cùng phân bố, trong đó tập test sẽ không có price thật. Price thật được lưu trong file solution.csv
--------
File eda.ipynb đã được viết sẵn để tạo ra các ma trận X_train, X_val, X_test, y_train, y_val, cũng như cách sử dụng một số model cơ bản như linear_model, cũng như cách tạo file để submit kaggle. Mọi người khi code có thể copy file eda.ipynb, tạo ra các file ipynb cho từng model, sử dụng các ma trận X_train, X_val, X_test, y_train, y_val có sẵn để làm

-------
Link kaggle contest để submit: https://www.kaggle.com/t/f683cdf9b9c80285bcdec807404e116f
