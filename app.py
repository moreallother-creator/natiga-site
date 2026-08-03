import streamlit as st
import pandas as pd

st.set_page_config(page_title="موقع النتيجة", layout="centered")

@st.cache_data
def load_data():
    # قراءة الملف المضغوط بصيغة zip مباشرة
    return pd.read_csv("natiga.zip", compression="zip")

try:
    df = load_data()

    st.title("🔍 الاستعلام عن النتيجة")
    
    # مربع البحث برقم الجلوس
    seating_no = st.text_input("أدخل رقم الجلوس:")

    if seating_no:
        # البحث عن رقم الجلوس
        result = df[df['seating_no'].astype(str) == seating_no.strip()]

        if not result.empty:
            st.success("تم العثور على النتيجة!")
            st.dataframe(result, use_container_width=True)
        else:
            st.error("رقم الجلوس غير موجود، التأكد من الرقم وحاول مرة أخرى.")

except Exception as e:
    st.error(f"حدث خطأ أثناء تحميل البيانات: {e}")