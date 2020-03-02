import logging

from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class Applicant(models.Model):
    _inherit = 'hr.applicant'

    @api.multi
    def action_start_survey(self):
        self.ensure_one()
        # create a response and link it to this applicant
        if not self.response_id:
            response = self.env['survey.user_input'].create(
                {'survey_id': self.survey_id.id,
                 'partner_id': self.partner_id.id,
                 'kw_hr_job_id': self.job_id.id,
                 })
            self.response_id = response.id
        else:
            response = self.response_id
        # grab the token of the response and start surveying
        return self.survey_id.with_context(
            survey_token=response.token).action_start_survey()

    @api.model
    def create(self, vals):
        if vals.get('partner_name') and vals.get('email_from'):
            partner = self.env['res.partner'].create({
                'name': vals.get('partner_name'),
                'email': vals.get('email_from'),
                'phone': vals.get('partner_phone'), })
            vals['partner_id'] = partner.id
        return super().create(vals)
