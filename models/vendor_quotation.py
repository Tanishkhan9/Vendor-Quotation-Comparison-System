from odoo import models, fields


class VendorQuotation(models.Model):
    _name = "vendor.quotation"
    _description = "Vendor Quotation"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string="Quotation Number",
        required=True,
        copy=False,
        readonly=True,
        default="New"
    )

    vendor_id = fields.Many2one(
        "res.partner",
        string="Vendor",
        required=True
    )

    product_id = fields.Many2one(
        "product.product",
        string="Product",
        required=True
    )

    quantity = fields.Float(
        default=1
    )

    unit_price = fields.Float()

    quotation_date = fields.Date()

    delivery_days = fields.Integer()

    warranty_months = fields.Integer()

    notes = fields.Text()

    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default="draft")
