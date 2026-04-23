from flask import Flask, send_file
import qrcode
import io
import random

app = Flask(__name__)

URL = "https://qr-app.onrender.com/qr.png"

@app.route("/")
def home():
    return '<h1>QR Code</h1><img src="/qr.png">'

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
