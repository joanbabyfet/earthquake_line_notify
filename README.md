## About
通过 line notify 发送地震信息，藉由 LINE Notify 官方帐号发送给消息订阅者

## Feature

* 通过 line notify 机器人实现消息通知
* 采集地震信息, 接口以 https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=CWB-66ECD273-CA87-4B56-9F1E-BB49875601FE 为例
* 配置文件设置 token

## Requires
Python 3.11.0  
requests 2.28.1  
configparser 5.3.0  

## Usage
```
python main.py
```
![image](https://raw.githubusercontent.com/joanbabyfet/md_img/master/earthquake_line_notify/display.jpg)

## Change Log
v1.0.0

## Maintainers
Alan

## LICENSE
[MIT License](https://github.com/joanbabyfet/earthquake_line_notify/blob/master/LICENSE)