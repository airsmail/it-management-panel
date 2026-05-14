from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Bostan IT Panel - GitHub Otomasyonu Devrede!</h1><p>Bu yazı GitHub'dan otomatik geldi.</p>"

if __name__ == "__main__":
    app.run()
