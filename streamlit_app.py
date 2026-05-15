import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="자기소개",
    page_icon="👤",
    layout="wide"
)

# 제목
st.title("👤 자기소개")

# 탭 구분
tab1, tab2, tab3, tab4 = st.tabs(["소개", "관심사", "경력", "연락처"])

with tab1:
    st.header("안녕하세요!")
    st.write("""
    저는 구지원입니다. 교대에서 음악교육과를 전공했으며, 아이들을 좋아하고 가르치는 일을 좋아합니다.
    새로운 것을 배우고 도전하는 것을 즐기고 있습니다.
    이 페이지에서 제 소개, 관심사, 경력 등을 확인하실 수 있습니다.
    """)
    
    # 프로필 이미지 영역
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write("**프로필 사진**")
        st.write("(이미지 추가 예정)")
    with col2:
        st.write("**기본 정보**")
        st.write("- 이름: 구지원")
        st.write("- 직업: 초등학교 교사")
        st.write("- 거주지: 충북 청주")

with tab2:
    st.header("관심사")
    st.write("""
    관심 있는 분야나 취미를 소개해주세요.
    """)
    st.bullet_points = []
    # 관심사 항목들

with tab3:
    st.header("경력 및 경험")
    st.write("""
    학력, 경력, 프로젝트 등을 소개해주세요.
    """)
    # 경력 정보

with tab4:
    st.header("연락처")
    st.write("""
    연락 방법을 입력해주세요.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.write("- 이메일: gujiwon.music@gmail.com")
        st.write("- 전화: 010-1234-5678")
    with col2:
        st.write("- GitHub: github.com/gujiwon")
        st.write("- LinkedIn: linkedin.com/in/gujiwon")
