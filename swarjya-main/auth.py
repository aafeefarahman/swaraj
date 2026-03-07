import streamlit as st
from utils.auth import is_authenticated

# Page configuration with dark theme settings
st.set_page_config(
    page_title="Government Portal Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Updated CSS with orange gradient buttons and moved auth
dark_theme_css = """
<style>
    /* Dark theme color palette */
    :root {
        --primary-dark: #1a3e72;
        --primary-light: #2a5a8c;
        --secondary-dark: #121212;
        --secondary-light: #1e1e1e;
        --accent: #4d9fec;
        --text-primary: #f0f0f0;
        --text-secondary: #b0b0b0;
        --orange-gradient: linear-gradient(135deg, #FFA500 0%, #FF8C00 100%);
        --orange-gradient-hover: linear-gradient(135deg, #FF8C00 0%, #FF6B00 100%);
    }
    
    /* Main app background */
    .stApp {
        background-color: var(--secondary-dark);
        color: var(--text-primary);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: var(--secondary-light) !important;
        border-right: 1px solid #333;
    }
    
    /* Orange gradient buttons */
    .orange-btn {
        background: var(--orange-gradient) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    
    .orange-btn:hover {
        background: var(--orange-gradient-hover) !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(255, 140, 0, 0.2);
    }
    
    /* Auth buttons container */
    .auth-container {
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
        justify-content: center;
    }
    
    /* Rest of your existing CSS... */
    /* [Keep all your existing CSS styles below] */
</style>
"""
st.markdown(dark_theme_css, unsafe_allow_html=True)

# Sidebar navigation (simplified without auth)
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/1a3e72/ffffff?text=Gov+Logo", width=150)
    st.title("Portal Navigation")
    
    if is_authenticated():
        st.page_link("pages/1_🏠_Home.py", label="🏠 Dashboard", icon="🏠")
        st.page_link("pages/1_🏠_Home.py", label="🌐 Translation", icon="🌐")
        st.page_link("pages/1_🏠_Home.py", label="📑 Documents", icon="📑")
        st.page_link("pages/1_🏠_Home.py", label="ℹ️ About", icon="ℹ️")

# Main content area with auth buttons
st.title("Government Services Multilingual Portal")

# Auth buttons container at top right
if not is_authenticated():
    auth_col1, auth_col2 = st.columns([3, 1])
    with auth_col2:
        st.markdown("""
        <div class="auth-container">
            <a href="/Login" class="orange-btn" style="text-decoration:none; color:white;">🔑 Login</a>
            <a href="/Signup" class="orange-btn" style="text-decoration:none; color:white;">📝 Register</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

if is_authenticated():
    # Authenticated user view
    col1, col2 = st.columns([3, 1])
    with col1:
        st.success(f"Welcome back, {st.session_state.email}")
        st.markdown("""
        <div class="info-card">
            <h3>Translation Services</h3>
            <p style="color: var(--text-secondary);">
            Access government webpages and documents in your preferred language
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.page_link("pages/1_🏠_Home.py", label="➡️ Go to Translation Dashboard", icon="➡️")
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>Quick Actions</h4>
            <p style="color: var(--text-secondary);">• Recent translations</p>
            <p style="color: var(--text-secondary);">• Saved documents</p>
            <p style="color: var(--text-secondary);">• Language preferences</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Logout button with orange styling
        if st.button("🚪 Logout", key="logout_btn"):
            from utils.auth import logout
            logout()
            st.rerun()
else:
    # Public/guest view
    st.markdown("""
    <div class="info-card" style="padding: 2rem;">
        <h2 style="color: var(--accent);">Access Government Services in Your Language</h2>
        <p style="font-size: 1.1rem; color: var(--text-secondary);">
            Our portal provides real-time translation of government webpages and documents 
            to make services accessible to all citizens regardless of language barriers.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    features = [
        ("🌍", "Multilingual Access", "Supports 20+ official languages"),
        ("📄", "Document Translation", "Government forms and publications"),
        ("🔒", "Secure Portal", "Encrypted and government-certified")
    ]
    
    for idx, (icon, title, desc) in enumerate(features):
        with cols[idx]:
            st.markdown(f"""
            <div class="info-card">
                <h4>{icon} {title}</h4>
                <p style="color: var(--text-secondary);">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.info("Please login or register to access translation services")

# Footer
st.markdown("""
<div style="text-align: center; padding: 1rem; margin-top: 2rem; border-top: 1px solid #333;">
    <p style="color: var(--text-secondary);">© 2023 Government Services Portal | Accessibility | Privacy Policy</p>
</div>
""", unsafe_allow_html=True)