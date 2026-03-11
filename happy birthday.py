from flask import Flask

app = Flask(__name__)

@app.route('/')
def birthday_greeting():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Happy Birthday! 🎂</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;600&display=swap');

            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                overflow: hidden;
            }

            /* Floating Background Elements */
            .bg-circles {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
            }

            .circle {
                position: absolute;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 50%;
                animation: float 10s infinite linear;
            }

            @keyframes float {
                0% { transform: translateY(100vh) scale(0); opacity: 0; }
                50% { opacity: 0.5; }
                100% { transform: translateY(-10vh) scale(1.5); opacity: 0; }
            }

            /* Main Card */
            .card {
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(15px);
                -webkit-backdrop-filter: blur(15px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                padding: 3rem;
                border-radius: 30px;
                text-align: center;
                box-shadow: 0 25px 45px rgba(0,0,0,0.2);
                color: white;
                max-width: 500px;
                animation: fadeIn 1.5s ease-out;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }

            h1 {
                font-family: 'Pacifico', cursive;
                font-size: 3.5rem;
                margin: 0;
                background: linear-gradient(to right, #fff, #ffd700);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            p {
                font-size: 1.2rem;
                line-height: 1.8;
                font-weight: 300;
                margin-top: 20px;
            }

            .highlight {
                color: #ffd700;
                font-weight: 600;
            }

            .emoji-row {
                font-size: 2.5rem;
                margin-top: 25px;
                letter-spacing: 15px;
            }
        </style>
    </head>
    <body>
        <div class="bg-circles">
            <div class="circle" style="width: 80px; height: 80px; left: 10%; animation-delay: 0s;"></div>
            <div class="circle" style="width: 40px; height: 40px; left: 30%; animation-delay: 2s;"></div>
            <div class="circle" style="width: 120px; height: 120px; left: 70%; animation-delay: 4s;"></div>
            <div class="circle" style="width: 60px; height: 60px; left: 85%; animation-delay: 1s;"></div>
        </div>

        <div class="card">
            <h1>Happy Birthday!</h1>
            <p>
                Wishing you a truly <span class="highlight">magnificent year</span> ahead! 
                May every moment be filled with joy, laughter, and 
                <span class="highlight">beautiful memories</span> that last a lifetime.
            </p>
            <div class="emoji-row">✨🎂🎉🥂</div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()