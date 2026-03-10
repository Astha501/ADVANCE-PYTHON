import json
from datetime import datetime
from pathlib import Path

CATALOG = {
    "1001": ("Apple", 0.50),
    "1002": ("Banana", 0.30),
    "2001": ("Milk", 1.20),
}

TRANSACTIONS_FILE = Path(r"d:/Advance Python/transactions.json")


class BillingSystem:
    def __init__(self, catalog=None):
        self.catalog = catalog or {}
        self.cart = []  # list of (sku, qty)

    def scan(self, sku, qty=1):
        sku = str(sku)
        if sku not in self.catalog:
            raise KeyError(f"SKU not found: {sku}")
        qty = int(qty)
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        self.cart.append((sku, qty))

    def compute(self, coupon_percent=0):
        lines = []
        subtotal = 0.0
        for sku, qty in self.cart:
            name, price = self.catalog[sku]
            line_total = price * qty
            subtotal += line_total
            lines.append({"sku": sku, "name": name, "unit_price": price, "qty": qty, "line_total": round(line_total, 2)})

        coupon_percent = float(coupon_percent or 0)
        discount = round(subtotal * (coupon_percent / 100.0), 2) if coupon_percent > 0 else 0.0
        total = round(subtotal - discount, 2)

        return {"lines": lines, "subtotal": round(subtotal, 2), "discount": discount, "total": total, "coupon_percent": coupon_percent if discount > 0 else None}

    def print_bill(self, totals):
        print("RECEIPT")
        print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("-" * 30)
        for ln in totals["lines"]:
            print(f"{ln['name']} x{ln['qty']} @ {ln['unit_price']:.2f} = {ln['line_total']:.2f}")
        print("-" * 30)
        print(f"Subtotal: {totals['subtotal']:.2f}")
        if totals["discount"] > 0:
            print(f"Discount ({totals['coupon_percent']}%): -{totals['discount']:.2f}")
        print(f"TOTAL: {totals['total']:.2f}")

    def record(self, totals):
        rec = {"timestamp": datetime.now().isoformat(), "cart": self.cart.copy(), "totals": totals}
        data = []
        try:
            if TRANSACTIONS_FILE.exists():
                with open(TRANSACTIONS_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
        except Exception:
            data = []
        data.append(rec)
        with open(TRANSACTIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def clear(self):
        self.cart = []


if __name__ == '__main__':
    b = BillingSystem(catalog=CATALOG)
    # basic demo
    try:
        b.scan("1001", 3)
        b.scan("2001", 1)
    except KeyError as e:
        print(e)

    totals = b.compute(coupon_percent=10)  
    b.print_bill(totals)
    b.record(totals)
    b.clear()