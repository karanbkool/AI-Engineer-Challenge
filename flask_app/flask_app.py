from flask import Flask, request, jsonify
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/image', methods=['POST'])
def generate_image():
    data = request.get_json()
    if not data or 'hex' not in data:
        return jsonify({'error': 'Missing "hex" key in JSON input'}), 400
    
    hex_code = data['hex']
    try:
        img = Image.new('RGB', (1500, 1500), hex_code)
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        base64_img = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return jsonify({'image': base64_img})
    except ValueError:
        return jsonify({'error': 'Invalid hex code'}), 400

if __name__ == '__main__':
    app.run(debug=True)
