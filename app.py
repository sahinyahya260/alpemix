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
def load_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"{file_path} dosyası bulunamadı.")
        return None
    except Exception as e:
        st.error(f"Dosya okuma hatası: {str(e)}")
        return None

# HTML içeriğini göster
def main():
    st.markdown("""
    <style>
        .main > div {
            padding: 0;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
    
    html_content = load_html_file('alpemix.html')
    
    if html_content:
        # Cloudflare scriptini kaldır (hata kaynağı)
        if '<script>(function(){function c(){' in html_content:
            html_content = html_content.split('<script>(function(){function c(){')[0]
        
        components.html(html_content, width=None, height=3000, scrolling=True)

if __name__ == "__main__":
    main()
