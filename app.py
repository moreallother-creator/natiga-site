import pandas as pd
import streamlit as st

st.set_page_config(page_title="نتيجة الثانوية العامة")
st.title("🎓 البحث عن النتيجة")

@st.cache_data
def load_data():
    return pd.read_excel("natiga.xlsx")

try:
    df = load_data()
    seat_num = st.text_input("أدخل رقم الجلوس:")

    if st.button("عرض النتيجة"):
        if seat_num:
            result = df[df["seating_no"].astype(str).str.strip() == seat_num.strip()]
            
            if not result.empty:
                name = result.iloc[0]["arabic_name"]
                score = result.iloc[0]["total_degree"]
                st.success(f"الاسم: {name}")
                st.info(f"المجموع: {score}")
            else:
                st.error("رقم الجلوس غير موجود!")
except Exception as e:
    st.error("حدث خطأ في قراءة البيانات، تأكد من ملف الإكسل.")
    