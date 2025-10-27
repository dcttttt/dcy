import streamlit as st
import numpy as np
import pandas as pd
st.set_page_config(page_title="野原新之助 - 数字档案", layout="centered", initial_sidebar_state="collapsed")
st.markdown(
    """
    
    """,
    unsafe_allow_html=True
)
st.title("野原新之助 - 数字档案")
st.header("🚀 基础信息")
st.text("别名: 小新、新之助、马铃薯小鬼 (野原 しんのすけ)")
st.text("类型: 漫画塑造人物 | 身份:双叶幼稚园向日葵班学生")
st.text("居住地: 日本埼玉县春日部市")
st.text("人物关系: 野原广志(父亲)、野原美伢(母亲)、野原向日葵(妹妹)、金有民子(未婚妻) | 宠物: 小白🐶")
st.header("📊 技能矩阵")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="运动技能", value="92%", delta="↑3%")  # 滑雪游泳攀爬等
with col2:
    st.metric(label="生活能力", value="90%", delta="↑8%")  # 书写泡茶等
with col3:
    st.metric(label="才艺技能", value="88%", delta="↓3%")  # 跳舞钢琴等
st.header("🗓️ 任务日志")
data = {
    "上映日期": ["1993.07.24", "1994.04.23", "1995.04.15"],
    "对手": ["魔王", "白蛇党领袖蟒蛇伯爵", "黑云斋等"],
    "结果": ["打败魔王（乘坐时光机回到原来世界)", "粉碎阴谋", "解除危机"],
    "评级（综合网络评价）": ["★★★★", "★★★★★", "★★★★★"]
}
df = pd.DataFrame(data)
st.table(df)
st.header("💻 经典问候语台词代码")
code = """
import random
quotes = (
    "I'm not a kid!",
    "Super无敌小白鼠！",
    "You guys wait, I'll come to save you!",
    "It's me, Crayon Shin - chan, the strongest superman!",
    "Shiro, come and fight!",
    "Oh, this is really a troublesome thing!"
)
def get_random_quote():
    quote = random.choice(quotes)
    return quote
def main():
    while True:
        print(get_random_quote())
        repeat = input("Do you want to see another one? (y/n): ")
        if repeat.lower() != 'y':
            print("Thanks for using, goodbye!")
            breaks
if __name__ == "__main__":
    main()
"""
st.code(code, language="python")
st.markdown("---")
st.markdown("**最新剧集：**《蜡笔小新:灼热的春日部舞者》🌸   \n**最后更新：** 2025-10-18  \n**目前状态：** 在更 | 古灵精怪 | 随时抗压")
