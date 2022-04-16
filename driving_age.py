# 開車年齡判斷

driving = input('請問您有沒有汽車駕駛經驗')

if driving != '有' and driving != '沒有' :
    print('不要輸入"有"或"沒有"以外的答案')
    raise SystemExit

age = int(input('請問您的年齡'))

if driving == '有' :
    if 18 <= age :
        print('您沒有違法。')
    else:
        print('你犯了無照駕駛罪!')
elif driving == '沒有' :
    if 18 <= age :
        print('您怎麼不去考駕照呢?')
    else:
        print('再過幾年您就可以考了。')