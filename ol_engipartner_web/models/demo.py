from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta
import base64
import requests
import datetime
from odoo.exceptions import ValidationError


class businessunit(models.Model):
    _name='business.unit'
    name = fields.Char(string='name')

class rooftype(models.Model):
    _name='roof.type'
    name = fields.Char(string='name')

class rooftypematerial(models.Model):
    _name='rooftype.material'
    name = fields.Char(string='name')

class rockingbrand(models.Model):
    _name='rocking.brand'
    name = fields.Char(string='name')

class attachmentbrand(models.Model):
    _name='attachment.brand'
    name = fields.Char(string='name')

class sealandbrand(models.Model):
    _name='sealand.brand'
    name = fields.Char(string='name')


class methodpreference(models.Model):
    _name='method.preference'
    name = fields.Char(string='name')

class pvmodule(models.Model):
    _name='pv.module'
    name = fields.Char(string='name')

class modulebattery(models.Model):
    _name='module.battery'
    name = fields.Char(string='name')


class batteryspecificatio(models.Model):
    _name = 'battery.specification'
    name = fields.Char(string='name')

class specificationinver(models.Model):
    _name = 'specification.inverter'
    name = fields.Char(string='name')

class secondinver(models.Model):
    _name = 'second.inverter'
    name = fields.Char(string='name')

class documenttype(models.Model):
    _name = 'document.type'
    name = fields.Char(string='name')

class stamptype(models.Model):
    _name = 'stamp.type'
    name = fields.Char(string='name')

class revisionsubmission(models.Model):
    _name = 'revision.submission'
    name = fields.Char(string='name')


class stamptypedoc(models.Model):
    _name = 'stamp.typedoc'
    name = fields.Char(string='name')









class inheritincompany(models.Model):
    _inherit = 'project.project'

    external_id = fields.Char(string='Project External ID', required=False, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    address = fields.Char(string='Address')
    city = fields.Char(string='City')
    utility = fields.Char(string='Utility')
    external_links = fields.Char(string='External Links')

    country = fields.Many2one('res.country')
    state = fields.Many2one('res.country.state')
    jurisdiction = fields.Char(string='Authority Having Jurisdiction')
    business_unit=fields.Many2one('business.unit', string='Business Unit')
    roof_type = fields.Many2one('roof.type', string='Roof Type')
    roof_type_material = fields.Many2one('rooftype.material',string='Roof Type Material')
    rocking_brand = fields.Many2one('rocking.brand',string='Rocking Brand')
    attachment_brand = fields.Many2one('attachment.brand',string='Attachment Brand')
    sealand_brand = fields.Many2one('sealand.brand',string='Sealand Brand')
    other_comments = fields.Char(string='Other Comments')
    method_preference= fields.Many2one('method.preference', string='Interconnection Method Preference:')
    main_bus = fields.Char(string='Main Bus Bar Rating')
    main_breaker = fields.Char(string='Main Breaker Rating')
    pv_module= fields.Many2one('pv.module', string='PV Module')
    battery= fields.Many2one('module.battery', string='Battery')
    module_quantity = fields.Char(string='Module Quantity')
    battery_spec = fields.Many2one('battery.specification', string='Battery Specification')
    inverter = fields.Many2one('specification.inverter', string='Inverter')
    sec_inverter = fields.Many2one('second.inverter', string='Second Inverter')
    inverter_quantity = fields.Char(string='Inverter Quantity')
    sec_quantity = fields.Char(string='Second Inverter Quantity')
    doc_type = fields.Many2one('document.type', string='Document Type')
    stamp_type = fields.Many2one('stamp.type', string='Stamp Type')
    revision_submission = fields.Many2one('revision.submission', string='Revision Type')
    revision_comment = fields.Char(string='Revision Comment')
    file_attachment = fields.Binary(string='Attachment')
    permit_number = fields.Char(string='Permit Number')
    installation_date = fields.Date(string='Installation Date')
    inspection_date = fields.Date(string='Inspection Date')
    special_req = fields.Char(string='Special Request')
    upload_doc = fields.Binary(string='Attachment')
    another_battery = fields.Boolean(string= 'Battery')
    ballasted = fields.Boolean(string= 'Ballasted')
    canopy = fields.Boolean(string= 'Canopy')
    generator = fields.Boolean(string= 'Generator')
    kw = fields.Boolean(string= 'KW')
    greater = fields.Boolean(string= 'Greater than 11.5 kW DC')
    than = fields.Boolean(string= 'Greater than 15 kW DC')
    groundmount = fields.Boolean(string= 'Groundmount')
    solar = fields.Boolean(string= 'Solar')
    naa = fields.Boolean(string= 'N/A')
    stamp_type_doc = fields.Many2one('stamp.typedoc', string='Stamp Type')
    other_commments_doc = fields.Char(string='Other Comments')
    eng_plans = fields.Boolean(string='Engineering Plans')
    eng_letter = fields.Boolean(string='Engineering Letters')
    inspection_form = fields.Boolean(string='Inspection Form')
    cvc_permit = fields.Boolean(string='CVC Permit')
    ec_permit = fields.Boolean(string='EC Permit')
    coi = fields.Boolean(string='COI')

    # sequence field fuction in car inspection form
    @api.model
    def create(self, vals):
        # print(vals.get('name_seq'))
        if vals.get('external_id', _('New')) == _('New'):
            vals['external_id'] = self.env['ir.sequence'].next_by_code('project.project') or _('New')
        result = super(inheritincompany, self).create(vals)
        return result








    @api.onchange('country')
    def set_values_to(self):
        if self.country:
            ids = self.env['res.country.state'].sudo().search([('country_id', '=', self.country.id)])
            return {
                'domain': {'state': [('id', 'in', ids.ids)], }
            }
