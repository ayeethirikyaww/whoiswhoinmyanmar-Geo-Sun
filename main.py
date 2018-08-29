from flask import Flask, render_template, url_for

app=Flask(__name__)

@app.route('/')
@app.route("/index")
def hello():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/aboutactor")
def aboutactor():
    return render_template("aboutactor.html")

@app.route("/aboutdirector")
def aboutdirector():
    return render_template("aboutdirector.html")

@app.route("/aboutparli")
def aboutparli():
    return render_template("aboutparli.html")

@app.route("/aboutsinger")
def aboutsinger():
    return render_template("aboutsinger.html")

@app.route("/aboutwriter")
def aboutwriter():
    return render_template("aboutwriter.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/method")
def method():
    return render_template("method.html")

@app.route("/moreactor")
def moreactor():
    return render_template("moreactor.html")

@app.route("/moredirector")
def moredirector():
    return render_template("moredirector.html")

@app.route("/moreparli")
def moreparli():
    return render_template("moreparli.html")

@app.route("/moresinger")
def moresinger():
    return render_template("moresinger.html")

@app.route("/morewriter")
def morewriter():
    return render_template("morewriter.html")

@app.route("/partner")
def partner():
    return render_template("partner.html")

@app.route("/qa")
def qa():
    return render_template("qa.html")

@app.route("/send")
def send():
    return render_template("send.html")

@app.route("/use")
def use():
    return render_template("use.html")

if __name__=="__main__":
    app.run(debug=True)
