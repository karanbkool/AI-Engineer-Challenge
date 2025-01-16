**AI Engineer Interview Challenge Documentation**

**1.0 Objectives and Functional Overview**

* Flask REST API: Crafting a simple server that accepts a hex color code and returns a base64 encoded PNG image of that color.  
* Weaviate Setup: A local instance of Weaviate is set up using Docker. A collection named “Colors” is created with specific properties. Data is inserted and queried through a Jupyter Notebook.  
* Ollama Setup: Ollama is configured locally with the `nomic-embed-text` model to generate 768-dimensional embeddings for given text.

**2.0 Flask REST API**

* The /image endpoint listens for POST requests.  
* The function uses Pillow library to create an image (1500 x 1500\) of the color described in the hex key of JSON input.  
* The image is encoded as a base64 image and returned in a JSON output, unless there are errors with the hex code or data.

Next, we run the flask\_app.py file on cmd. The Flask server has an endpoint on:  [http://127.0.0.1:5000/image](http://127.0.0.1:5000/image).


**3.0 Weaviate with Docker**  
I created a docker-compose.yml file.  

* This configuration sets up a Weaviate instance with no vectorizer; external vectors are expected on data insertion.  
* Opens port 8080 for API access.  
* Stores data in a data folder locally.

We run Weaviate through docker in the command prompt after navigating to the docker compose file. The Docker instantiated Weaviate creates the schema at the following endpoint: [http://localhost:8080/v1/schema](http://localhost:8080/v1/schema).


**4.0 Ollama embedding with nomic-embed-text**
This code sets up a local ollama server and listens on port 11435\. Ollama run nomic-embed-text can be used as a CLI. 

**5.0 Testing Results**  
I created a Testing.ipynb jupyter notebook to test out the functionality of Flask API (5.1), Weaviate(5.2) and Ollama(5.3).

	**5.1 Flask API Test**  

* Uses `subprocess` to start the Flask server.  
* Sends a POST request with a JSON payload containing a hex color.  
* Decodes the base64 image and displays it inline in the notebook.  
* Shuts Flask down.

For testing, we use red as hex input for the flask server, and it returns a 1500 x 1500 pixel red color image.

**5.2 Weaviate Test**  

* Connects to local Weaviate.  
* Clears out any existing `Colors` class.  
* Defines and creates a new `Colors` class schema.  
* Iterates over sample color data.  
* Inserts each item into Weaviate with an external vector.  
* Queries all objects from the `Colors` collection.  
* Prints the output to verify insertion.  
* Deletes all classes to clean up the Weaviate instance after testing.

Successful insertion of dummy variables.

**5.3 Ollama Testing**  

* Prepares a request payload for generating embeddings.  
* Sends POST request to Ollama’s embedding API.


As we can see we get 768 dimensional vectors using Ollama nomic-embed-text and the vectorization of the first 5 values is also printed. 


