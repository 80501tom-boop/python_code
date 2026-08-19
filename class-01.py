# class:紅豆餅模板、藍圖、設計圖、無實體
# object:紅豆餅、房子、有實體

# 定義一個類別名為 Myclass、包含屬性(變數(int,float,str,list))、method(方法)/function(函式)
# 屬性，名詞、容器
# 方法，動詞、行為、功能
class Myclass:
    def __init__(self): # 初始化方法
      self.text = "ABC" # 字串屬性
    def clear(self): # 方法
      self.text = "" # 清空屬性
      
##############
obj = Myclass() # 建立物件
print(f'text: {obj.text}') # 取值
obj.text = "DEF" # 改值
print(f'text: {obj.text}') # 取值
obj.clear() # 呼叫方法
print(f'text: {obj.text}') # 取值