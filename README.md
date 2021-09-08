# iptokuni

## Description

IPアドレスを渡すと国名を出力するツール。サブネット形式で渡すと範囲内のIPを全て出力する。ローカルにGeoLite2のデータベースを置く必要があります。

## Setup

#### データベースを取得する

以下のサイトから「GeoLite2 City」のデータベースを取得し解凍しておく

https://dev.maxmind.com/geoip/geolite2-free-geolocation-data?lang=en

#### Usage

```
# 引数で渡す
$ python3 iptokuni.py 1.1.1.1
build_date: 2021-08-31 10:29:40
1.1.1.1: AU

# サブネット形式で渡す
$ python3 iptokuni.py 1.1.1.1/29
build_date: 2021-08-31 10:29:40
1.1.1.1: AU
1.1.1.2: AU
1.1.1.3: AU
1.1.1.4: AU
1.1.1.5: AU
1.1.1.6: AU

# ファイルで渡す
$ cat test.txt
1.1.1.1
8.8.8.8
11.22.33.44

$ cat test.txt | python3 iptokuni.py
build_date: 2021-08-31 10:29:40
1.1.1.1: AU
8.8.8.8: US
11.22.33.44: US
```
