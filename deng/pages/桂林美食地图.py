import streamlit as st
import pandas as pd
import numpy as np

st.title("🍲桂林美食探索🥢")
st.text("📷探索广西桂林最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置.")
shops_data = {
    "店铺名称": ["阿秀米粉", "李记阳朔啤酒鱼老店", "蒋记王城糯米饭", "油茶故里", "椿记烧鹅"],
    "特色美食": ["桂林米粉🍜", "🍺阳朔啤酒鱼🐟", "传统糯米饭🍙", "恭城油茶🧉", "烧鹅🦢"],
    "人均消费":[5,60,10,30,40],
    "评分": [4.5, 4.7, 4.6, 4.7, 4.8],
    "地址": ["七星区建干路", "象山区南环路", "秀峰区秀峰街道", "七星区龙隐园", "象山区中山中路"],
    "纬度": [25.277666, 25.268197, 25.275264, 25.263762, 25.268743],
    "经度": [110.312878, 110.290799, 110.299844, 110.303532, 110.289686],
    
}
shops_df = pd.DataFrame(shops_data)

months = [f"{i}月" for i in range(1, 13)]
price_data = {
    "月份": months,
"阿秀米粉": np.random.uniform(10, 20, 12),
    "李记阳朔啤酒鱼老店": np.random.uniform(80, 120, 12),
    "蒋记王城糯米饭": np.random.uniform(5, 10, 12),
    "油茶故里": np.random.uniform(15, 25, 12),
    "椿记烧鹅": np.random.uniform(30, 50, 12)
}
price_df = pd.DataFrame(price_data)
price_df.set_index("月份", inplace=True)

st.subheader("🚀桂林美食店铺信息")
st.dataframe(shops_df)

st.subheader("💰桂林美食店铺价格走势↗️↘️（12个月）")
st.line_chart(price_df)

st.subheader("⭐桂林美食店铺评分对比")
st.bar_chart(shops_df.set_index("店铺名称")["评分"])

sales_data = {
    "月份": months,
    "阿秀米粉": np.random.uniform(200, 300, 12),
    "李记阳朔啤酒鱼老店": np.random.uniform(100, 180, 12),
    "蒋记王城糯米饭": np.random.uniform(150, 250, 12),
    "油茶故里": np.random.uniform(80, 150, 12),
    "椿记烧鹅": np.random.uniform(60, 120, 12)
}
sales_df = pd.DataFrame(sales_data).set_index("月份")
st.subheader("✈️桂林美食店铺销量走势（面积图）")
st.area_chart(sales_df)

map_data = {
    'latitude':[25.277666,25.268197,25.275264,25.263762,25.268743],
    'longitude':[110.312878,110.290799,110.299844,110.303532,110.289686]
    }
st.map(pd.DataFrame(map_data))

