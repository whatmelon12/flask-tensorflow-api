---


---

<h1 id="welcome-to-dog-breed---flask-tensor-flow-api">Welcome to Dog Breed - Flask Tensor Flow API!</h1>
<p>This project implements a  RESTful API using <strong>Flask</strong>, a python web framework, to analize an input image using a  <strong>Tensor Flow</strong> graph, and return its score based on the <strong>120 dog breeds</strong> that were used to train the last layer of the <a href="https://github.com/tensorflow/models/tree/master/research/inception"><strong>Inception Model V3</strong></a> provided by Google.</p>
<h2 id="dependencies">Dependencies</h2>
<p>The main two dependencies of the project are the <a href="https://www.tensorflow.org/">Tensor Flow</a> library, and <a href="https://opencv.org/">OpenCV</a> a library to handle images.</p>
<p>To install all dependencies of this projects run the following command:</p>
<pre><code>pip install -r requirements.txt
</code></pre>
<h2 id="run-the-project">Run the project</h2>
<p>Execute the <code>app.py</code> file from the console to start the Flask API.</p>

<table>
<thead>
<tr>
<th>Endpoint Path</th>
<th>Method</th>
<th>Body type</th>
<th>Returns</th>
</tr>
</thead>
<tbody>
<tr>
<td>api/dogbreeds</td>
<td>GET</td>
<td>None</td>
<td>List of available dog breeds</td>
</tr>
<tr>
<td>api/uploadtest</td>
<td>POST</td>
<td>Multipart Form (image)</td>
<td>Analysis result</td>
</tr>
</tbody>
</table>
