from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

def calculate_total_bill(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative")
    return round(price * quantity, 2)

def calculate_discounted_total(price, quantity, discount_percent):
    subtotal = calculate_total_bill(price, quantity)
    discount_amount = subtotal * (discount_percent / 100)
    final_total = subtotal - discount_amount

    return {
        "subtotal": round(subtotal, 2),
        "discount_percent": discount_percent,
        "discount_amount": round(discount_amount, 2),
        "final_total": round(final_total, 2)
    }

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

                <label>Discount (%):</label><br>
                <input type="number" name="discount_percent" min="0" max="100" value="0" required><br><br>

                <button type="submit">Calculate Bill</button>
            </form>
        </body>
    </html>
    """)

@app.route("/bill", methods=["POST"])
def bill():
    price = float(request.form["price"])
    quantity = int(request.form["quantity"])
    discount_percent = float(request.form.get("discount_percent", 0))

    result = calculate_discounted_total(price, quantity, discount_percent)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)