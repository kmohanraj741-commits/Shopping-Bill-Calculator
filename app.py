from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

def calculate_total_bill(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative")
    return round(price * quantity, 2)

@app.route("/", methods=["GET"])
def index():
    return render_template_string("""
    <html>
        <body style="font-family: Arial; margin: 40px;">
            <h2>Shopping Bill Calculator</h2>
            <form method="POST" action="/bill">
                <label>Price:</label><br>
                <input type="number" name="price" step="0.01" required><br><br>

                <label>Quantity:</label><br>
                <input type="number" name="quantity" min="1" required><br><br>

                <button type="submit">Calculate Total</button>
            </form>
        </body>
    </html>
    """)

@app.route("/bill", methods=["POST"])
def bill():
    price = float(request.form["price"])
    quantity = int(request.form["quantity"])
    total = calculate_total_bill(price, quantity)
    return jsonify({
        "price": price,
        "quantity": quantity,
        "total_bill": total
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)