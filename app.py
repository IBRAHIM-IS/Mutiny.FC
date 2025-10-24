import streamlit as st
from PIL import Image

# --- إعداد الصفحة ---
st.set_page_config(
    page_title="MUTINY",
    layout="wide",
)

# --- قائمة جانبية ---
st.sidebar.title("القائمة")
menu = st.sidebar.radio(
    "اختر القسم",
    ("الصفحة الرئيسية", "عن MUTINY", "منجزات النادي", "إحصائيات اللاعبين", "الرؤساء", "أطقم وملعب النادي")
)

# --- اللون الخلفي (لون رمادي فاتح) ---
st.markdown(
    """
    <style>
    .main {
        background-color: #2E2E2E;
        color: white;
    }
    .stApp {
        background-color: #2E2E2E;
    }
    .css-1d391kg {
        background-color: #2E2E2E;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- الصفحة الرئيسية ---
if menu == "الصفحة الرئيسية":
    st.markdown("<h1 style='text-align:center; font-size:60px;'>MUTINY</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:24px;'>أهلاً بك في أفضل نادي في FC26</p>", unsafe_allow_html=True)
    img = Image.open("club1.jpg")
    st.image(img, use_column_width=True)

# --- عن MUTINY ---
elif menu == "عن MUTINY":
    st.header("عن MUTINY")
    img = Image.open("club.jpg")
    st.image(img, use_column_width=True)
    st.write("""
MUTINY، النادي صاحب الفكر المستقبلي الذي سيغيّر معنى البرو كلوب، وذلك لا يقتصر فقط على تصميم النادي وأزياء اللاعبين، بل وأيضًا على اللاعبين أنفسهم، ومرافق النادي، وكذلك لاعبو الذكاء الاصطناعي في الفريق (BOTS)، وإحدى هذه الأفكار هي إنشاء هذا الموقع الخاص بالنادي.
"نحن لا نتبع القواعد... نحن نتمرّد."
في هذا النادي، نحن لا نسير خلف أحد، نحن نكسر القواعد، ونخلق طريقنا الخاص.
وُلد MUTINY من رحم الفوضى.
اسمنا يعني التمرّد، العصيان، ورفض الخضوع.
لسنا مجرد نادٍ، بل فكرة:
أن تقف ضد التيار، أن تلعب بأسلوبك، وأن تفرض هيبتك دون إذن أحد.
نحن الفريق الذي لا يخشى المجازفة،
نُهاجم بعزيمة لا تنكسر،
وندافع بشراسة لا تُقهر.
"MUTINY ليس مجرد نادي..."
""")

# --- منجزات النادي ---
elif menu == "منجزات النادي":
    st.header("منجزات النادي")
    img = Image.open("trophy.jpg")
    st.image(img, use_column_width=True)
    st.write("نادي MUTINY معكم يصنع التاريخ بإذن الله تعالى")

# --- إحصائيات اللاعبين ---
elif menu == "إحصائيات اللاعبين":
    st.header("إحصائيات اللاعبين")
    img = Image.open("stats.jpg")
    st.image(img, use_column_width=True)
    st.subheader("الأكثر تهديفاً")
    st.write("1- ( ) بـ ( ) هدف")
    st.write("2- ( ) بـ ( ) هدف")
    st.write("3- ( ) بـ ( ) هدف")

    st.subheader("الأكثر صناعة")
    st.write("1- ( ) بـ ( ) صناعة")
    st.write("2- ( ) بـ ( ) صناعة")
    st.write("3- ( ) بـ ( ) صناعة")

    st.subheader("نجوم مباريات النادي")
    st.write("1- ( ) رجل المباراة ( ) مرة")
    st.write("2- ( ) رجل المباراة ( ) مرة")
    st.write("3- ( ) رجل المباراة ( ) مرة")

# --- الرؤساء ---
elif menu == "الرؤساء":
    st.header("الرؤساء")
    img = Image.open("president.jpg")
    st.image(img, use_column_width=True)
    st.write("سالم الشهري - Online ID: sa-1-0")
    st.write("إبراهيم الشهري - Online ID: IBRA_SH47")
    st.write("عبدالله الشهري - Online ID: ad_7ull")
    st.write("أحمد الشهري - Online ID: NINJA_AL507")

# --- أطقم وملعب النادي ---
elif menu == "أطقم وملعب النادي":
    st.header("أطقم وملعب النادي")
    img = Image.open("kits.jpg")
    st.image(img, use_column_width=True)
    st.write("1- ملعب النادي: ملعب نادي MUTINY ( ) بسعة ( ) مشجع.")
    st.write("2- أطقم النادي:")
    st.write("- الطقم الأول")
    st.write("- الطقم الثاني")
    st.write("- الطقم الثالث")
    st.write("- طقم الحراس")
