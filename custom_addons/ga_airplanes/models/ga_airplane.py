from jinja2.utils import consume

from odoo import models, fields, api

class Airplane(models.Model):
    _name = 'ga.airplane'
    _rec_name = 'registration_number'

    capacity = fields.Integer(string='Capacity', required=True, default=100)
    manufacture_date = fields.Date()
    airplane_model_id = fields.Many2one(comodel_name='ga.airplane.model')
    airline_id = fields.Many2one(comodel_name='ga.airline')
    registration_number = fields.Char(required=True)
    consumption_per_hour = fields.Float()
    flied_hours = fields.Integer()
    total_consumption = fields.Float(compute='_compute_total_consumption', store=True)

    @api.depends('flied_hours', 'consumption_per_hour')
    def _compute_total_consumption(self):
        for plane in self:
            plane.total_consumption = plane.consumption_per_hour * plane.flied_hours

