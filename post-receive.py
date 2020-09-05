#coding=utf-8
import requests
import subprocess
import configparser

config = configparser.ConfigParser()
# 讀取config
config.read('config.ini')

# 下git指令 (git show 取得最新一筆commit)
process = subprocess.Popen(['git', 'show', '-s', '--pretty=format:"%h - %an, %ar : %s"'], stdout=subprocess.PIPE)
output = process.communicate()[0].decode()

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

# 要傳送的訊息內容
project_name = config.get('line-notify', 'project_name')
message =  project_name + ' has been update. \n' + output
# 從config取得line notify權杖內容
token = config.get('line-notify', 'channel_access_token')

statusCode = lineNotifyMessage(token, message)
if statusCode == 200:
    print("done.")
else:
    print("errorCode" + str(statusCode))
