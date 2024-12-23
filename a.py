import requests

cookies = {
    'Hm_lvt_40639e2e855ad00c65304ee021f07859': '1734958819',
    'HMACCOUNT': 'E756515C7441AA0A',
    'Hm_lvt_42803e69eee56e1038e546a372218318': '1734958819',
    'HstCfa4903354': '1734958820800',
    'HstCmu4903354': '1734958820800',
    'HstCnv4903354': '1',
    'HstCns4903354': '1',
    'c_ref_4903354': 'https%3A%2F%2Fcn.bing.com%2F',
    'HstCla4903354': '1734959279269',
    'HstPn4903354': '2',
    'HstPt4903354': '2',
    'Hm_lpvt_42803e69eee56e1038e546a372218318': '1734959279',
    'Hm_lpvt_40639e2e855ad00c65304ee021f07859': '1734959279',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'Hm_lvt_40639e2e855ad00c65304ee021f07859=1734958819; HMACCOUNT=E756515C7441AA0A; Hm_lvt_42803e69eee56e1038e546a372218318=1734958819; HstCfa4903354=1734958820800; HstCmu4903354=1734958820800; HstCnv4903354=1; HstCns4903354=1; c_ref_4903354=https%3A%2F%2Fcn.bing.com%2F; HstCla4903354=1734959279269; HstPn4903354=2; HstPt4903354=2; Hm_lpvt_42803e69eee56e1038e546a372218318=1734959279; Hm_lpvt_40639e2e855ad00c65304ee021f07859=1734959279',
    'priority': 'u=0, i',
    'referer': 'https://cn.bing.com/',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

response = requests.get('https://www.ddyucshu.cc/19346_19346902/', cookies=cookies, headers=headers)

print(response.text)