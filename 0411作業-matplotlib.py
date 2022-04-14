
import numpy as np
import matplotlib.pyplot as plt # 匯入matplotlib 的pyplot 類別，並設定為plt
from matplotlib.font_manager import FontProperties # 中文字體

from PIL import ImageTk, Image
import matplotlib.image as mpimg                   # 匯入image 類別，並設定為 mpimg

# 換成中文的字體
# plt.rcParams['font.新細明體'] = ['SimSun'] # 步驟一（替換sans-serif字型）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

### 官方範例
#plt.style.use('_mpl-gallery')
# Covid 19 台北、新北、桃園地區4月份每日確診人數


# make data
date1=["4/1","4/2","4/3","4/4","4/5","4/6","4/7","4/8","4/9"]

TaipeiCase= [19,13,22,29,41, 84, 61, 74, 67]
TaipeiLabel="台北市"
NweTaipeiCase=[51,82,43,91,95,114,156,138,124]
NweTaipeiLabel="新北市"
TaoyuanCase= [22,25,15,13,10, 35, 30, 40, 40]
TaoyuanLabel="桃園市"



listDates1=[date1,date1,date1]
listCases1=[TaipeiCase,NweTaipeiCase,TaoyuanCase]
listLabels1=[TaipeiLabel,NweTaipeiLabel,TaoyuanLabel]


###########
# plot
fig, ax = plt.subplots(nrows=3, ncols=3,figsize=(10.24,7.68))   # 上下一份

# 1
n=0
while n<len(listDates1):
    ax[0,0].scatter( listDates1[n] ,
                  listCases1[n],
                  label=listLabels1[n])
    n=n+1
ax[0,0].legend()

# 2
n=0
while n<len(listDates1):
    ax[0,1].plot( listDates1[n] ,
                  listCases1[n],
                  label=listLabels1[n])
    n=n+1
ax[0,1].legend()

# 3
n=0
while n<len(listDates1):
    ax[0,2].bar( listDates1[n] ,
                  listCases1[n],
                  label=listLabels1[n])
    n=n+1
ax[0,2].legend()

# 4
n=0
while n<len(listDates1):
    ax[1,0].fill_between( listDates1[n] ,
                          listCases1[n],
                          label=listLabels1[n])
    n=n+1
ax[1,0].legend()

# 5
n=0
while n<len(listDates1):
    ax[1,1].stem( listDates1[n] ,
                  listCases1[n],
                  label=listLabels1[n])
    n=n+1
ax[1,1].legend()

# 6
n=0
while n<len(listDates1):
    ax[1,2].step( listDates1[n] ,
                  listCases1[n],
                  label=listLabels1[n])
    n=n+1
ax[1,2].legend()

# 7
n=0
while n<len(listDates1):
    ax[2,0].plot( listDates1[n] ,
                 listCases1[n],
                 label=listLabels1[n])
    n=n+1
ax[2,0].legend()

# 8
n=0
while n<len(listDates1):
    ax[2,1].plot( listDates1[n] ,
                 listCases1[n],
                 label=listLabels1[n])
    n=n+1
ax[2,1].legend()

# 9
n=0
while n<len(listDates1):
    ax[2,2].plot( listDates1[n] ,
                 listCases1[n],
                 label=listLabels1[n])
    n=n+1
ax[2,2].legend()





plt.show()
