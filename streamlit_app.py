import streamlit as st

# 페이지 제목
st.title("👋 자기 소개 페이지")

# 프로필 섹션
st.header("프로필")

col1, col2 = st.columns([1, 2])

with col1:
    # 프로필 사진 (사용자가 자신의 사진 URL이나 경로로 변경 가능)
    st.image("https://via.placeholder.com/150", caption="프로필 사진", width=150)

with col2:
    st.subheader("이름: [여기에 이름을 입력하세요]")
    st.write("**직업:** [여기에 직업을 입력하세요]")
    st.write("**간단한 소개:** [여기에 자신을 소개하는 짧은 문장을 입력하세요. 예: 열정적인 데이터 과학자입니다.]")

# 기술 스킬 섹션
st.header("💻 기술 스킬")
skills = [
    "Python",
    "데이터 분석",
    "머신러닝",
    "Streamlit",
    "SQL",
    "Pandas",
    "NumPy"
]  # 이 리스트를 자신의 스킬로 변경하세요

for skill in skills:
    st.write(f"- {skill}")

# 경력 섹션
st.header("🏢 경력")
st.write("**회사명:** [회사 이름을 입력하세요]")
st.write("**직책:** [직책을 입력하세요]")
st.write("**기간:** [근무 기간을 입력하세요]")
st.write("**주요 업무:** [주요 업무를 간단히 설명하세요]")

# 추가 경력이 있다면 아래에 더 추가할 수 있어요
# st.write("**회사명2:** [회사2]")
# st.write("**직책2:** [직책2]")
# 등

# 학력 섹션
st.header("🎓 학력")
st.write("**학교:** [학교 이름을 입력하세요]")
st.write("**전공:** [전공을 입력하세요]")
st.write("**졸업년도:** [졸업년도를 입력하세요]")

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
st.header("📞 연락처")
st.write("**이메일:** [이메일 주소를 입력하세요]")
st.write("**LinkedIn:** [LinkedIn 프로필 링크]")
st.write("**GitHub:** [GitHub 프로필 링크]")
st.write("**포트폴리오:** [포트폴리오 사이트 링크, 있다면]")

# 사이드바 (추가 메뉴)
st.sidebar.title("메뉴")
st.sidebar.write("이곳에 추가 메뉴를 넣을 수 있어요.")
st.sidebar.write("- [프로젝트 보기]")
st.sidebar.write("- [블로그]")
st.sidebar.write("- [연락하기]")

# 푸터
st.markdown("---")
st.write("© 2024 [이름]. 모든 권리 보유.")
