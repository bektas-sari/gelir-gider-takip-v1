from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 1-31 arası günlük bakiye tutulacak (index 0 kullanılmayacak)
daily_balance = [0] * 32

# İşlemleri sakladığımız liste (her eleman: {'day': int, 'desc': str, 'amount': float})
transactions = []

def recalc_daily_balance():
    """Tüm işlemleri baz alarak 1..31 günleri için daily_balance dizisini sıfırdan hesaplar."""
    for i in range(1, 32):
        daily_balance[i] = 0
    
    sorted_tx = sorted(transactions, key=lambda x: x['day'])
    for tx in sorted_tx:
        day = tx['day']
        amount = tx['amount']
        for i in range(day, 32):
            daily_balance[i] += amount

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Gün değerini alırken kontrol ediyoruz
        day_str = request.form.get("day")
        if not day_str or day_str.strip() == "":
            return "Hata: Gün değeri eksik", 400
        try:
            day = int(day_str)
        except ValueError:
            return "Hata: Gün değeri sayı olmalı", 400

        # Açıklama kontrolü
        desc = request.form.get("desc")
        if not desc or desc.strip() == "":
            return "Hata: Açıklama eksik", 400

        # Miktar kontrolü
        amount_str = request.form.get("amount")
        if not amount_str or amount_str.strip() == "":
            return "Hata: Miktar değeri eksik", 400
        try:
            amount = float(amount_str)
        except ValueError:
            return "Hata: Miktar sayı olmalı", 400

        # İşlem türünü al (income veya expense)
        tx_type = request.form.get("type")
        if tx_type not in ["income", "expense"]:
            return "Hata: İşlem türü eksik veya hatalı", 400

        # Giderse miktarı negatif yap
        if tx_type == "expense":
            amount = -abs(amount)
        else:
            amount = abs(amount)

        # İşlemi ekle
        transactions.append({"day": day, "desc": desc, "amount": amount})
        recalc_daily_balance()

    return render_template("index.html", transactions=transactions)

@app.route("/data", methods=["GET"])
def data():
    days = list(range(1, 32))
    return jsonify({
        "days": days,
        "balances": daily_balance[1:]
    })

if __name__ == "__main__":
    app.run(debug=True)
