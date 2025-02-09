from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_invoice(invoice_number, customer_name, items, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)
    
    # Invoice Title - Centered, Bold, and Underlined
    c.drawCentredString(300, 750, "INVOICE")
    c.line(200, 745, 400, 745)
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 710, f"Invoice Number: {invoice_number}")
    c.drawString(100, 690, f"Customer Name: {customer_name}")
    
    # Table Headers
    c.drawString(100, 660, "S.No")
    c.drawString(150, 660, "Item")
    c.drawString(300, 660, "Quantity")
    c.drawString(400, 660, "Price")
    
    y = 640
    total_amount = 0
    for idx, (item, quantity, price) in enumerate(items, start=1):
        c.drawString(100, y, str(idx))
        c.drawString(150, y, item)
        c.drawString(300, y, str(quantity))
        c.drawString(400, y, f"${price:.2f}")
        total_amount += quantity * price
        y -= 20
    
    # Total Amount
    c.drawString(100, y-20, f"Total Amount: ${total_amount:.2f}")
    
    c.save()
    print(f"Invoice {filename} generated successfully.")
    print(f"Total Amount: ${total_amount:.2f}")

# Get Invoice Details
filename = input("Enter file name: ")
filename += ".pdf"
invoice_number = input("Enter invoice number: ")
customer_name = input("Enter customer name: ")

# User Input for Items
items = []
while True:
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    items.append((item, quantity, price))
    choice = input("Do you want to add another item? (y/n): ").strip().lower()
    if choice != 'y':
        break

# Generate Invoice
generate_invoice(invoice_number, customer_name, items, filename)
    
