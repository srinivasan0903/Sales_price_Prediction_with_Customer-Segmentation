from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
from sklearn.cluster import KMeans

app = Flask(__name__)
CORS(app)

def customer_segmentation(file_name, num_clusters):
    data = pd.read_csv(file_name)

    # Assuming your CSV file has columns like 'name', 'sales', 'domain'
    features = ['sales']
    X = data[features]

    # K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    data['cluster'] = kmeans.fit_predict(X)

    # Extract clustered names and domains
    clustered_data = data[['name', 'domain', 'cluster']]
    
    # Save the clustered data to a CSV file
    clustered_data.to_csv('clustered_data.csv', index=False)

@app.route('/', methods=['POST', 'GET'])
def perform_customer_segmentation():
    if request.method == 'POST':
        num_clusters = int(request.form['num_clusters'])

        file = request.files['file']
        file_name = file.filename
        file.save(file_name)

        customer_segmentation(file_name, num_clusters)

        response_headers = {'Access-Control-Allow-Origin': '*'}
        response = {'message': 'Success'}
        return jsonify(response), 200, response_headers

    if request.method == 'GET':
        return render_template('cluster.html')  # Assuming you have a result.html template

@app.route('/cluster-results', methods=['GET'])
def get_cluster_results():
    # Read the clustered data from the CSV file
    clustered_data = pd.read_csv('clustered_data.csv')
    # Convert to JSON format
    clustered_json = clustered_data.to_json(orient='records')
    return clustered_json

if __name__ == '__main__':
    app.run(debug=True)
