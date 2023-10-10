from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_order_discount_estimated = fields.Float(string="Discount Estimated", compute='_compute_discount')
    customer_discount_code = fields.Char(string="Discount Code", related='partner_id.customer_discount_code')
 

    @api.depends('partner_id', 'order_line')
    def _compute_discount(self):
        code = self.partner_id.customer_discount_code
        if code != 'None':
            if self.partner_id.is_code_valid == 'valid':
                start_index = code.find("_") + 1
                perc = code[start_index:]
                for rec in self.order_line:
                    rec.discount_estimated = rec.price_subtotal * int(perc) / 100
                self.sale_order_discount_estimated = self.amount_total * int(perc) / 100
            else:
                for rec in self.order_line:
                    rec.discount_estimated = 0
                self.sale_order_discount_estimated = 0
        else:
            self.sale_order_discount_estimated = 0

        message = 'Applied'
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'info',
                'sticky': True,
                'message': message,
            }
        }


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_estimated = fields.Float(string="Discount")
