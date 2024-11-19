from flask import Flask, send_file
import os
import random
import string
import hashlib

app = Flask(__name__)

@app.route('/file', methods=['GET'])
def send_random_file():
    file_path = '/serverdata/random.txt'
    checksum_path = '/serverdata/checksum.txt'
    
    # Generate random text
    with open(file_path, 'w') as f:
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=1024))
        f.write(random_text)
    
    # Calculate checksum
    checksum = hashlib.md5(random_text.encode()).hexdigest()
    with open(checksum_path, 'w') as f:
        f.write(checksum)
    
    return send_file(file_path)
    
@app.route('/checksum', methods=['GET'])
def send_checksum():
    return send_file('/serverdata/checksum.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
