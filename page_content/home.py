import streamlit as st
from PIL import Image

def home_page():
    st.title("欢迎来到我的个人网站")
    
    # 创建两列布局
    col_left, col_right = st.columns([2, 1])  # 2:1 的宽度比例
    
    with col_left:
        # 添加个人简介
        st.header("姚昕潼")
        st.write("""
        以下是我的自我介绍）
        """)
    
    with col_right:
        # 添加个人照片
        try:
            image = Image.open('/Users/yaoxintong/Desktop/MKTG6037/04_personal_site_streamlit/static/images/image1.jpg')
            st.image(image, caption='', use_column_width=True)
        except FileNotFoundError:
            st.error("找不到图片文件")
    
    # 添加一些技能或专长
    st.header("专业技能")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("编程语言")
        st.write("- Python\n- R\n- SQL")
    
    with col2:
        st.subheader("数据分析")
        st.write("- 数据可视化\n- 统计分析\n- 机器学习")
    
    with col3:
        st.subheader("工具")
        st.write("- Streamlit\n- Pandas\n- Excel")