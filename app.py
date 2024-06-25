from flask import Flask, request, jsonify
import string
import random

app = Flask(__name__)

url_mapping = {}
short_to_long = {}

CHAR_POOL = string.ascii_letters + string.digits

def generate_short_url():
    return ''.join(random.choices(CHAR_POOL, k=6))

@app.route('/encode', methods=['POST'])
def encode():
    long_url = request.json.get('url')
    if not long_url:
        return jsonify({'error': 'URL is required'}), 400

    if long_url in url_mapping:
        short_url = url_mapping[long_url]
    else:
        short_url = generate_short_url()
        while short_url in short_to_long:  # Ensure uniqueness
            short_url = generate_short_url()
        url_mapping[long_url] = short_url
        short_to_long[short_url] = long_url

    return jsonify({'short_url': f'http://short.est/{short_url}'})

@app.route('/decode', methods=['POST'])
def decode():
    short_url = request.json.get('url')
    if not short_url:
        return jsonify({'error': 'URL is required'}), 400

    short_url_key = short_url.split('/')[-1]
    long_url = short_to_long.get(short_url_key)

    if not long_url:
        return jsonify({'error': 'Short URL not found'}), 404

    return jsonify({'long_url': long_url})

if __name__ == '__main__':
    app.run(debug=True)
