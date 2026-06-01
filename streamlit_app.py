import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="Streamlit 요소 가이드",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 제목
st.title("🎨 Streamlit 요소 가이드")
st.markdown("Streamlit의 주요 UI 요소들을 보여주는 예시 페이지입니다.")

# 사이드바
st.sidebar.title("📑 메뉴")
page = st.sidebar.radio(
    "보고 싶은 요소를 선택하세요:",
    ["텍스트 요소", "입력 요소", "데이터 표시", "차트 & 그래프", "미디어", "레이아웃", "기타"]
)

# 텍스트 요소
if page == "텍스트 요소":
    st.header("📝 텍스트 요소")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("제목과 텍스트")
        st.write("이것은 st.write()를 사용한 일반 텍스트입니다.")
        st.markdown("**st.markdown()** - 마크다운을 지원합니다!")
        st.markdown("- 리스트\n- 아이템\n- 구조")
        st.caption("이것은 작은 글씨의 캡션입니다.")
    
    with col2:
        st.subheader("강조 텍스트")
        st.success("✅ 성공 메시지")
        st.info("ℹ️ 정보 메시지")
        st.warning("⚠️ 경고 메시지")
        st.error("❌ 에러 메시지")

# 입력 요소
elif page == "입력 요소":
    st.header("⌨️ 입력 요소")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("기본 입력")
        text_input = st.text_input("텍스트 입력:", placeholder="텍스트를 입력하세요")
        if text_input:
            st.write(f"입력값: {text_input}")
        
        number_input = st.number_input("숫자 입력:", value=10, step=1)
        st.write(f"선택된 숫자: {number_input}")
        
        password = st.text_input("비밀번호:", type="password")
        if password:
            st.write("비밀번호가 입력되었습니다.")
    
    with col2:
        st.subheader("선택 요소")
        select_box = st.selectbox("드롭다운 선택:", ["옵션1", "옵션2", "옵션3"])
        st.write(f"선택됨: {select_box}")
        
        multi_select = st.multiselect("다중 선택:", ["A", "B", "C", "D"])
        st.write(f"선택된 항목들: {multi_select}")
        
        slider_val = st.slider("슬라이더:", 0, 100, 50)
        st.write(f"슬라이더 값: {slider_val}")
    
    st.subheader("기타 입력")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        checkbox = st.checkbox("체크박스를 체크하세요")
        st.write(f"체크됨: {checkbox}")
    
    with col2:
        radio_btn = st.radio("라디오 버튼:", ["선택1", "선택2", "선택3"])
        st.write(f"선택됨: {radio_btn}")
    
    with col3:
        color_val = st.color_picker("색상 선택:")
        st.write(f"선택된 색상: {color_val}")

# 데이터 표시
elif page == "데이터 표시":
    st.header("📊 데이터 표시")
    
    # 샘플 데이터 생성
    df = pd.DataFrame({
        "이름": ["Alice", "Bob", "Charlie", "David"],
        "나이": [25, 30, 35, 28],
        "도시": ["Seoul", "Busan", "Daegu", "Incheon"],
        "급여": [50000, 60000, 75000, 55000]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("테이블")
        st.write(df)
    
    with col2:
        st.subheader("데이터프레임 정보")
        st.dataframe(df, use_container_width=True)
    
    st.subheader("JSON 데이터")
    st.json({
        "이름": "Streamlit",
        "버전": "1.0+",
        "특징": ["빠른 개발", "Python 기반", "인터랙티브"]
    })
    
    st.subheader("메트릭")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("온도", "25 °C", "+2 °C")
    with col2:
        st.metric("습도", "60%", "-5%")
    with col3:
        st.metric("풍속", "10 km/h", "+1 km/h")

# 차트 & 그래프
elif page == "차트 & 그래프":
    st.header("📈 차트 & 그래프")
    
    # 샘플 데이터
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("라인 차트")
        st.line_chart(chart_data)
        
        st.subheader("바 차트")
        st.bar_chart(chart_data)
    
    with col2:
        st.subheader("에어리어 차트")
        st.area_chart(chart_data)
        
        st.subheader("스캐터 차트")
        scatter_data = pd.DataFrame(
            np.random.randn(100, 2),
            columns=['x', 'y']
        )
        st.scatter_chart(scatter_data)

# 미디어
elif page == "미디어":
    st.header("🎬 미디어")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("이미지")
        st.info("이미지는 URL 또는 로컬 파일로 표시할 수 있습니다.")
        st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", 
                width=200, caption="Streamlit 로고")
    
    with col2:
        st.subheader("오디오 & 비디오")
        st.info("오디오와 비디오는 URL로 표시할 수 있습니다.")
        audio_data = np.sin(2 * np.pi * np.linspace(0, 1, 200)) * 32767
        st.audio(audio_data.astype(np.int16), sample_rate=200)

# 레이아웃
elif page == "레이아웃":
    st.header("🎨 레이아웃 요소")
    
    st.subheader("컬럼 (Columns)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("첫 번째 컬럼")
        st.button("버튼 1")
    with col2:
        st.write("두 번째 컬럼")
        st.button("버튼 2")
    with col3:
        st.write("세 번째 컬럼")
        st.button("버튼 3")
    
    st.divider()
    
    st.subheader("탭 (Tabs)")
    tab1, tab2, tab3 = st.tabs(["탭 1", "탭 2", "탭 3"])
    with tab1:
        st.write("첫 번째 탭의 내용")
    with tab2:
        st.write("두 번째 탭의 내용")
    with tab3:
        st.write("세 번째 탭의 내용")
    
    st.divider()
    
    st.subheader("확장 박스 (Expander)")
    with st.expander("클릭하여 상세정보 보기"):
        st.write("숨겨진 콘텐츠가 여기에 있습니다!")
        st.write("텍스트, 입력 요소, 차트 등 모든 것을 포함할 수 있습니다.")

# 기타
elif page == "기타":
    st.header("🔧 기타 요소")
    
    st.subheader("버튼")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("일반 버튼"):
            st.success("버튼이 클릭되었습니다!")
    with col2:
        if st.button("다운로드 버튼", help="다운로드를 시작합니다"):
            st.info("파일 다운로드 중...")
    with col3:
        if st.button("삭제 버튼", type="primary"):
            st.warning("삭제되었습니다!")
    
    st.divider()
    
    st.subheader("진행률 바")
    progress = st.slider("진행률 설정:", 0, 100, 50)
    st.progress(progress / 100)
    
    st.divider()
    
    st.subheader("코드 표시")
    st.code("""
def hello_world():
    print("Hello, Streamlit!")
    
hello_world()
    """, language="python")
    
    st.divider()
    
    st.subheader("수식 (LaTeX)")
    st.latex(r"e^{i\pi} + 1 = 0")
    
    st.divider()
    
    st.subheader("분할선 (Divider)")
    st.write("위의 divider()를 사용했습니다.")
