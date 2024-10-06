from odoo import models, fields

class Airport(models.Model):
    _name = 'ga.airport'

    name = fields.Char(string='Airport Name', required=True)
    country_id = fields.Many2one(string='Country', comodel_name='res.country')
