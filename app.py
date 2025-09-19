import streamlit as st
import streamlit.components.v1 as components

# Sayfa yapılandırması
st.set_page_config(
    page_title="ALPEMİX - Donas Kurye Yönetim Sistemi",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HTML dosyasını oku ve Cloudflare scriptini kaldır
with open('alpemix.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Cloudflare scriptini kaldır (hata kaynağı)
html_content = html_content.split('<script>(function(){function c(){')[0]

# HTML içeriğini göster
components.html(html_content, width=None, height=3000, scrolling=True)

# CSS için ek stil
st.markdown("""
<style>
    /* Streamlit'in varsayılan stillerini gizle */
    .main > div {
        padding: 0;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Iframe içindeki içeriğin düzgün görünmesi için */
    iframe {
        border: none;
    }
</style>
""", unsafe_allow_html=True)
