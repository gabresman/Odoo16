from odoo import models, fields

class Airplane(models.Model):
    _name = 'ga.airplane'
    _rec_name = 'registration_number'

    capacity = fields.Integer(string='Capacity', required=True, default=100)
    manufacture_date = fields.Date()
    airplane_model_id = fields.Many2one(comodel_name='ga.airplane.model')
    airline_id = fields.Many2one(comodel_name='ga.airline')
    registration_number = fields.Char(required=True)