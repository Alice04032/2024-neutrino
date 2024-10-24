import streamlit as st

st.title('NEUTRINO')
st.markdown('안녕하세요! 부산과학고등학교 유일 물리 동아리인 **NEUTRINO**입니다!')
st.write('저희는 위대한 물리학자들의 뒤를 이어 최고의 물리학자가 되는 것이 목표입니다.')
st.markdown('이번 **BSS 10회 openlab**에서 다양한 물리 실험들을 준비하였습니다.')
st.write('심화 기자재를 사용하는 부스부터 간단히 체험할 수 있는 부스까지 다양하게 준비하였으니 많은 기대 부탁드립니다.')

st.image("/Users/imskrr/Desktop/뉴트리노 2024 오픈랩/포스터 jpg/time table.png")
st.write("위의 사진은 테슬라코일과 루벤스튜브 시연 시간이니 참조해주시길 바라겠습니다.")
tab7, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["EVENTS!", "루벤스튜브", "라이덴병", "레이저를 피하라!", "히히 구슬 발사", "스트로브효과", "테슬라코일"])
with tab7:
    st.header("간식 쿠폰을 찾아라!")
    st.image("/Users/imskrr/Desktop/뉴트리노 2024 오픈랩/포스터 jpg/7.jpg", use_column_width=True)

with tab1:
    st.header("테슬라코일")
    st.image("/Users/imskrr/Desktop/뉴트리노 2024 오픈랩/포스터 jpg/5.jpg",  use_column_width=True)

with tab2:
    st.header("루벤스튜브")
    st.image("/Users/imskrr/Desktop/뉴트리노 2024 오픈랩/포스터 jpg/4.jpg", use_column_width=True)

with tab3:
    st.header("라이덴병")
    st.image("/Users/imskrr/Desktop/뉴트리노 2024 오픈랩/포스터 jpg/3.jpg",  use_column_width=True)

with tab4:
    st.header("레이저를 피하라!")
    st.image("/Users/imskrr/Desktop/뉴트리노 2024 오픈랩/포스터 jpg/2.jpg", use_column_width=True)
with tab5:
    st.header("히히 구슬 발사!")
    st.image("/Users/imskrr/Desktop/뉴트리노 2024 오픈랩/포스터 jpg/6.jpg", use_column_width=True)
with tab6:
    st.header("스트로브효과")
    st.image("/Users/imskrr/Desktop/뉴트리노 2024 오픈랩/포스터 jpg/1.jpg", use_column_width=True)
