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
    age = fields.Integer(compute='_compute_age')
    fuel_capacity = fields.Float()
    max_flight_time = fields.Integer(compute='_compute_max_flight_time', store=True)
    state = fields.Selection([
        ('active', 'Activo'),
        ('inactive', 'Inactivo'),
        ('maintenance', 'Mantenimiento'),
    ], default='active')

    @api.depends('flied_hours', 'consumption_per_hour')
    def _compute_total_consumption(self):
        for plane in self:
            plane.total_consumption = plane.consumption_per_hour * plane.flied_hours

    @api.depends('manufacture_date')
    def _compute_age(self):
        for plane in self:
            if plane.manufacture_date:
                current_year = fields.Date().today().year
                plane.age = current_year - plane.manufacture_date.year
            else:
                plane.age = 0

    @api.depends('consumption_per_hour', 'fuel_capacity')
    def _compute_max_flight_time(self):
        for plane in self:
            if plane.consumption_per_hour > 0:
                plane.max_flight_time = plane.fuel_capacity / plane.consumption_per_hour
            else:
                plane.max_flight_time = 0