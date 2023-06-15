from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/inquiry')
def inquiry():
    return render_template('inquiry.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/drybag')
def drybag():
    return render_template('drybag.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # SMTP Configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'mohitphotoart1980@gmail.com'
    smtp_password = 'jljjrzsconxuopry'
    sender_email = 'mohitphotoart1980@gmail.com'
    receiver_email = 'Sbpenterprise2@gmail.com'

    # Construct email message
    subject = 'Form Submission'
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    message = f'Subject: {subject}\n\n{body}'

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

        return 'Form submitted successfully!'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
