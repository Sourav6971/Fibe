from flask import Flask, request, render_template, redirect, url_for
from main import category

app = Flask(__name__)

# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle article submission
@app.route('/submit-article', methods=['POST'])
def submit_article():
    global article  
    article = request.form['article']  # Get article from the form
    return redirect(url_for('thank_you'))  # Redirect to thank_you route

# Route to display prediction and render the index.html page with prediction
@app.route('/thank-you', methods=['GET'])
def thank_you():
    prediction = category(article=article)  # Get prediction based on the article
    # Render the index.html with the prediction to display
    return render_template('index.html', prediction=prediction[0])

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
