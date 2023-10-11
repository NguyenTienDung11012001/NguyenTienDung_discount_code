from odoo import fields, models, api, _
import re


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_discount_code = fields.Char(string='Discount Code', groups='discount_code.advanced_sale_group_user')
    is_code_valid = fields.Char(string='Is Discount Code Valid', compute='_compute_valid_code', store=True)

    @api.depends('customer_discount_code')
    def _compute_valid_code(self):
        pattern = r'^VIP_(?:[1-9]\d?|100)$'
        for rec in self:
            if rec.customer_discount_code:
                match = re.match(pattern, rec.customer_discount_code)
                if match:
                    rec.is_code_valid = 'valid'
                else:
                    rec.is_code_valid = 'invalid'
            else:
                rec.is_code_valid = False
