from odoo import api, fields, models, tools, _


class UpdateCodeWizard(models.TransientModel):
    _name = 'update.code.wizard'

    discount_code = fields.Char('Discount Code')

    def multi_update(self):
        ids = self.env.context['active_ids']  # selected record ids
        res_partner = self.env['res.partner'].browse(ids)
        new_data = {}

        if self.discount_code:
            new_data['customer_discount_code'] = self.discount_code

        res_partner.write(new_data)
