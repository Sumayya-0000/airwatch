from flask import Flask

app = Flask(__name__)

# Sample data for demonstration only
readings = [
    {"city": "Hyderabad", "aqi": 85, "pm25": 28, "pm10": 55},
    {"city": "Delhi", "aqi": 165, "pm25": 78, "pm10": 120},
    {"city": "Bengaluru", "aqi": 48, "pm25": 15, "pm10": 30},
]


def page(title, content):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title} | AirWatch</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                background: #eef5f2;
                color: #20332d;
            }}
            header {{
                background: #176b55;
                color: white;
                padding: 22px;
                text-align: center;
            }}
            nav {{
                background: #104b3c;
                padding: 14px;
                text-align: center;
            }}
            nav a {{
                color: white;
                text-decoration: none;
                margin: 12px;
            }}
            main {{
                max-width: 900px;
                margin: 25px auto;
                padding: 20px;
            }}
            .card {{
                background: white;
                padding: 20px;
                margin: 12px 0;
                border-radius: 10px;
                box-shadow: 0 2px 7px #cccccc;
            }}
            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 12px;
            }}
            .value {{
                font-size: 30px;
                font-weight: bold;
                color: #176b55;
            }}
            footer {{
                text-align: center;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>AirWatch</h1>
            <p>Air Quality Monitoring System</p>
        </header>
        <nav>
            <a href="/">Home</a>
            <a href="/monitoring">Live Monitoring</a>
            <a href="/about">About & Health Tips</a>
        </nav>
        <main>{content}</main>
        <footer>AirWatch | Educational Demonstration Project</footer>
    </body>
    </html>
    """


@app.route("/")
def home():
    content = """
    <div class="card">
        <h2>Welcome to AirWatch</h2>
        <p>Monitor air quality indicators and understand pollution levels.</p>
        <p><strong>Notice:</strong> All readings shown are sample data,
        not real-time sensor measurements.</p>
    </div>

    <div class="grid">
        <div class="card">
            <h3>Hyderabad AQI</h3>
            <div class="value">85</div>
            <p>Moderate (US AQI scale)</p>
        </div>
        <div class="card">
            <h3>PM2.5</h3>
            <div class="value">28</div>
            <p>µg/m³</p>
        </div>
        <div class="card">
            <h3>PM10</h3>
            <div class="value">55</div>
            <p>µg/m³</p>
        </div>
    </div>
    """
    return page("Home", content)


@app.route("/monitoring")
def monitoring():
    rows = ""

    for item in readings:
        rows += f"""
        <tr>
            <td>{item['city']}</td>
            <td>{item['aqi']}</td>
            <td>{item['pm25']}</td>
            <td>{item['pm10']}</td>
        </tr>
        """

    content = f"""
    <div class="card">
        <h2>Air Quality Monitoring</h2>
        <p>Sample readings for three cities.</p>
        <table border="1" cellpadding="12"
               cellspacing="0" width="100%">
            <tr>
                <th>City</th>
                <th>AQI</th>
                <th>PM2.5 (µg/m³)</th>
                <th>PM10 (µg/m³)</th>
            </tr>
            {rows}
        </table>
        <p>Readings are simulated for demonstration purposes.</p>
    </div>
    """
    return page("Monitoring", content)


@app.route("/about")
def about():
    content = """
    <div class="card">
        <h2>About AirWatch</h2>
        <p>AirWatch demonstrates how air quality indicators can
        be displayed through a web application.</p>
        <p>AQI summarizes air pollution using a scale defined by
        the applicable air quality standard.</p>
    </div>

    <div class="card">
        <h2>Air Quality Tips</h2>
        <ul>
            <li>Check official air quality advisories.</li>
            <li>Reduce strenuous outdoor activity when pollution is high.</li>
            <li>Keep indoor spaces well ventilated when outdoor air is clean.</li>
            <li>Consider a suitable air purifier when needed.</li>
            <li>Follow local public health recommendations.</li>
        </ul>
    </div>

    <div class="card">
        <h2>Technologies Used</h2>
        <p>Python, Flask, Docker, Kubernetes, Jenkins and GitHub.</p>
    </div>
    """
    return page("About", content)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)