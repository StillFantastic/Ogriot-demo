from flask import Flask, render_template, request, url_for, redirect, make_response
import os
import time

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "/home/islab/demo/static/image"
box = []
time_box = []
temperature = [25, 26, 27, 28, 29, 28, 27, 26, 25, 20, 28, 35, 28, 29]
maturity = ["50%", "69%", "96%", "55%", "38%", "83%", "17%", "79%", "17%"]
wet = ["38%", "47%", "69%", "96%", "87%", "78%", "100%", "0%", "50%", "49%"]


@app.route("/home", methods=["get"])
def homePage():
    return render_template("index.html",
                            box=box,
                            time_box=time_box,
                            temperature=temperature,
                            maturity=maturity,
                            wet=wet)
        
@app.route("/receive", methods=["post"])
def handleReceive():
    if request.method == "POST":
        if "file" not in request.files or "category" not in request.form:
            # 400 Bad Request
            res = make_response("mission data", 400) 

        # Category
        box.append(request.form["category"])

        # Image
        file = request.files["file"]
        filename = "demo_" + str(len(box) - 1)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        
        # Time
        t = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        time_box.append(t)
        return redirect(url_for("homePage"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

