import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(page_title="ResearchMind", page_icon="🧠", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: radial-gradient(circle at 20% 0%, #1a1a1f 0%, #0e0e11 45%, #0a0a0c 100%);
    color: #e8e8ea;
}

.badge {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 999px;
    background: rgba(255, 106, 0, 0.12);
    color: #ff8a3d;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 18px;
    border: 1px solid rgba(255, 138, 61, 0.3);
}

.hero-title {
    font-size: 56px;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 6px;
}
.hero-title .accent {
    background: linear-gradient(90deg, #ff6a00, #ff9d4d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-sub {
    color: #9a9aa2;
    font-size: 16px;
    max-width: 640px;
    margin-bottom: 36px;
}

.section-label {
    color: #ff8a3d;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 6px;
    text-transform: uppercase;
}

.pipeline-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01));
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 16px 18px;
    margin-bottom: 12px;
    transition: all 0.2s ease;
}
.pipeline-card:hover {
    border-color: rgba(255, 138, 61, 0.4);
    transform: translateY(-1px);
}
.pipeline-card .step-num {
    color: #ff8a3d;
    font-weight: 800;
    font-size: 13px;
}
.pipeline-card .step-title {
    font-weight: 700;
    font-size: 15px;
    margin: 2px 0 4px 0;
}
.pipeline-card .step-desc {
    color: #8f8f97;
    font-size: 13px;
}

.stButton > button {
    background: linear-gradient(90deg, #ff6a00, #ff8a3d);
    color: #0a0a0c;
    font-weight: 700;
    border: none;
    border-radius: 10px;
    padding: 12px 0;
    font-size: 15px;
    box-shadow: 0 4px 20px rgba(255, 106, 0, 0.25);
}
.stButton > button:hover {
    box-shadow: 0 6px 26px rgba(255, 106, 0, 0.4);
    color: #0a0a0c;
}

.stTextInput > div > div > input {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px;
    color: #e8e8ea;
    padding: 12px;
}

.stTabs [data-baseweb="tab"] {
    color: #9a9aa2;
    font-weight: 600;
}
.stTabs [aria-selected="true"] {
    color: #ff8a3d !important;
}
</style>
""", unsafe_allow_html=True)

if "result" not in st.session_state:
    st.session_state.result = None

# ---------- Hero ----------
st.markdown('<div class="badge">MULTI-AGENT AI SYSTEM</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-title">Research<span class="accent">Mind</span></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="hero-sub">Four specialized AI agents collaborate — searching, scraping, '
    'writing, and critiquing — to deliver a polished research report on any topic.</div>',
    unsafe_allow_html=True,
)

col_main, col_side = st.columns([2, 1], gap="large")

with col_main:
    st.markdown('<div class="section-label">RESEARCH TOPIC</div>', unsafe_allow_html=True)
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Quantum computing breakthroughs in 2026",
        label_visibility="collapsed",
    )
    run_clicked = st.button("🔎  Run Research Pipeline", type="primary", disabled=not topic.strip(), use_container_width=True)

    examples = ["LLM agents 2025", "CRISPR gene editing", "Fusion energy progress"]
    st.markdown(
        "<div style='color:#6f6f78; font-size:12px; margin-top:14px;'>TRY</div>",
        unsafe_allow_html=True,
    )
    ex_cols = st.columns(len(examples))
    for c, ex in zip(ex_cols, examples):
        if c.button(ex, use_container_width=True, key=f"ex_{ex}"):
            topic = ex
            run_clicked = True

with col_side:
    st.markdown('<div class="section-label" style="font-size:14px;">Pipeline</div>', unsafe_allow_html=True)
    steps = [
        ("01", "Search Agent", "Gathers recent web information"),
        ("02", "Reader Agent", "Scrapes & extracts deep content"),
        ("03", "Writer Chain", "Drafts the full research report"),
        ("04", "Critic Chain", "Reviews & scores the report"),
    ]
    for num, title, desc in steps:
        st.markdown(f"""
        <div class="pipeline-card">
            <div class="step-num">{num}</div>
            <div class="step-title">{title}</div>
            <div class="step-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ---------- Run pipeline ----------
if run_clicked and topic.strip():
    status_box = st.status("Starting pipeline...", expanded=True)
    try:
        status_box.write("🔎 Search agent gathering sources...")
        status_box.write("📖 Reader agent scraping deep content...")
        status_box.write("✍️ Writer drafting the report...")
        status_box.write("🧐 Critic reviewing the report...")

        result = run_research_pipeline(topic)
        st.session_state.result = result
        status_box.update(label="Pipeline complete ✅", state="complete", expanded=False)
    except Exception as e:
        status_box.update(label="Pipeline failed ❌", state="error", expanded=True)
        st.error(f"Something went wrong: {e}")

# ---------- Results ----------
if st.session_state.result:
    result = st.session_state.result
    st.markdown("---")

    tab_report, tab_feedback, tab_search, tab_scraped = st.tabs(
        ["📄 Report", "🧐 Critic Feedback", "🔍 Search Results", "📚 Scraped Content"]
    )

    with tab_report:
        st.markdown(result.get("report", "No report generated."))

    with tab_feedback:
        st.markdown(result.get("feedback", "No feedback generated."))

    with tab_search:
        st.text(result.get("search_results", "No search results."))

    with tab_scraped:
        st.text(result.get("scraped_content", "No scraped content."))

    st.download_button(
        "⬇️  Download Report as Markdown",
        data=result.get("report", ""),
        file_name="research_report.md",
        mime="text/markdown",
    )
