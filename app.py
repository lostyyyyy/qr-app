from flask import Flask, send_file
import qrcode
import io
import random

app = Flask(__name__)

URL = "https://qr-app-ua9a.onrender.com"

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                background: white;
            }
            img {
                max-width: 90vw;
                max-height: 90vh;
            }
        </style>
    </head>
    <body>
        <img src="/qr.png">
    </body>
    </html>
    '''

@app.route("/qr.png")
def generate_qr():
    qr = qrcode.QRCode(
        error_correction=random.choice([
            qrcode.constants.ERROR_CORRECT_L,
            qrcode.constants.ERROR_CORRECT_M,
            qrcode.constants.ERROR_CORRECT_H,
        ]),
        box_size=random.randint(8, 12),
        border=random.randint(2, 5),
    )
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")
