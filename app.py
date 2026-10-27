
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">
        <title>موقعي الأول</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #101828, #243b55);
                color: white;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
            .card {
                padding: 35px 25px;
                margin: 20px;
                border-radius: 20px;
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.15);
                max-width: 350px;
            }
            h1 { color: #66e3ff; }
            p { line-height: 1.8; }
            a {
                display: inline-block;
                background: #66e3ff;
                color: #101828;
                padding: 12px 22px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>مرحبا بيك 👋</h1>
            <p>هذا أول موقع ويب نصنعوه باستعمال Python و Flask.</p>
            <a href="https://www.python.org/">تعرف على Python</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)


