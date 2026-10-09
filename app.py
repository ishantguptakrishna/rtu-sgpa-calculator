from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from ocr_engine import extract_text_from_file
from parser import parse_extracted_text, extract_semester
from calculator import calculate_sgpa

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB max

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            import gc
            
            # Process the file
            text = extract_text_from_file(filepath)
            
            # Immediately force garbage collection to free up memory from Tesseract/Pillow
            gc.collect()
            
            semester = extract_semester(text)
            courses = parse_extracted_text(text)
            
            if not courses:
                return jsonify({'error': 'Could not extract any courses or grades from the file. Please check the image quality.'}), 400
                
            print("EXTRACTED COURSES:")
            for c in courses:
                print(f"{c['code']} | {c['title']} | Grade: {c['grade']}")
                
            sgpa, results = calculate_sgpa(courses)
            print(f"CALCULATED SGPA: {sgpa}")
            
            # Clean up uploaded file
            # try:
            #     os.remove(filepath)
            # except:
            #     pass
                
            return jsonify({
                'semester': semester,
                'sgpa': sgpa,
                'results': results
            })
            
        except Exception as e:
            # Clean up uploaded file on error
            # try:
            #     os.remove(filepath)
            # except:
            #     pass
            return jsonify({'error': str(e)}), 500
            
    return jsonify({'error': 'Invalid file format. Only PDF, PNG, and JPG are allowed.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
