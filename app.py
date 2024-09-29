from flask import Flask, render_template, request
from extractor import extract_citation_from_pdf 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', citations=None)

@app.route('/upload', methods=['POST'])
def upload():
    if 'files' not in request.files:
        return "No files uploaded", 400

    files = request.files.getlist('files')
    citations = []
    
    for file in files:
        if file.filename == '':
            return "No file selected", 400

        citation = extract_citation_from_pdf(file)  
        citations.append(citation)

    return render_template('index.html', citations=citations) 

if __name__ == '__main__':
    app.run(debug=True)
