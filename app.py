from flask import Flask, render_template, abort

app = Flask(__name__)

# محتوى الموقع كما طلبت
pages = {
    "home": {
        "title": "MUTINY",
        "hero_image": "club1.jpg",
        "hero_big": True,
        "content_html": None
    },
    "about": {
        "title": "عن MUTINY",
        "hero_image": "club.jpg",
        "content_html": """
<p><strong>MUTINY</strong>، النادي صاحب الفكر المستقبلي الذي سيغيّر معنى البرو كلوب، وذلك لا يقتصر فقط على تصميم النادي وأزياء اللاعبين، بل وأيضًا على اللاعبين أنفسهم، ومرافق النادي، وكذلك لاعبو الذكاء الاصطناعي في الفريق (BOTS)، وإحدى هذه الأفكار هي إنشاء هذا الموقع الخاص بالنادي.</p>

<blockquote><em>"نحن لا نتبع القواعد... نحن نتمرّد."</em></blockquote>

<p>في هذا النادي، نحن لا نسير خلف أحد، نحن نكسر القواعد، ونخلق طريقنا الخاص. وُلد MUTINY من رحم الفوضى. اسمنا يعني التمرّد، العصيان، ورفض الخضوع. لسنا مجرد نادٍ، بل فكرة: أن تقف ضد التيار، أن تلعب بأسلوبك، وأن تفرض هيبتك دون إذن أحد. نحن الفريق الذي لا يخشى المجازفة، نُهاجم بعزيمة لا تنكسر، وندافع بشراسة لا تُقهر.</p>

<p><strong> "MUTINY ليس مجرد نادي..."</strong></p>
"""
    },
    "achievements": {
        "title": "منجزات النادي",
        "hero_image": "trophy.jpg",
        "content_html": "<p>نادي MUTINY معكم يصنع التاريخ بإذن الله تعالى</p>"
    },
    "players": {
        "title": "إحصائيات اللاعبين",
        "hero_image": "stats.jpg",
        "content_html": """
<h3>الأكثر تهديفاً:</h3>
<ol>
  <li>اللاعب 1 — بـ ( ) هدف</li>
  <li>اللاعب 2 — بـ ( ) هدف</li>
  <li>اللاعب 3 — بـ ( ) هدف</li>
</ol>

<h3>الأكثر صناعة:</h3>
<ol>
  <li>اللاعب 1 — بـ ( ) صناعة</li>
  <li>اللاعب 2 — بـ ( ) صناعة</li>
  <li>اللاعب 3 — بـ ( ) صناعة</li>
</ol>

<h3>نجوم مباريات النادي:</h3>
<ol>
  <li>(اسم) — رجل المباراة ( ) مرة</li>
  <li>(اسم) — رجل المباراة ( ) مرة</li>
  <li>(اسم) — رجل المباراة ( ) مرة</li>
</ol>
"""
    },
    "presidents": {
        "title": "الرؤساء",
        "hero_image": "president.jpg",
        "content_html": """
<ul>
  <li><strong>سالم الشهري</strong><br>Online ID: sa-1-0</li>
  <li><strong>إبراهيم الشهري</strong><br>Online ID: IBRA_SH47</li>
  <li><strong>عبدالله الشهري</strong><br>Online ID: ad_7ull</li>
  <li><strong>أحمد الشهري</strong><br>Online ID: NINJA_AL507</li>
</ul>
"""
    },
    "kits": {
        "title": "أطقم وملعب النادي",
        "hero_image": "kits.jpg",
        "content_html": """
<h3>1- ملعب النادي :</h3>
<p>ملعب نادي MUTINY ( ) بسعة ( ) مشجع.</p>

<h3>2- أطقم النادي :</h3>

<div class="kit">
  <img src="/static/kits1.jpg" alt="kits1" class="kit-thumb">
  <p><strong>الطقم الأول</strong></p>
</div>

<div class="kit">
  <img src="/static/kits2.jpg" alt="kits2" class="kit-thumb">
  <p><strong>الطقم الثاني</strong></p>
</div>

<div class="kit">
  <img src="/static/kits3.jpg" alt="kits3" class="kit-thumb">
  <p><strong>الطقم الثالث</strong></p>
</div>

<div class="kit">
  <img src="/static/kits4.jpg" alt="kits4" class="kit-thumb">
  <p><strong>طقم الحراس</strong></p>
</div>

"""
    }
}


@app.route("/")
def home():
    page = pages["home"]
    return render_template("index.html", page=page, menu=pages)

@app.route("/page/<slug>")
def show(slug):
    page = pages.get(slug)
    if not page:
        abort(404)
    return render_template("index.html", page=page, menu=pages)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
