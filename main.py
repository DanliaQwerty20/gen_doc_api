from flask import Flask, request, send_file
from docx import Document
import uuid

app = Flask(__name__)

@app.route('/generate-doc', methods=['POST'])
def generate_document():
    data = request.json
    replacements = {
        "{universityName}": data.get("universityName", ""),
        "{studentName}": data.get("studentName", ""),
        "{topicReportDescription}": data.get("topicReportDescription", ""),
        "{topicReport}": data.get("topicReport", ""),
        "{advisorName}": data.get("advisorName", ""),
        "{educationLevel}": data.get("educationLevel", ""),
        "{educationDirection}": data.get("educationDirection", ""),
        "{formEducation}": data.get("formEducation", ""),
        "{numberPhone}": data.get("numberPhone", ""),
        "{email}": data.get("email", ""),
        "{section}": data.get("section", ""),
        "{academicTitle}": data.get("academicTitle", ""),
        "{faculty}": data.get("faculty", ""),
        "{yearStudy}": data.get("yearStudy", ""),
        "{group}": data.get("group", ""),
        "{base}": data.get("base", "")
    }

    template_path = "template.docx"
    doc = Document(template_path)

    for para in doc.paragraphs:
        for key, value in replacements.items():
            if key in para.text:
                para.text = para.text.replace(key, value)

    output_filename = f"filled_doc_{uuid.uuid4().hex}.docx"
    doc.save(output_filename)

    return send_file(output_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000)