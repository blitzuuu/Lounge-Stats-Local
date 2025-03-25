from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-lounge-stats', methods=['GET'])
def run_lounge_stats():
    try:
        # Run the LoungeStats.py script
        result = subprocess.run(['python3', 'LoungeStats.py'], capture_output=True, text=True)
        return jsonify({"status": "success", "output": result.stdout}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
