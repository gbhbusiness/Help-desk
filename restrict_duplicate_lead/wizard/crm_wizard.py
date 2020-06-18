# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class CrmLeadWizard(models.TransientModel):

    _name = 'crm.lead.wizard'
    _description = 'Crm Lead Wizard'

    partner_id = fields.Many2one('res.partner', 'Customer')
    lead_id = fields.Many2one('crm.lead', 'Lead')
    note = fields.Char()
