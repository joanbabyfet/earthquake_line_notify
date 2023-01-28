import requests
import configparser

# 配置文件
config_file = 'config.ini'

# 发送信息
def send_message(text, img):
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='utf-8') # 这里要加utf-8, 否则会报错, 默认gbk
    config_section  = 'line_config'
    token   = conf.get(config_section, 'token') # 存取令牌

    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer ' + token
    }
    data = {
        'message': text,
        'imageThumbnail': img, # 预览图地址
        'imageFullsize': img, # 完整图片地址
        # 'stickerPackageId': '789', # 贴图包id
        # 'stickerId': '10863' # 贴图id
    }
    res = requests.post(url, headers = headers, data =  data)
    return res.json() # 成功返回 {'status': 200, 'message': 'ok'}

# 获取地震信息
def get_earthquake():
    ret = {} # 组装数据, 类型为字典

    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=CWB-66ECD273-CA87-4B56-9F1E-BB49875601FE'
    resp = requests.get(url)
    resp.encoding = 'utf-8' # 使用与网页相对应的编码格式, 避免乱码
    data = resp.json()
    location = data['records']['Earthquake'] # 字段大小写要区分, 否则获取到数据
    
    for index in range(len(location)):
        loc         = location[index]['EarthquakeInfo']['Epicenter']['Location'] # 地震地点
        magnitude   = location[index]['EarthquakeInfo']['EarthquakeMagnitude']['MagnitudeValue'] # 芮氏规模
        depth       = location[index]['EarthquakeInfo']['FocalDepth'] # 地震深度
        time        = location[index]['EarthquakeInfo']['OriginTime'] # 地震时间
        img_url     = location[index]['ReportImageURI'] # 图片
        break # 只获取第1条最新数据

    ret = {
        'loc': loc,
        'magnitude': magnitude,
        'depth': depth,
        'time': time,
        'img_url': img_url,
    }
    return ret

def main():
    try:
        status = 0
        info = get_earthquake() # 获取图片
        if info:
            msg = '%s，芮氏規模 %s 級，深度 %s 公里，發生時間 %s' % (
                info['loc'], info['magnitude'], info['depth'], info['time']
            )
            ret = send_message(msg, info['img_url'])
            if ret['status'] == 200:
                status = 1
        if status:
            print(f'地震信息通知成功')
        else:
            print(f'地震信息通知失败')
    except Exception as e:
        print(f'地震信息 {e} 通知失败')

if __name__ == '__main__': # 主入口
    main()
