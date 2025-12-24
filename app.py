import streamlit as st
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Amulya B | Portfolio",
    page_icon="🌸",
    layout="centered"
)

# ---------------- STYLES ----------------
st.markdown("""
<style>
.stApp {
    background-color: #F4F1FF;
}

.block-container {
    max-width: 760px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

.name {
    font-size: 36px;
    font-weight: 700;
    color: #1A1A1A;
}

.title {
    font-size: 18px;
    color: #6B5FEA;
    font-weight: 600;
    margin-bottom: 12px;
}

.text {
    font-size: 16px;
    color: #2F2F2F;
    line-height: 1.65;
}

.section {
    font-size: 24px;
    font-weight: 700;
    margin-top: 48px;
    margin-bottom: 18px;
    color: #1A1A1A;
    border-bottom: 2px solid #D6D1FF;
    padding-bottom: 6px;
}

.project-title {
    font-size: 18px;
    font-weight: 600;
    margin-top: 22px;
    margin-bottom: 6px;
    color: #2B2B2B;
}

a {
    color: #6B5FEA !important;
    text-decoration: none;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([1, 3])

with col1:
    img = Image.open("profile.jpg")
    st.image(img, width=150)

with col2:
    st.markdown("<div class='name'>Amulya B</div>", unsafe_allow_html=True)
    st.markdown("<div class='title'>AI/ML Engineer | Backend Developer</div>", unsafe_allow_html=True)

    st.markdown(
        "<p class='text'>I build applied machine learning systems focused on healthcare, "
        "IoT, and real-world deployment. My work emphasizes clarity, reliability, and "
        "practical impact.</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "[GitHub](https://github.com/amulya817) • "
        "[LinkedIn](https://www.linkedin.com/in/amulya-b-7a0786239)"
    )

    # -------- RESUME DOWNLOAD BUTTON --------
    with open("Amulya_B_Resume.pdf", "rb") as file:
        st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Amulya_B_Resume.pdf",
            mime="application/pdf"
        )

# ---------------- PROJECTS ----------------
st.markdown("<div class='section'>Projects ✨</div>", unsafe_allow_html=True)

st.markdown("<div class='project-title'>🩺 Sleep Apnea Detection (IoT + ML)</div>", unsafe_allow_html=True)
st.markdown(
    "<p class='text'>Wearable IoT-based system using ESP32-C3 and MAX30102 to monitor heart rate and SpO₂. "
    "A Random Forest model trained on physiological features achieved <b>97% accuracy</b>. "
    "Includes Firebase-based cloud storage and a real-time Streamlit dashboard.</p>",
    unsafe_allow_html=True
)
st.markdown("[GitHub](https://github.com/amulya817/Sleep-apnea-Detection-with-IOT-)")

st.markdown("<div class='project-title'>🧠 Pediatric Retinal OCT Disease Classification</div>", unsafe_allow_html=True)
st.markdown(
    "<p class='text'>Deep learning–based medical image classification system using OCT images. "
    "Fine-tuned a ResNet-18 model with transfer learning in PyTorch to classify CNV, DME, "
    "DRUSEN, and Normal cases. Training accelerated using GPU on Google Colab.</p>",
    unsafe_allow_html=True
)
st.markdown("[GitHub](https://github.com/amulya817/pediatric-retinal-oct)")

st.markdown("<div class='project-title'>🛠️ Habit Tracker — Full Stack Web Application</div>", unsafe_allow_html=True)
st.markdown(
    "<p class='text'>Full-stack habit tracking application built with React and FastAPI. "
    "RESTful APIs documented using Swagger and deployed using Vercel (frontend) and "
    "Railway (backend).</p>",
    unsafe_allow_html=True
)
st.markdown(
    "[GitHub](https://github.com/amulya817/Habit-tracker) • "
    "[Live App](https://habit-tracker-two-beryl.vercel.app/)"
)

# ---------------- SKILLS ----------------
st.markdown("<div class='section'>Skills ✨</div>", unsafe_allow_html=True)
st.markdown("""
<p class='text'><b>🧠 AI / ML:</b> Python, Scikit-learn, PyTorch, CNNs, Transfer Learning</p>
<p class='text'><b>⚙️ Backend:</b> FastAPI, REST APIs, Firebase, Swagger/OpenAPI</p>
<p class='text'><b>🧰 Tools:</b> Git, GitHub, Google Colab (GPU), Vercel, Railway</p>
""", unsafe_allow_html=True)

# ---------------- CONTACT ----------------
st.markdown("<div class='section'>Contact ✨</div>", unsafe_allow_html=True)
st.markdown(
    "<p class='text'>📧 amulyabkrishna@gmail.com<br>"
    "🔗 https://www.linkedin.com/in/amulya-b-7a0786239</p>",
    unsafe_allow_html=True
)
