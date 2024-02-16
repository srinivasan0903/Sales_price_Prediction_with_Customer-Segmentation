#this code displays the cluster value for all members


# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler

# app = Flask(__name__)
# CORS(app)

# # Load the dataset
# df = pd.read_csv('cluster.csv')

# # Extract relevant features for clustering
# features = df[['sales']].values

# # Standardize the features
# scaler = StandardScaler()
# features_standardized = scaler.fit_transform(features)

# # K-means clustering
# num_clusters = 3  # You can adjust this based on your requirement
# kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
# df['cluster'] = kmeans_model.fit_predict(features_standardized)

# # Save clustered data to a new CSV file
# df.to_csv('clustered_data.csv', index=False)

# # Define an endpoint to get clustered names and domains
# @app.route('/cluster', methods=['GET'])
# def get_cluster_results():
#     # Read clustered data
#     clustered_data = pd.read_csv('clustered_data.csv')

#     # Group by cluster and collect names and domains
#     clustered_info = clustered_data.groupby('cluster').agg({'name': list, 'domain': 'first'}).reset_index()

#     # Convert to JSON format
#     clustered_json = clustered_info.to_json(orient='records')

#     return clustered_json

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)



#this code displays the clustered people alone


# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import pandas as pd
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler


# app = Flask(__name__)
# CORS(app)


# # Load the dataset
# df = pd.read_csv('cluster.csv')

# # Extract relevant features for clustering (sales and domain)
# features = df[['sales']].values

# # Standardize the features
# scaler = StandardScaler()
# features_standardized = scaler.fit_transform(features)

# # K-means clustering
# num_clusters = 3  # You can adjust this based on your requirement
# kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
# df['cluster'] = kmeans_model.fit_predict(features_standardized)

# # Identify clusters with high sales values
# high_sales_clusters = df.groupby('cluster')['sales'].mean().sort_values(ascending=False).index[:1]

# # Filter the dataframe to include only rows from high sales clusters
# df_high_sales = df[df['cluster'].isin(high_sales_clusters)]

# # Save clustered data to a new CSV file
# df_high_sales.to_csv('high_sales_clusters.csv', index=False)

# @app.route('/high_sales_clusters_csv', methods=['GET'])
# def get_high_sales_clusters_csv():
#     return send_file('high_sales_clusters.csv', as_attachment=True)

# @app.route('/cluster', methods=['GET', 'POST'])
# def get_cluster_results():
#     # Read clustered data with high sales values
#     if request.method == 'POST':
#         # Handle the POST request, perform clustering, and return the necessary response
#         # ...
#         return jsonify({'message': 'Clustering completed successfully'})

#     # For GET requests, return the high sales clusters
#     clustered_data_high_sales = pd.read_csv('high_sales_clusters.csv')

#     # Find the domain with the highest sales value in each cluster
#     cluster_results = []
#     for cluster_id, group in clustered_data_high_sales.groupby('cluster'):
#         max_sales_row = group.loc[group['sales'].idxmax()]  # Get the row with the max sales value
#         domain = max_sales_row['domain']
#         cluster_results.append({'cluster': cluster_id, 'domain': domain})

#     # Convert to JSON format
#     clustered_json = jsonify(cluster_results)

#     return clustered_json

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)


#this code displays discount in float values

# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import pandas as pd
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler

# app = Flask(__name__)
# CORS(app)

# # Load the dataset
# df = pd.read_csv('cluster.csv')

# # Extract relevant features for clustering (sales)
# features = df[['sales']].values

# # Standardize the features
# scaler = StandardScaler()
# features_standardized = scaler.fit_transform(features)

# # K-means clustering
# num_clusters = 3  # You can adjust this based on your requirement
# kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
# df['cluster'] = kmeans_model.fit_predict(features_standardized)

# # Identify clusters with high sales values
# high_sales_clusters = df.groupby('cluster')['sales'].mean().sort_values(ascending=False).index[:1]

# # Filter the dataframe to include only rows from high sales clusters
# df_high_sales = df[df['cluster'].isin(high_sales_clusters)].copy()  # Create a copy to avoid SettingWithCopyWarning

# # Calculate discount for each row based on sales value
# df_high_sales['discount'] = df_high_sales['sales'] * 0.1  # Adjust the discount percentage as needed

# # Save clustered data with discount to a new CSV file
# df_high_sales.to_csv('high_sales_clusters_with_discount.csv', index=False)

# # Print the head of the new CSV file to verify the 'discount' column is present
# verification_df = pd.read_csv('high_sales_clusters_with_discount.csv')
# print(verification_df.head())

# @app.route('/high_sales_clusters_csv', methods=['GET'])
# def get_high_sales_clusters_csv():
#     return send_file('high_sales_clusters_with_discount.csv', as_attachment=True)

# @app.route('/cluster', methods=['GET', 'POST'])
# def get_cluster_results():
#     # Read clustered data with high sales values and discount
#     if request.method == 'POST':
#         # Handle the POST request, perform clustering, calculate discount, and return the necessary response
#         # ...
#         return jsonify({'message': 'Clustering and discount calculation completed successfully'})

#     # For GET requests, return the high sales clusters with discount
#     clustered_data_high_sales = pd.read_csv('high_sales_clusters_with_discount.csv')

#     # Convert to JSON format
#     clustered_json = clustered_data_high_sales.to_json(orient='records')

#     return clustered_json

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)





from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

# Load the dataset
df = pd.read_csv('cluster.csv')

# Extract relevant features for clustering (sales)
features = df[['sales']].values

# Standardize the features
scaler = StandardScaler()
features_standardized = scaler.fit_transform(features)

# K-means clustering
num_clusters = 3  # You can adjust this based on your requirement
kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
df['cluster'] = kmeans_model.fit_predict(features_standardized)

# Identify clusters with high sales values
high_sales_clusters = df.groupby('cluster')['sales'].mean().sort_values(ascending=False).index[:1]

# Filter the dataframe to include only rows from high sales clusters
df_high_sales = df[df['cluster'].isin(high_sales_clusters)].copy()  # Create a copy to avoid SettingWithCopyWarning

# Calculate discount for each row based on sales value (rounded to 2 decimal places)
df_high_sales['discount'] = (df_high_sales['sales'] * 0.1).round(2)

# Save clustered data with discount to a new CSV file
df_high_sales.to_csv('high_sales_clusters_with_discount.csv', index=False)

# Print the head of the new CSV file to verify the 'discount' column is present
verification_df = pd.read_csv('high_sales_clusters_with_discount.csv')
print(verification_df.head())

@app.route('/high_sales_clusters_csv', methods=['GET'])
def get_high_sales_clusters_csv():
    return send_file('high_sales_clusters_with_discount.csv', as_attachment=True)

@app.route('/cluster', methods=['GET', 'POST'])
def get_cluster_results():
    # Read clustered data with high sales values and discount
    if request.method == 'POST':
        # Handle the POST request, perform clustering, calculate discount, and return the necessary response
        # ...
        return jsonify({'message': 'Clustering and discount calculation completed successfully'})

    # For GET requests, return the high sales clusters with discount
    clustered_data_high_sales = pd.read_csv('high_sales_clusters_with_discount.csv')

    # Convert to JSON format
    clustered_json = clustered_data_high_sales.to_json(orient='records')

    return clustered_json

# Run the Flask app
