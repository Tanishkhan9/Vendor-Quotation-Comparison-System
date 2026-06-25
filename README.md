# Vendor-Quotation-Comparison-System

A comprehensive Odoo module for managing vendor quotations and comparing them to find the best vendor for your procurement needs.

## Workflow Overview

```
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
```

## Project Structure

```
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
```

## Database Models

### Existing Odoo Models (Reused)

Instead of creating our own vendor table, we reuse Odoo's existing models:

| Model | Purpose |
|-------|---------|
| `res.partner` | Vendor |
| `product.product` | Product |
| `res.currency` | Currency |
| `res.users` | Employee |

*This is how professional Odoo developers work.*

### New Models

#### vendor.quotation

**Fields:**
- Quotation Number
- Vendor
- Product
- Quantity
- Unit Price
- Delivery Days
- Warranty
- Status
- Quotation Date
- Total Amount

#### quotation.comparison

**Fields:**
- Product
- Best Vendor
- Lowest Price
- Highest Price
- Average Price
- Savings

## Example Workflow

### Scenario: Laptop Procurement

| Vendor | Product | Price |
|--------|---------|-------|
| Vendor A | Laptop | ₹52,000 |
| Vendor B | Laptop | ₹49,500 |
| Vendor C | Laptop | ₹50,000 |

**Process:**
1. Compare quotations from all vendors
2. Recommend Vendor B (lowest price)
3. Approve the quotation
4. Generate Purchase Report

## Business Logic

The comparison model automatically calculates:

- **Minimum Price** - Lowest quoted price
- **Maximum Price** - Highest quoted price
- **Average Price** - Mean of all quotations
- **Savings** - Amount saved by selecting best vendor
- **Recommended Vendor** - Best option based on criteria

All calculations are performed using Odoo ORM for reliable and efficient processing.

---

*For more information on Odoo development, visit the [official Odoo documentation](https://www.odoo.com/documentation)*
