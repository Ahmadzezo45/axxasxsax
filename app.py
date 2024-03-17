import requests
from flask import *
app = Flask(__name__)
@app.route("/vf",methods=["GET"]) 
def check():
    number = str(request.args.get('num'))
    password = str(request.args.get('pas'))
    urlo = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
    hdo = {
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "x-agent-operatingsystem": "10.1.0.264C185",
    "clientId": "AnaVodafoneAndroid",
    "x-agent-device": "HWDRA-MR",
    "x-agent-version": "2022.1.2.3",
    "x-agent-build": "500",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "142",
    "Host": "mobile.vodafone.com.eg",
    "User-Agent": "okhttp/4.9.1"
    }
    datao = 'username='+number+'&password='+password+'&grant_type=password&client_secret=a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3&client_id=my-vodafone-app'
    setup = requests.post(urlo, headers=hdo, data=datao).json()
    token = setup['access_token']
    url7=f'https://web.vodafone.com.eg/services/dxl/ramadanpromo/promotion?@type=RamadanHub&channel=website&msisdn={number}'
    head6={
    'Host': 'web.vodafone.com.eg',
'Connection': 'keep-alive',
'msisdn': number,
'api-host': 'PromotionHost',
'Authorization': f'Bearer {token}',
'Content-Type': 'application/json',
'x-dtreferer': 'https://web.vodafone.com.eg/spa/portal/hub?error=login_required&state=0650be48-8504-42fe-a750-5ee60013b9bf',
'Accept': 'application/json',
'clientId': 'WebsiteConsumer',
'x-dtpc': '13$86271925_590h6vOCQDKJFUIKMHBHNJLAAVICFNVFVUIBFC-0e0',
'User-Agent': 'Mozilla/5.0 (Linux; Android 9; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.94 Mobile Safari/537.36',
'channel': 'WEB',
'Referer': 'https://web.vodafone.com.eg/spa/portal/hub'
    }
    jt=requests.get(url7,headers=head6).json()
    return jt

if __name__ ==  '__main__' :
	app.run(host= '0.0.0.0' , port=8080)