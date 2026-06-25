# Vendor-Quotation-Comparison-System

Vendor Management

↓

Product Selection

↓

Vendor submits quotation

↓

Compare quotations

↓

Recommend Best Vendor

↓

Approve Quotation

↓

Generate Purchase Summary


Project Structure
vendor_quotation_management/
│
├── __init__.py
├── __manifest__.py
│
├── models/
│   ├── __init__.py
│   ├── vendor.py
│   ├── quotation.py
│   └── comparison.py
│
├── views/
│   ├── vendor_views.xml
│   ├── quotation_views.xml
│   ├── comparison_views.xml
│   └── menu.xml
│
├── security/
│   └── ir.model.access.csv
│
├── data/
│   └── sequence.xml
│
└── static/
    └── description/
        └── icon.png
Database Models

Instead of creating our own vendor table, we'll reuse Odoo's existing models.

Existing Odoo Models
res.partner      → Vendor

product.product  → Product

res.currency     → Currency

res.users        → Employee

This is how professional Odoo developers work.

New Model
vendor.quotation

Fields

Quotation Number

Vendor

Product

Quantity

Unit Price

Delivery Days

Warranty

Status

Quotation Date

Total Amount
Another Model
quotation.comparison

Stores

Product

Best Vendor

Lowest Price

Highest Price

Average Price

Savings
Workflow
Vendor A

↓

Laptop

↓

₹52,000


Vendor B

↓

Laptop

↓

₹49,500


Vendor C

↓

Laptop

↓

₹50,000


↓

Compare

↓

Recommend Vendor B

↓

Approve

↓

Generate Purchase Report
Business Logic

The comparison model will calculate

Minimum Price

Maximum Price

Average Price

Savings

Recommended Vendor

using Odoo ORM.
