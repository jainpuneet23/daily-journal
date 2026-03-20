import csv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_journal():
    rows = []
    with open("journal.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    table_rows = ""
    for row in rows:
        table_rows += f"<tr><td>{row['date']}</td><td>{row['feeling']}</td><td>{row['mood_score']}</td></tr>"

    html = f"""
    <html>
    <body>
        <h1>My Daily Journal</h1>
        <table border="1">
            <tr><th>Date</th><th>Feeling</th><th>Mood Score</th></tr>
            {table_rows}
        </table>
    </body>
    </html>
    """
    return html
