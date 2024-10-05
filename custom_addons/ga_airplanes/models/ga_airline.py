from odoo import models, fields

class Airline(models.Model):
    _name = 'ga.airline'

    name = fields.Char(string='Name', required=True)
    country_id = fields.Many2one(string='Country', comodel_name='res.country')
