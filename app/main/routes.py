from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('error.html', message="No file uploaded.")

    file = request.files['file']
    if file.filename == '':
        return render_template('error.html', message="No selected file.")

    # Dummy data for demonstration
    predicted_disease = "Common Cold"
    recommended_medication = "Rest and hydration"

    return render_template('result.html', prediction=predicted_disease, recommendation=recommended_medication)
