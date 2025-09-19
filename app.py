import streamlit as st
import streamlit.components.v1 as components

# Sayfa yapılandırması
st.set_page_config(
    page_title="ALPEMİX - Donas Kurye Yönetim Sistemi",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HTML dosyasını oku
with open('alpemix.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# HTML içeriğini göster
components.html(html_content, width=None, height=2000, scrolling=True)

# CSS için ek stil (gerekirse)
st.markdown("""
<style>
    /* Streamlit'in varsayılan stillerini geçersiz kılmak için */
    .main > div {
        padding: 0;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)