from flask import Flask, render_template, request

app = Flask(__name__)

def caesar(msg, mode):

    message = msg
    key = 13
    mode = mode            # True = encrypt False = Decrypt
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == True:         # 'encrypt'
                translatedIndex = symbolIndex + key
            elif mode == False:      # 'decrypt'
                translatedIndex = symbolIndex - key

            # Handle wrap-around, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    return translated

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    msg = request.form.get("msg")
    mode = True
    name = caesar(msg, mode)
    return render_template("encrypt.html", name=name)

@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    msg = request.form.get("msg1")
    mode = False
    name = caesar(msg, mode)
    return render_template("decrypt.html", name=name)