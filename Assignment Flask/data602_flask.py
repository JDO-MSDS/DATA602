from flask import Flask, request

app = Flask(__name__)

main_page = '''
<html>
    <head>
    <title>Multiplier</title>
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    </head>
<body>
<form class="form-horizontal" method="post" action="/calc">
<fieldset>
<legend>Multiplier</legend>

<div class="form-group">
  <label class="col-md-4 control-label">Number</label>  
  <div class="col-md-4">
    <input type="number" name="number" placeholder="Enter a number" class="form-control input-md">
  </div>
</div>

<div class="form-group">
  <div class="col-md-4 col-md-offset-4">
    <button class="btn btn-primary">Calculate</button>
  </div>
</div>

</fieldset>
</form>
</body>
</html>
'''

@app.route("/", methods=["GET"])
def index():
    return main_page

@app.route("/calc", methods=["POST"])
def calculate():
    number = request.form.get("number", type=float)

    if number is None:
        return "<h3>Please enter a valid number.</h3>"

    result = number * 5

    return f"""
    <html>
        <body>
            <h3>Result</h3>
            <p>{number} × 5 = <strong>{result}</strong></p>
            <a href="/">Go back</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
