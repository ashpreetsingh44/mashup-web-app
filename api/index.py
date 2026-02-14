from flask import Flask, request, send_file, render_template
import zipfile

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static",
    static_url_path="/static"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    singer = request.form.get("singer", "Unknown")
    zipname = "/tmp/mashup.zip"

    with zipfile.ZipFile(zipname, "w") as z:
        z.writestr("result.txt", f"Mashup generated for {singer}")

    return send_file(zipname, as_attachment=True)
