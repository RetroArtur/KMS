from flask import Flask, request, render_template, jsonify
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = '/data/shared/Exports'
ALLOWED_EXTENSIONS = {'txt', 'md', 'pdf', 'json'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return jsonify({'success': f'Datei {file.filename} hochgeladen'})
    else:
        return jsonify({'error': 'Invalid file type'})
    
@app.route('/upload-json', methods=['POST'])
def upload_json():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if not file.filename.lower().endswith('.json'):
        return jsonify({'error': 'Only JSON files are allowed'})
    
    # Save as KMS.json regardless of original filename
    filename = os.path.join(app.config['UPLOAD_FOLDER'], 'KMS.json')
    file.save(filename)
    return jsonify({'success': 'Zotero JSON Datei wurde erfolgreich hochgeladen'})

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        script_path = os.path.join(UPLOAD_FOLDER, 'pull_zotero.py')
        subprocess.run(['python3', script_path, 'KMS.json', '.'], check=True)
        
        return jsonify({'success': 'Zotero Dateien wurden erfolgreich heruntergeladen'})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'Script execution failed: {str(e)}'})
    
@app.route('/list-files')
def list_files():
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        if filename.lower().endswith(('.pdf', '.md', '.txt')):
            files.append(filename)
    return jsonify({'files': files})

@app.route('/delete-file/<filename>', methods=['DELETE'])
def delete_file(filename):
    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return jsonify({'success': f'Datei {filename} gelöscht'})
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Error deleting file: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
