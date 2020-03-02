import logging

from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    kw_hr_job_id = fields.Many2one(
        comodel_name='hr.job',
        string='Applied Job', )
