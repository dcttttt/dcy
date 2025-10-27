import streamlit as st

st.set_page_config(layout="wide")

st.set_page_config(page_title="羊族简历谱生成器", page_icon="❀", layout="wide")

st.title('喜气洋洋')

st.text("我是奇思妙想喜羊羊，青青草原我称王")

c1, c2 = st.columns([1, 2], gap='large')

with c1:
    
    st.header("喜羊羊的信息表单", anchor='introduction')
    st.caption('---')
    
    name = st.text_input('姓名：', autocomplete='name', value='喜羊羊')
    filmography = st.text_input('登场作品:', autocomplete='filmography', value='《喜羊羊与灰太狼》')
    contact = st.text_input('联系方式：', autocomplete='tel', value='青青草原羊村101号')
    email = st.text_input('邮箱：', autocomplete='email', value='xiyangyang@yangcun.com')
    dob = st.text_input('出生日期：', value='羊历3505年5月25日')
    
    st.text('性别')
    gender = st.radio(
        '选择性别',
        ['男', '女', '其他'],
        label_visibility='collapsed',
        index=0
    )
    
    st.text('学历')
    education = st.selectbox(
        '选择学历',
        ['幼稚园', '小学', '初中', '高中', '大学', '未知'],
        label_visibility='collapsed',
        index=4
    )
    
    languages = st.multiselect(
        '语言能力',
        ['中文', '英文', '韩语', '羊文', '日语'],
        ['中文', '羊文'],
        max_selections=2
    )
    
    skills = st.multiselect(
        '技能',
        ['唱歌', '跳舞', 'rap', '足球', '羽毛球','橄榄球','游泳','发明','手工','等等'],
        ['发明',],
        max_selections=999
    )
    
    combat_exp = st.slider(
        '战斗经验（年）',
        0, 50, (10, 20)
    )
    
    my_range = range(1, 100)
    creativity = st.select_slider(
        '奇思妙想蓄能ing', 
        options=my_range, 
        value=66
    )

    intro = st.text_area(
        label='个羊简介：', 
        placeholder='请输入个人简介',
        value='蓝蓝天空晴朗,青青草地也芳香,慢慢长大的小羊,一天一天更坚强,再多困难不怕,再多险阻也去闯,让美梦飞翔,奇思妙想聪明的小羊.'
    )

    best_time = st.time_input("每日联系本羊最佳时间段")


with c2:
    
    st.header("实时信息预览", anchor='preview')
    st.caption('---')
    
    
    st.subheader(name, divider='blue')
    
    info_col1, info_col2 = st.columns([1, 3])
    with info_col1:
        
        st.image("https://pic.baike.soso.com/ugc/baikepic2/0/ori-20210518153032-1224701089_png_602_540_410206.jpg/800", caption="喜羊羊头像", use_container_width=True)
    
    with info_col2:
        st.write(f"**登场作品**：{filmography}")
        st.write(f"**联系方式**：{contact}")
        st.write(f"**邮箱**：{email}")
        st.write(f"**出生日期**：{dob}")
        st.write(f"**性别**：{gender}")
        st.write(f"**学历**：{education}")
        st.write(f"**最佳联系时间**：{best_time}")
    
    st.caption('---')
    
    st.write("### 个羊简介")
    st.write(intro)
    
    st.caption('---')
    
    st.write("### 能力详情")
    skill_col1, skill_col2 = st.columns(2)
    
    with skill_col1:
        st.write("**语言能力**")
        for lang in languages:
            st.write(f"• {lang}")
        
        st.write("\n**战斗经验**")
        st.write(f"{combat_exp[0]}-{combat_exp[1]}年")
    
    with skill_col2:
        st.write("**掌握技能**")
        for skill in skills:
            st.write(f"• {skill}")
        
        st.write("\n**奇思妙想指数**")
        st.progress(creativity / 100)
        st.write(f"{creativity}分（满分100分）")
