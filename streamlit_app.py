import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 Streamlit 요소들 예시 페이지")

st.header("1. 텍스트 요소들")
st.write("이것은 `st.write()`로 작성된 일반 텍스트입니다.")
st.markdown("**이것은 `st.markdown()`으로 작성된 마크다운 텍스트입니다.**")
st.text("이것은 `st.text()`로 작성된 일반 텍스트입니다.")
st.code("""
def hello():
    print("Hello, Streamlit!")
""")

st.header("2. 입력 위젯들")
if st.button("버튼 클릭"):
    st.success("버튼이 클릭되었습니다!")

checkbox = st.checkbox("체크박스")
if checkbox:
    st.info("체크박스가 선택되었습니다.")

radio = st.radio("라디오 버튼 선택", ["옵션 1", "옵션 2", "옵션 3"])
st.write(f"선택된 라디오: {radio}")

select = st.selectbox("셀렉트박스 선택", ["항목 A", "항목 B", "항목 C"])
st.write(f"선택된 항목: {select}")

slider = st.slider("슬라이더", min_value=0, max_value=100, value=50)
st.write(f"슬라이더 값: {slider}")

text_input = st.text_input("텍스트 입력", placeholder="여기에 입력하세요")
st.write(f"입력된 텍스트: {text_input}")

text_area = st.text_area("텍스트 영역", height=100)
st.write(f"입력된 텍스트 영역: {text_area}")

st.header("3. 데이터 표시")
df = pd.DataFrame({
    '이름': ['Alice', 'Bob', 'Charlie'],
    '나이': [25, 30, 35],
    '점수': [85, 90, 95]
})
st.dataframe(df)
st.table(df)

st.header("4. 차트")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(chart_data)
st.bar_chart(chart_data)

st.header("5. 레이아웃 요소들")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("컬럼 1")
with col2:
    st.write("컬럼 2")
with col3:
    st.write("컬럼 3")

with st.expander("확장 가능한 섹션"):
    st.write("이 내용은 확장할 때 나타납니다.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)

st.header("6. 사이드바")
st.sidebar.title("사이드바")
st.sidebar.write("이것은 사이드바입니다.")
sidebar_select = st.sidebar.selectbox("사이드바 선택", ["옵션 X", "옵션 Y"])
st.sidebar.write(f"사이드바에서 선택된: {sidebar_select}")

st.header("7. 미디어 요소들")
st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit 로고")
st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-05.wav")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

st.header("8. 진행 표시줄과 상태")
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
st.success("완료되었습니다!")

st.header("9. 파일 업로드")
uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file is not None:
    st.write("업로드된 파일:", uploaded_file.name)

st.header("10. 다운로드 버튼")
st.download_button(
    label="샘플 데이터 다운로드",
    data=df.to_csv(index=False),
    file_name="sample_data.csv",
    mime="text/csv"
)
