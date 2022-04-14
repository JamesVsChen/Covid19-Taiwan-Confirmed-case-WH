
import numpy as np
import matplotlib.pyplot as plt # 匯入matplotlib 的pyplot 類別，並設定為plt
from matplotlib.font_manager import FontProperties # 中文字體

from PIL import ImageTk, Image
import matplotlib.image as mpimg                   # 匯入image 類別，並設定為 mpimg

# 換成中文的字體
# plt.rcParams['font.新細明體'] = ['SimSun']        # 步驟一（替換sans-serif字型）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False         # 步驟二（解決座標軸負數的負號顯示問題）

### 官方範例
#plt.style.use('_mpl-gallery')

# Covid 19 台北、新北、桃園地區4月份每日確診人數

# make data
date1=["4/1","4/2","4/3","4/4","4/5","4/6","4/7","4/8","4/9","4/10","4/11"] # 日期list

TaipeiCase= [19,13,22,29,41, 84, 61, 74, 67,96,100]           # 台北list(每日確診人數)
TaipeiLabel="台北市"                                           # 台北標籤
NweTaipeiCase=[51,82,43,91,95,114,156,138,124,173,155]        # 新北list(每日確診人數)
NweTaipeiLabel="新北市"                                        # 新北標籤
TaoyuanCase= [22,25,15,13,10, 35, 30, 40, 40,35,30]           # 桃園ilst(每日確診人數)
TaoyuanLabel="桃園市"                                          # 桃園標籤



listDates1=[date1,date1,date1]                               # 日期list
listCases1=[TaipeiCase,NweTaipeiCase,TaoyuanCase]            # 每日確診人數list
listLabels1=[TaipeiLabel,NweTaipeiLabel,TaoyuanLabel]        # 各地標籤list


###########
# plot

fig, ax = plt.subplots(nrows=3, ncols=3,figsize=(10.24,7.68))  # 畫面切割3*3,畫面大小1024*768
plt.suptitle("Covid 19 台北、新北、桃園地區4月份每日確診人數",fontsize=20) # tittle

# 左上角圖表
n=0                                                         # Variable n=0
while n<len(listDates1):                                    # 迴圈
    ax[0,0].scatter( listDates1[n] ,                        # 分割第[0,0]的位置,scatter圖表,X= 日期
                  listCases1[n],                            # Y= 各地每日確診人數
                  label=listLabels1[n])                     # 各地名稱
    n=n+1                                                   # n+1 以利迴圈運作
ax[0,0].legend()                                            # 加入圖例
ax[0,0].set_title("scatter")                                # 子圖表標題

# 正上方圖表
n=0                                                         # Variable n=0
while n<len(listDates1):                                    # 迴圈
    ax[0,1].plot( listDates1[n] ,                           # 分割第[0,1]的位置,plt圖表,X= 日期
                  listCases1[n],                            # Y= 各地每日確診人數
                  label=listLabels1[n])                     # 各地名稱
    n=n+1                                                   # n+1 以利迴圈運作
ax[0,1].legend()                                            # 加入圖例
ax[0,1].set_title("plot")                                   # 子圖表標題

# 右上方圖表 有覆蓋問題須修正
n=0                                                         # Variable n=0
while n<len(listDates1):                                    # 迴圈
    ax[0,2].bar( listDates1[n] ,                            # 分割第[0,2]的位置,bar圖表,X= 日期
                listCases1[n],                              # Y= 各地每日確診人數
                alpha=0.8,                                  # 顏色淡化 0.8
                label=listLabels1[n])                       # 各地名稱
    n=n+1                                                   # n+1 以利迴圈運作
ax[0,2].legend()                                            # 加入圖例
ax[0,2].set_title("bar")                                    # 子圖表標題

# 左邊中間圖表 有覆蓋問題須修正
n=0                                                         # Variable n=0
while n<len(listDates1):                                    # 迴圈
    ax[1,0].fill_between( listDates1[n] ,                   # 分割第[1,0]的位置,fill_between圖表,X= 日期
                          listCases1[n],                    # Y= 各地每日確診人數
                          alpha=0.8,                        # 顏色淡化 0.8
                          label=listLabels1[n])             # 各地名稱
    n=n+1                                                   # n+1 以利迴圈運作
ax[1,0].legend(loc="upper left")                            # 加入圖例 位置 upper left
ax[1,0].set_title("fill_between")                           # 子圖表標題

# 正中間圖表
n=0                                                         # Variable n=0
while n<len(listDates1):                                    # 迴圈
    ax[1,1].stem( listDates1[n] ,                           # 分割第[1,1]的位置,stem圖表,X= 日期
                  listCases1[n],                            # Y= 各地每日確診人數
                  label=listLabels1[n])                     # 各地名稱
    n=n+1                                                   # n+1 以利迴圈運作
ax[1,1].legend()                                            # 加入圖例
ax[1,1].set_title("stem")                                   # 子圖表標題

# 中間右邊圖表
n=0                                                         # Variable n=0
while n<len(listDates1):                                    # 迴圈
    ax[1,2].step( listDates1[n] ,                           # 分割第[1,2]的位置,step圖表,X= 日期
                  listCases1[n],                            # Y= 各地每日確診人數
                  label=listLabels1[n])                     # 各地名稱
    n=n+1                                                   # n+1 以利迴圈運作
ax[1,2].legend()                                            # 加入圖例
ax[1,2].set_title("step")                                   # 子圖表標題

# 左下角圖表(待更換圖表)
n=0                                                         # Variable n=0
while n<len(listDates1):                                    # 迴圈
    ax[2,0].plot( listDates1[n] ,                           # 分割第[2,0]的位置,scatter圖表,X= 日期
                 listCases1[n],"g--",                       # Y= 各地每日確診人數
                 label=listLabels1[n])                      # 各地名稱
    n=n+1                                                   # n+1 以利迴圈運作
ax[2,0].legend()                                            # 加入圖例
ax[2,0].set_title("plot_g--")                               # 子圖表標題

# 中間下面圖表(待更換圖表)
n=0                                                         # Variable n=0
while n<len(listDates1):                                    # 迴圈
    ax[2,1].plot( listDates1[n] ,                           # 分割第[0,0]的位置,scatter圖表,X= 日期
                 listCases1[n],"b*",                        # Y= 各地每日確診人數
                 label=listLabels1[n])                      # 各地名稱
    n=n+1                                                   # n+1 以利迴圈運作
ax[2,1].legend()                                            # 加入圖例
ax[2,1].set_title("plot_b*")                                # 子圖表標題

# 右下角圖表 (待更換圖表)
n=0                                                         # Variable n=0
while n<len(listDates1):                                    # 迴圈
    ax[2,2].plot( listDates1[n] ,                           # 分割第[0,0]的位置,scatter圖表,X= 日期
                 listCases1[n],"ro",                        # Y= 各地每日確診人數
                 label=listLabels1[n])                      # 各地名稱
    n=n+1                                                   # n+1 以利迴圈運作
ax[2,2].legend()                                            # 加入圖例
ax[2,2].set_title("plot_ro")                                # 子圖表標題


plt.show()

