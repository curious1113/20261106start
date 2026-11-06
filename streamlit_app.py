from html import escape

import streamlit as st


st.set_page_config(page_title="자기소개 | Personal Profile", page_icon="✳", layout="wide")

PROFILE = {
        "name": "이름을 입력하세요",
        "headline": "나를 설명하는 한 문장을 적어보세요.",
        "introduction": "관심 분야와 좋아하는 일, 중요하게 생각하는 가치를 소개해 주세요.",
        "affiliation": "학교 · 학과 또는 회사 · 팀",
        "location": "활동 지역을 입력하세요",
        "dream": "앞으로 이루고 싶은 목표와 그 이유를 적어보세요.",
        "email": "your.email@example.com",
        "career": [
                {"period": "2024 — 현재", "title": "현재 소속 또는 활동", "detail": "맡은 역할이나 배우고 있는 내용을 적어보세요."},
                {"period": "2022 — 2024", "title": "이전 경험 또는 프로젝트", "detail": "기억에 남는 성과와 경험을 적어보세요."},
                {"period": "2021", "title": "첫 번째 경험", "detail": "경력, 수상, 봉사, 동아리 활동 등을 적어보세요."},
        ],
}

career_items = "".join(
        f"""
        <article class="career-item">
            <p class="career-period">{escape(item['period'])}</p>
            <div>
                <h3>{escape(item['title'])}</h3>
                <p>{escape(item['detail'])}</p>
            </div>
            <span class="career-mark" aria-hidden="true">↗</span>
        </article>
        """
        for item in PROFILE["career"]
)

st.markdown(
        """
        <style>
            :root {
                --ink: #24221f;
                --paper: #f3f0e9;
                --line: #cbc6bd;
                --muted: #716d66;
            }
            [data-testid="stAppViewContainer"] { background: var(--paper); color: var(--ink); }
            [data-testid="stHeader"] { background: transparent; }
            .main .block-container { max-width: 1080px; padding: 3rem 2rem 2rem; }
            .profile-page { color: var(--ink); font-family: Arial, sans-serif; }
            .hero {
                background: var(--ink); color: var(--paper); padding: 2rem 2.4rem 1.4rem;
                min-height: 390px; display: flex; flex-direction: column; justify-content: space-between;
            }
            .eyebrow, .section-kicker, .hero-foot, .affiliation-label, .career-period {
                font-size: .75rem; letter-spacing: .12em; text-transform: uppercase;
            }
            .hero-top { display: flex; justify-content: space-between; border-bottom: 1px solid #625f59; padding-bottom: 1rem; }
            .hero-grid { display: grid; grid-template-columns: 1fr 190px; align-items: end; gap: 2rem; padding: 2.8rem 0; }
            .hero h1 { font-family: Georgia, serif; font-size: 4.2rem; line-height: 1.08; font-weight: 400; margin: .55rem 0 1rem; }
            .hero-lead { color: #d3cfc6; font-size: 1.05rem; max-width: 520px; line-height: 1.8; }
            .hero-index { height: 150px; border: 1px solid #77736b; display: flex; flex-direction: column; justify-content: space-between; padding: 1rem; }
            .hero-index strong { font-family: Georgia, serif; font-size: 5rem; line-height: 1; font-weight: 400; }
            .hero-index span, .hero-foot { color: #c4bfb5; }
            .hero-foot { display: flex; justify-content: space-between; border-top: 1px solid #625f59; padding-top: 1rem; }
            .content-section { padding: 5rem 0; border-bottom: 1px solid var(--line); }
            .section-kicker { color: var(--muted); margin: 0 0 1.4rem; }
            .section-title { font-family: Georgia, serif; font-size: 2.6rem; font-weight: 400; margin: 0 0 1.4rem; }
            .about-grid { display: grid; grid-template-columns: 1.4fr .8fr; gap: 5rem; }
            .about-copy { font-size: 1.12rem; line-height: 1.95; max-width: 620px; }
            .affiliation { border-top: 1px solid var(--ink); padding-top: 1.2rem; margin-top: .6rem; }
            .affiliation-label { color: var(--muted); margin: 0 0 .65rem; }
            .affiliation-value { font-family: Georgia, serif; font-size: 1.45rem; line-height: 1.5; margin: 0 0 1.7rem; }
            .dream-panel { background: var(--ink); color: var(--paper); padding: 3rem; margin: 4rem 0 0; }
            .dream-panel .section-kicker { color: #c4bfb5; }
            .dream-panel blockquote { border: 0; padding: 0; margin: 0; font-family: Georgia, serif; font-size: 2.3rem; line-height: 1.5; max-width: 800px; }
            .career-list { border-top: 1px solid var(--ink); }
            .career-item { display: grid; grid-template-columns: 170px 1fr 32px; gap: 1.5rem; align-items: start; padding: 1.6rem 0; border-bottom: 1px solid var(--line); }
            .career-period { color: var(--muted); margin: .4rem 0 0; }
            .career-item h3 { font-family: Georgia, serif; font-size: 1.35rem; font-weight: 400; margin: 0 0 .5rem; }
            .career-item p:not(.career-period) { color: var(--muted); line-height: 1.7; margin: 0; }
            .career-mark { font-size: 1.2rem; }
            .contact { padding: 3.5rem 0 1rem; display: flex; justify-content: space-between; align-items: end; gap: 2rem; }
            .contact .section-title { margin-bottom: .4rem; }
            .contact a { color: var(--ink); font-size: 1.05rem; text-decoration-thickness: 1px; text-underline-offset: 5px; }
            .footer-note { color: var(--muted); font-size: .8rem; }
            @media (max-width: 700px) {
                .main .block-container { padding: 1rem 1rem 1.5rem; }
                .hero { padding: 1.4rem; min-height: 350px; }
                .hero-grid { grid-template-columns: 1fr; gap: 1.5rem; padding: 2.2rem 0; }
                .hero h1 { font-size: 3rem; }
                .hero-index { height: 90px; }
                .hero-index strong { font-size: 3rem; }
                .about-grid { grid-template-columns: 1fr; gap: 2rem; }
                .content-section { padding: 3.5rem 0; }
                .section-title { font-size: 2.1rem; }
                .dream-panel { padding: 1.5rem; }
                .dream-panel blockquote { font-size: 1.7rem; }
                .career-item { grid-template-columns: 1fr 28px; gap: .6rem; }
                .career-period { grid-column: 1 / -1; }
                .contact { align-items: start; flex-direction: column; }
            }
        </style>
        """,
        unsafe_allow_html=True,
)

st.markdown(
        f"""
        <main class="profile-page">
            <header class="hero">
                <div class="hero-top"><span class="eyebrow">Personal profile</span><span class="eyebrow">2026</span></div>
                <div class="hero-grid">
                    <div>
                        <p class="eyebrow">안녕하세요,</p>
                        <h1>{escape(PROFILE['name'])}입니다.</h1>
                        <p class="hero-lead">{escape(PROFILE['headline'])}</p>
                    </div>
                    <div class="hero-index"><span>PROFILE / NO.</span><strong>01</strong><span>ABOUT THE AUTHOR</span></div>
                </div>
                <div class="hero-foot"><span>{escape(PROFILE['location'])}</span><span>PROFILE · INTRODUCTION</span></div>
            </header>

            <section class="content-section">
                <div class="about-grid">
                    <div>
                        <p class="section-kicker">01 / About</p>
                        <h2 class="section-title">나를 소개합니다</h2>
                        <p class="about-copy">{escape(PROFILE['introduction'])}</p>
                    </div>
                    <div>
                        <div class="affiliation">
                            <p class="affiliation-label">Affiliation</p>
                            <p class="affiliation-value">{escape(PROFILE['affiliation'])}</p>
                        </div>
                        <div class="affiliation">
                            <p class="affiliation-label">Based in</p>
                            <p class="affiliation-value">{escape(PROFILE['location'])}</p>
                        </div>
                    </div>
                </div>
                <div class="dream-panel">
                    <p class="section-kicker">02 / Dream</p>
                    <blockquote>{escape(PROFILE['dream'])}</blockquote>
                </div>
            </section>

            <section class="content-section">
                <p class="section-kicker">03 / Experience</p>
                <h2 class="section-title">경력과 경험</h2>
                <div class="career-list">{career_items}</div>
            </section>

            <footer class="contact">
                <div><p class="section-kicker">04 / Contact</p><h2 class="section-title">함께 이야기 나눠요</h2></div>
                <a href="mailto:{escape(PROFILE['email'])}">{escape(PROFILE['email'])} ↗</a>
                <p class="footer-note">© {escape(PROFILE['name'])}</p>
            </footer>
        </main>
        """,
        unsafe_allow_html=True,
)
