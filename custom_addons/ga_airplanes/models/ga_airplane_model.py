from odoo import models, fields

class AirplaneModel(models.Model):
    _name = 'ga.airplane.model'

    name = fields.Char(string='Name', required=True)
    provider = fields.Char(string='Provider')