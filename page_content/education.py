import streamlit as st
from components.interactive import display_interactive_chart

def education_page():
    st.title("My Education")
    
    # 教育经历部分
    st.header("学历经历")
    
    # 使用卡片式布局展示教育经历
    with st.container():
        st.subheader("悉尼大学")
        st.write("硕士学位 · 市场营销")
        st.write("2023 - 2024")
        st.write("主要课程：数字营销、市场分析、消费者行为学")
    
    st.markdown("---")  # 分隔线
    
    with st.container():
        st.subheader("本科院校")
        st.write("学士学位 · 专业名称")
        st.write("2019 - 2023")
        st.write("主要课程：xxx、xxx、xxx")
    
    # 添加分隔线
    st.markdown("---")
    
    # 添加交互式数据可视化部分
    st.header("数据分析技能展示")
    display_interactive_chart()