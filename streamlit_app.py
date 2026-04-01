import streamlit as st

# 페이지 제목
st.markdown("<h1 style='text-align: center; color: #4CAF50; font-family: Georgia; font-size: 40px;'>👋 자기 소개 페이지</h1>", unsafe_allow_html=True)

# 프로필 섹션
st.header("프로필")

col1, col2 = st.columns([1, 2])

with col1:
    # 프로필 사진 (귀여운 여자 선생님 만화 캐릭터)
    st.image("https://cdn-icons-png.flaticon.com/512/2922/2922561.png", caption="프로필 사진", width=150)

with col2:
    st.subheader("이름: [서지형]")
    st.write("**직업:** [교사]")
    st.markdown("<p style='font-family: Georgia; font-size: 18px; color: #555;'>아이들을 사랑하는 열정적인 교사로, 교육을 통해 미래를 밝히는 꿈을 키우고 있습니다. 학생들의 잠재력을 믿고, 함께 성장하는 여정을 즐깁니다.</p>", unsafe_allow_html=True)

# 학력 섹션
st.header("🎓 학력")
st.write("**학교:** [한국대학교]")
st.write("**전공:** [영어]")
st.write("**졸업년도:** [2026]")

# 추가 학력이 있다면 아래에 더 추가
# st.write("**학교2:** [학교2]")

# 관심사 또는 취미 섹션 (선택사항)
st.header("🎨 관심사")
interests = [
    "데이터 시각화",
    "오픈소스 프로젝트",
    "여행",
    "독서"
]  # 자신의 관심사로 변경하세요

for interest in interests:
    st.write(f"- {interest}")

# 연락처 섹션
st.header("📞 02-3015-3333")
st.write("**이메일:** [seossam@sen.go.kr]")
st.write("**LinkedIn:** [LinkedIn 프로필 링크]")
st.write("**GitHub:** [GitHub 프로필 링크]")
st.write("**포트폴리오:** [포트폴리오 사이트 링크, 있다면]")

# 사이드바 (추가 메뉴)
st.sidebar.title("메뉴")
st.sidebar.write("이곳에 추가 메뉴를 넣을 수 있어요.")
st.sidebar.write("- [프로젝트 보기]")
st.sidebar.write("- [블로그]")
st.sidebar.write("- [연락하기]")
