import keyword

import requests
import openpyxl

keyword = input("關鍵字")

wb = openpyxl.Workbook()
ws = wb.active

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'referer': 'https://www.104.com.tw/jobs/main/newestjob/?jobsource=index_hot_c&tab=job_2&utm_medium=cweb_keyword&utm_source=104'
}

for i in range(0,60,30):
    print(i)

    url = f'https://www.104.com.tw/jobs/search/api/jobs?hotJob=0&jobcat=2007001004%2C2013001006%2C2007001006&keyword={keyword}%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B&order=15'

    response = requests.get(url, verify=False, headers= header)

    print(response.json())
    json_data = response.json()
    for item in json_data['data']:
        print(item['jobName'])
        print(item['custName'])
        #print(item['description'])
        print(item['salaryLow'])
        if item['salaryLow'] ==0:
            print('面議')
        else:
            print(item['salaryLow'])
        #ws.append([item['jobName'], item['custName'], item['salaryLow']])
        print('=' * 100)
#wb.save('104.xlsx')