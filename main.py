import xml.etree.ElementTree as ET
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Load and parse the XML file
tree = ET.parse('data.xml')
root = tree.getroot()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/data')
def get_data():
    data = []
    for node in root.findall('node'):
        node_details = {
            "id": node.get("id"),
            "latitude": node.get("lat"),
            "longitude": node.get("lon"),
            "tags": {}
        }
        for tag in node.findall('tag'):
            node_details["tags"][tag.get('k')] = tag.get('v')
        data.append(node_details)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
