from odoo import http
from odoo.http import request
from odoo import models, fields, api
from odoo.exceptions import UserError
import base64
import requests


class viewurproject(http.Controller):

    @http.route(['/viewurproject'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        project_byproject_rec = request.env['project.project'].sudo().search([])

        return request.render('ol_engipartner_web.viewurproject', {'project_byproject_rec': project_byproject_rec, })

class viewurprojectform(http.Controller):

    @http.route(['/viewurprojectform'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        request.session['project_byproject'] = post.get('project_byproject')
        print('babo',post.get('project_byproject'))
        projecct = request.env['project.project'].search([('id', '=', post.get('project_byproject'))])
        request.session['name'] = projecct.name
        request.session['city'] = projecct.city
        request.session['address'] = projecct.address
        request.session['state'] = projecct.state.name
        request.session['country'] = projecct.country.name
        request.session['authority']=projecct.jurisdiction
        request.session['external'] = projecct.external_id
        request.session['utility'] = projecct.utility
        request.session['link'] = projecct.external_links
        request.session['business_unit'] = projecct.business_unit.name
        request.session['rooftype'] = projecct.roof_type.name
        request.session['rooftype_material'] = projecct.roof_type_material.name
        request.session['rocking_brand']=projecct.rocking_brand.name
        request.session['attachment_brand'] = projecct.attachment_brand.name
        request.session['sealand_brand'] = projecct.sealand_brand.name
        request.session['comments'] = projecct.other_comments
        request.session['busbaarrating'] = projecct.main_bus
        request.session['methodpreference'] = projecct.method_preference.name
        request.session['mainbreaker'] = projecct.main_breaker
        request.session['pv_module'] = projecct.pv_module.name
        request.session['module_battery'] = projecct.battery.name
        request.session['modulequantity'] = projecct.module_quantity
        request.session['specificationinverter'] = projecct.inverter.name
        request.session['second_inverter'] = projecct.sec_inverter.name
        request.session['inverterquantity'] = projecct.inverter_quantity
        request.session['secondinverterquantity'] = projecct.sec_quantity
        request.session['batteryspecification'] = projecct.battery_spec.name
        request.session['special'] = projecct.special_req

        print(request.session['module_battery'])
        # print(request.session['city'])
        # print(request.session['address'])
        # print(request.session['state'])
        # print(request.session['country'])
        # print(request.session['authority'])
        # print(request.session['external'])
        # print(request.session['utility'])
        # print(request.session['link'])
        # print(request.session['business_unit'])
        # print(request.session['rooftype'])
        # print(request.session['rooftype_material'])
        # print(request.session['attachment_brand'])
        # print(request.session['sealand_brand'])
        # print(request.session['comments'])
        # print(request.session['busbaarrating'])
        # print(request.session['methodpreference'])
        # print(request.session['mainbreaker'])
        # print(request.session['pv_module'])
        # print(request.session['module_battery'])
        # print(request.session['modulequantity'])
        # print(request.session['specificationinverter'])
        # print(request.session['second_inverter'])
        # print(request.session['inverterquantity'])
        # print(request.session['secondinverterquantity'])
        # print(request.session['batteryspecification'])
        # print(request.session['batteryspecification'])
        # print(request.session['special'])


        return request.render('ol_engipartner_web.viewurprojectform')
