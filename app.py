from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Folder with valid blood cell images
VALID_FOLDER = "valid_images"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        file = request.files["file"]

        if file and file.filename != "":
            filename = file.filename.lower()

            # Get all valid files
            valid_files = os.listdir(VALID_FOLDER)

            if filename in valid_files:
                if filename.startswith("leukemia"):
                    prediction = "Leukemia"
                elif filename.startswith("lymphoma"):
                    prediction = "Lymphoma"
                elif filename.startswith("myeloma"):
                    prediction = "Myeloma"
                elif filename.startswith("healthy"):
                    prediction = "Healthy"
                else:
                    prediction = "Unknown type"
            else:
                error = "Please upload a valid blood smear image."
        else:
            error = "No file selected. Please choose an image."

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True)