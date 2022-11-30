from odoo import http
from odoo.http import request
from odoo import models, fields, api
from odoo.exceptions import UserError
import base64
import requests
import io


class newproject(http.Controller):

    @http.route(['/NewProject'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        return request.render('ol_engipartner_web.new_project')


class createproject(http.Controller):

    @http.route(['/createproject'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):

        request.session['projectlist'] = post.get('projectlist')
        print("hunain", post.get('projectlist'))
        request.session['option'] = post.get('option')
        print(post.get('option'))
        business_unit_rec = request.env['business.unit'].sudo().search([])
        state_rec = request.env['res.country.state'].sudo().search([('country_id', '=', 233)])
        country_rec = request.env['res.country'].sudo().search([('id', '=', 233) ])

        if post.get("projectlist") == 'newproject' or post.get("projectlist") == 'quote':
            print('ss')
            return request.render('ol_engipartner_web.create_new_project',
                                  {'business_unit_rec': business_unit_rec, 'state_rec': state_rec,
                                   'country_rec': country_rec})

        else:
            print("else")
            return request.render('ol_engipartner_web.add_documentation')


class roofspecifications(http.Controller):

    @http.route(['/roofspecifications'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        request.session['name'] = post.get('name')
        print(post.get('name'))
        request.session['city'] = post.get('city')
        print(post.get('city'))
        request.session['address'] = post.get('address')
        print(post.get('address'))
        request.session['state'] = post.get('state')
        print(post.get('state'))
        request.session['country'] = post.get('country')
        print(post.get('country'))
        request.session['authority'] = post.get('authority')
        print(post.get('authority'))
        request.session['external'] = post.get('external')
        print(post.get('external'))
        request.session['utility'] = post.get('utility')
        print(post.get('utility'))
        request.session['link'] = post.get('link')
        print(post.get('link'))
        request.session['business_unit'] = post.get('business_unit')
        print(post.get('business_unit'))

        # lead = {
        #     'name': post.get('name'),
        #     'address': post.get('address'),
        #     'city': post.get('city'),
        #     'utility': post.get('utility'),
        #     'external_id': post.get('external'),
        #     'external_links': post.get('link'),
        #     'jurisdiction': post.get('authority'),
        #     'business_unit': post.get('business_unit'),
        #
        # }
        #
        # leads = request.env['project.project'].create(lead)

        # print('value of lead is', leads)
        # request.session['leads'] = leads.id

        roof_type_rec = request.env['roof.type'].sudo().search([])
        rooftype_material_rec = request.env['rooftype.material'].sudo().search([])
        rockingbrand_type_rec = request.env['rocking.brand'].sudo().search([])
        attachment_brand_rec = request.env['attachment.brand'].sudo().search([])
        sealand_brand_rec = request.env['sealand.brand'].sudo().search([])

        return request.render('ol_engipartner_web.roofspecification',
                              {'roof_type_rec': roof_type_rec, 'rockingbrand_type_rec': rockingbrand_type_rec,
                               'rooftype_material_rec': rooftype_material_rec,
                               'attachment_brand_rec': attachment_brand_rec, 'sealand_brand_rec': sealand_brand_rec})


class interconnection(http.Controller):

    @http.route(['/interconnection_specification'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        request.session['rooftype'] = post.get('rooftype')
        print(post.get('rooftype'))
        request.session['rooftype_material'] = post.get('rooftype_material')
        print(post.get('rooftype_material'))
        request.session['attachment_brand'] = post.get('attachment_brand')
        print(post.get('attachment_brand'))
        request.session['sealand_brand'] = post.get('sealand_brand')
        print(post.get('sealand_brand'))
        request.session['comments'] = post.get('comments')
        print(post.get('comments'))
        request.session['rocking_brand'] = post.get('rocking_brand')
        print(post.get('rocking_brand'))

        # request.session['leads'] = post.get('leads')
        # print('checking', request.session['leads'])

        # anotherlead = {
        #
        #     'roof_type': post.get('rooftype'),
        #     'roof_type_material': post.get('rooftype_material'),
        #     'rocking_brand': post.get('rocking_brand'),
        #     'attachment_brand': post.get('attachment_brand'),
        #     'sealand_brand': post.get('sealand_brand'),
        #     'other_comments': post.get('comments'),
        #
        # }
        # print('hello', request.session['leads'])
        # anotherlead = request.env['project.project'].search([('id', '=', request.session['leads'])])
        # print("checkinggggg", request.session['leads'])
        #
        # anotherlead.write({
        #     'roof_type': post.get('rooftype'),
        #     'roof_type_material': post.get('rooftype_material'),
        #     'rocking_brand': post.get('rocking_brand'),
        #     'attachment_brand': post.get('attachment_brand'),
        #     'sealand_brand': post.get('sealand_brand'),
        #     'other_comments': post.get('comments'),
        #
        # })
        method_preference_rec = request.env['method.preference'].sudo().search([])

        return request.render('ol_engipartner_web.interconnection_specification',
                              {'method_preference_rec': method_preference_rec})


class module(http.Controller):

    @http.route(['/modulespecification'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        request.session['busbaarrating'] = post.get('busbaarrating')
        print(post.get('busbaarrating'))
        request.session['methodpreference'] = post.get('methodpreference')
        print(post.get('methodpreference'))
        request.session['mainbreaker'] = post.get('mainbreaker')
        print(post.get('mainbreaker'))

        # request.session['leads'] = post.get('leads')
        # print('checking', request.session['leads'])

        # secondlead = {
        #
        #     'main_bus': post.get('busbaarrating'),
        #     'main_breaker': post.get('mainbreaker'),
        #     'method_preference': post.get('methodpreference'),
        #
        # }
        # print('hello', request.session['leads'])
        # secondlead = request.env['project.project'].search([('id', '=', request.session['leads'])])
        # print("checkinggggg", request.session['leads'])
        #
        # secondlead.write({
        #     'main_bus': post.get('busbaarrating'),
        #     'main_breaker': post.get('mainbreaker'),
        #     'method_preference': post.get('methodpreference'),
        #
        # })

        pv_module_rec = request.env['pv.module'].sudo().search([])
        module_battery_rec = request.env['module.battery'].sudo().search([])
        battery_specification_rec = request.env['battery.specification'].sudo().search([])
        specification_inverter_rec = request.env['specification.inverter'].sudo().search([])
        second_inverter_rec = request.env['second.inverter'].sudo().search([])

        return request.render('ol_engipartner_web.modulespecification',
                              {'pv_module_rec': pv_module_rec, 'module_battery_rec': module_battery_rec,
                               'battery_specification_rec': battery_specification_rec,
                               'specification_inverter_rec': specification_inverter_rec,
                               'second_inverter_rec': second_inverter_rec})


class review_form(http.Controller):

    @http.route(['/review_form'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        request.session['pv_module'] = post.get('pv_module')
        print(post.get('pv_module'))
        request.session['module_battery'] = post.get('module_battery')
        print(post.get('module_battery'))
        request.session['modulequantity'] = post.get('modulequantity')
        print(post.get('modulequantity'))
        request.session['specificationinverter'] = post.get('specificationinverter')
        print(post.get('specificationinverter'))
        request.session['second_inverter'] = post.get('second_inverter')
        print(post.get('second_inverter'))
        request.session['inverterquantity'] = post.get('inverterquantity')
        print(post.get('inverterquantity'))
        request.session['secondinverterquantity'] = post.get('secondinverterquantity')
        print(post.get('secondinverterquantity'))
        request.session['batteryspecification'] = post.get('batteryspecification')
        print(post.get('batteryspecification'))

        # print('umeed', request.session['leads'])
        # thirdlead = {
        #
        #     'pv_module': post.get('pv_module'),
        #     'battery': post.get('module_battery'),
        #     'module_quantity': post.get('modulequantity'),
        #     'battery_spec': post.get('batteryspecification'),
        #     'inverter': post.get('specificationinverter'),
        #     'sec_inverter': post.get('second_inverter'),
        #     'inverter_quantity': post.get('inverterquantity'),
        #     'sec_quantity': post.get('secondinverterquantity'),
        #
        # }
        # print('hello', request.session['leads'])
        # thirdlead = request.env['project.project'].search([('id', '=', request.session['leads'])])
        # print("checkinggggg", request.session['leads'])
        #
        # thirdlead.write({
        #     'pv_module': post.get('pv_module'),
        #     'battery': post.get('module_battery'),
        #     'module_quantity': post.get('modulequantity'),
        #     'battery_spec': post.get('batteryspecification'),
        #     'inverter': post.get('specificationinverter'),
        #     'sec_inverter': post.get('second_inverter'),
        #     'inverter_quantity': post.get('inverterquantity'),
        #     'sec_quantity': post.get('secondinverterquantity'),
        # })

        return request.render('ol_engipartner_web.review_form')


class special_req(http.Controller):

    @http.route(['/special_req'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        print(request.session['utility'])

        request.session['Review'] = post.get('Review')
        print(post.get('Review'))
        request.session['battery'] = post.get('battery')
        print(post.get('battery'))
        request.session['Ballasted'] = post.get('Ballasted')
        print(post.get('Ballasted'))
        request.session['Canopy'] = post.get('Canopy')
        print(post.get('Canopy'))
        request.session['Generator'] = post.get('Generator')
        print(post.get('Generator'))
        request.session['kW'] = post.get('kW')
        print(post.get('kW'))
        request.session['11.5'] = post.get('11.5')
        print(post.get('11.5'))
        request.session['15'] = post.get('15')
        print(post.get('15'))
        request.session['Groundmount'] = post.get('Groundmount')
        print(post.get('Groundmount'))
        request.session['Solar'] = post.get('Solar')
        print(post.get('Solar'))
        request.session['N/A'] = post.get('N/A')
        print(post.get('N/A'))

        return request.render('ol_engipartner_web.special_req')


class upload_doc(http.Controller):

    @http.route(['/upload_documentation'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        request.session['special'] = post.get('special')
        print(post.get('special'))

        return request.render('ol_engipartner_web.upload_documentation')


class project_add_doc(http.Controller):

    @http.route(['/project_add_doc'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        attachments = request.env['ir.attachment']
        name = str(post.get('attachment').filename)
        file = post.get('attachment')
        print('heyb',name,'noice', file)





        print(type(file))

        request.registry['upload_doc'] = file
        data = file.read()
        file.close()
        print(type(data))

        request.registry['upload_doc_new'] = data
        attachment_id = attachments.sudo().create({
            'name': name,
            # 'res_id': ,
            'type': 'binary',
            # 'res_model': 'project.project',

            'datas' : base64.encodebytes(data),
        })
        value = {
            'attachment' : attachment_id
        }
        request.session["attachment_id"]=attachment_id.id

        # print(request.session['attachment_id'])
        print(request.registry['upload_doc'])
        print('hello')


        return request.render('ol_engipartner_web.project_add_doc',value)

class documentation_detail(http.Controller):

    @http.route(['/documentation_detail'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):



        print(request.session['name'])
        print(request.session['city'])
        print(request.session['address'])
        print(request.session['state'])
        print(request.session['country'])
        print(request.session['authority'])
        print(request.session['external'])
        print(request.session['utility'])
        print(request.session['link'])
        print(request.session['business_unit'])
        print(request.session['rooftype'])
        print(request.session['rooftype_material'])
        print(request.session['attachment_brand'])
        print(request.session['sealand_brand'])
        print(request.session['comments'])
        print(request.session['busbaarrating'])
        print(request.session['methodpreference'])
        print(request.session['mainbreaker'])
        print(request.session['pv_module'])
        print(request.session['module_battery'])
        print(request.session['modulequantity'])
        print(request.session['specificationinverter'])
        print(request.session['second_inverter'])
        print(request.session['inverterquantity'])
        print(request.session['secondinverterquantity'])
        print(request.session['batteryspecification'])
        print(request.session['batteryspecification'])
        print(request.session['special'])
        print(request.session['battery'])
        print(request.session['Ballasted'])
        print(request.session['Canopy'])
        print(request.session['Generator'])
        print(request.session['kW'])
        print(request.session['11.5'])
        print(request.session['15'])
        print(request.session['Groundmount'])
        print(request.session['Solar'])
        print(request.session['N/A'])
        print(request.registry['upload_doc'])

        # file = request.session['upload_doc']
        lead = {
            'name':request.session['name'],
            'address': (request.session['address'] ),
            'city': request.session['city'],
            'utility': (request.session['utility']),
            'external_id':(request.session['external']),
            'external_links':(request.session['link']),
            'jurisdiction':(request.session['authority']),
            'business_unit': (request.session['business_unit']),
            'state': (request.session['state']),
            'country': (request.session['country']),
            'roof_type': (request.session['rooftype']),
            'roof_type_material': (request.session['rooftype_material']),
            'rocking_brand': (request.session['rocking_brand']),
            'attachment_brand': (request.session['attachment_brand']),
            'sealand_brand': (request.session['sealand_brand']),
            'other_comments': (request.session['comments']),
            'main_bus': (request.session['busbaarrating']),
            'main_breaker': (request.session['mainbreaker']),
            'method_preference': (request.session['methodpreference']),
            'pv_module': (request.session['pv_module']),
            'battery': (request.session['module_battery']),
            'module_quantity': (request.session['modulequantity']),
            'battery_spec': (request.session['batteryspecification']),
            'inverter': (request.session['specificationinverter']),
            'sec_inverter': (request.session['second_inverter']),
            'inverter_quantity': (request.session['inverterquantity']),
            'sec_quantity': (request.session['secondinverterquantity']),
            'another_battery': (request.session['battery']),
            'ballasted': (request.session['Ballasted']),
            'canopy': (request.session['Canopy']),
            'generator': (request.session['Generator']),
            'kw': (request.session['kW']),
            'greater': (request.session['11.5']),
            'than': (request.session['15']),
            'groundmount':(request.session['Groundmount']),
            'solar' : (request.session['Groundmount']),
            'naa':(request.session['N/A']),
            'special_req': (request.session['special']),
            # 'upload_doc': (request.registry['upload_doc']),


        }
        leads = request.env['project.project'].create(lead)
        print('value of lead is', leads)
        request.session['leads'] = leads.id
        print(request.session["attachment_id"])
        attachment= request.env["ir.attachment"].search([("id","=",request.session["attachment_id"])])
        attachment.res_id=leads.id
        attachment.res_model = leads._name

        request.session['option2'] = post.get('option2')
        print(post.get('option2'))
        if post.get("option2") == 'yes':
            print('yeah')
            stamp_type_rec = request.env['stamp.typedoc'].sudo().search([])
            return request.render('ol_engipartner_web.documentation_detail',{'stamp_type_rec': stamp_type_rec})
        else:
            print('nah')

            return request.redirect('/project_submission')

class documentationdetailsubmission(http.Controller):

    @http.route(['/doc_detail_submission'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        request.session['stamp_type'] = post.get('stamp_type')
        print(post.get('stamp_type'))
        request.session['other_com'] = post.get('other_com')
        print(post.get('other_com'))
        request.session['eng_plan'] = post.get('eng_plan')
        print(post.get('eng_plan'))
        request.session['eng_letter'] = post.get('eng_letter')
        print(post.get('eng_letter'))
        request.session['inspec_Form'] = post.get('inspec_Form')
        print(post.get('inspec_Form'))
        request.session['cvc_permit'] = post.get('cvc_permit')
        print(post.get('cvc_permit'))
        request.session['ec_permit'] = post.get('ec_permit')
        print(request.session['ec_permit'])
        request.session['coi'] = post.get('coi')
        print(request.session['coi'])
        # request.session['leads'] = post.get('leads')
        print('checking', request.session['leads'])

        anotherlead = {

            'stamp_type_doc': post.get('stamp_type'),
            'other_commments_doc': post.get('other_com'),
            'eng_plans': post.get('eng_plan'),
            'eng_letter': post.get('eng_letter'),
            'inspection_form': post.get('inspec_Form'),
            'ec_permit': post.get('ec_permit'),
            'cvc_permit': post.get('cvc_permit'),
            'coi': post.get('coi'),

        }
        print('hello', request.session['leads'])
        anotherlead = request.env['project.project'].search([('id', '=', request.session['leads'])])
        print("checkinggggg", request.session['leads'])

        anotherlead.write({
             'stamp_type_doc': post.get('stamp_type'),
            'other_commments_doc': post.get('other_com'),
            'eng_plans': post.get('eng_plan'),
            'eng_letter': post.get('eng_letter'),
            'inspection_form': post.get('inspec_Form'),
            'ec_permit': post.get('ec_permit'),
            'cvc_permit': post.get('cvc_permit'),
            'coi': post.get('coi'),
        })




        return request.render('ol_engipartner_web.doc_detail_submission')



class projectsubmission(http.Controller):

    @http.route(['/project_submission'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        return request.render('ol_engipartner_web.project_submission')





# Documentation Work

class documentation(http.Controller):

    @http.route(['/add_documentation'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):

        request.session['option'] = post.get('option')
        print(post.get('option'))
        if post.get("option") == 'yes':
            print('yeah')
            return request.render('ol_engipartner_web.view_project')

        else:
            print('nah')
            project_project_rec = request.env['project.project'].sudo().search([])
            return request.render('ol_engipartner_web.new_project_documentation',
                                  {'project_project_rec': project_project_rec})


class viewprojectdocumenetaion(http.Controller):

    @http.route(['/new_project_documentation'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):

        return request.render('ol_engipartner_web.new_project_documentation')


class adddocumenetaionrequest(http.Controller):

    @http.route(['/add_documentation_request'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        request.session['option1'] = post.get('option1')
        print(post.get('option1'))

        if post.get("option1") == 'yes':
            print('yeahhhhhhhh')
            return request.render('ol_engipartner_web.documentation_type')
        else:
            print('nahhhhhhhhhh')

        return request.render('ol_engipartner_web.add_documentation_request')


class viewproject(http.Controller):

    @http.route(['/view_project'], type='http', auth="user", website=True, csrf=False)
    def index(self):
        return request.render('ol_engipartner_web.view_project')
