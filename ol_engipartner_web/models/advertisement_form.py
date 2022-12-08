from odoo import http
from odoo.http import request
from odoo import models, fields, api
from odoo.exceptions import UserError
import base64
import requests
import io



class advertisementform(http.Controller):

    @http.route(['/funnel'], type='http', auth="public", website=True, csrf=False)
    def index(self, **post):
        return request.render('ol_engipartner_web.Partnerwithus')


class states(http.Controller):

    @http.route(['/states'], type='http', auth="public", website=True, csrf=False)
    def index(self, **post):

        request.session['option'] = post.get('option')
        print(post.get('option'))
        if post.get("option") == 'yesiown':
            print('yeah')
            return request.render('ol_engipartner_web.ownsolarinstallation')
        else:
            return request.render('ol_engipartner_web.contactuss')

class planspermonth(http.Controller):

    @http.route(['/planspermonth'], type='http', auth="public", website=True, csrf=False)
    def index(self, **post):
        request.session['option1'] = post.get('option1')
        print(post.get('option1'))
        return request.render('ol_engipartner_web.planspermonth')

class contactform(http.Controller):

    @http.route(['/contactform'], type='http', auth="public", website=True, csrf=False)
    def index(self, **post):
        request.session['option2'] = post.get('option2')
        print(post.get('option2'))
        return request.render('ol_engipartner_web.contactform')

class visitordatasubmit(http.Controller):

    @http.route(['/visitordatasubmit'], type='http', auth="public", website=True, csrf=False)
    def index(self, **post):
        request.session['firstname'] = post.get('firstname')
        print(post.get('firstname'))
        request.session['lastname'] = post.get('lasttname')
        print(post.get('lastname'))
        request.session['companyname'] = post.get('companyname')
        print(post.get('companyname'))
        request.session['emailaddress'] = post.get('emailaddress')
        print(post.get('emailaddress'))
        request.session['phoneno'] = post.get('phoneno')
        print(post.get('phoneno'))
        print(request.session['option1'])
        print(request.session['option2'])

        if request.session['option1'] == 'onlyone':
            vari = 'Only 1'
        elif request.session['option1'] == 'two':
            vari = '2'
        else:
            vari = '3 or more than that'

        if request.session['option2'] == 'approx3':
            approx = 'Approximately 3-6'
        elif request.session['option2'] == 'approx7':
            approx = 'Approximately 7-12'
        else:
            approx = 'Approximately 13+'

        lead = {
            'name': str(post.get('firstname')) + ' '+ str(post.get('lastname')),
            'email_from': post.get('emailaddress'),
            'phone': post.get('phoneno'),
            'description': ("Our company operates in" + ' ' + vari + ' ' + 'States' + ' ' + 'and' + ' ' + approx + ' ' + 'plans per month would i need'),

        }

        lead = request.env['crm.lead'].create(lead)
        return request.render('ol_engipartner_web.visitordatasubmit')

class contactuss(http.Controller):

    @http.route(['/contactuss'], type='http', auth="public", website=True, csrf=False)
    def index(self, **post):

        return request.render('ol_engipartner_web.contactuss')

class visitordatasubmit2(http.Controller):

    @http.route(['/visitordatasubmit2'], type='http', auth="public", website=True, csrf=False)
    def index(self, **post):
        request.session['cntctfirstname'] = post.get('cntctfirstname')
        print(post.get('cntctfirstname'))
        request.session['cntctlastname'] = post.get('cntctlasttname')
        print(post.get('cntctlastname'))
        request.session['cntctcompanyname'] = post.get('cntctcompanyname')
        print(post.get('cntctcompanyname'))
        request.session['cntctemailaddress'] = post.get('cntctemailaddress')
        print(post.get('cntctemailaddress'))
        request.session['cntctphoneno'] = post.get('cntctphoneno')
        print(post.get('cntctphoneno'))
        lead = {
            'name': str(post.get('cntctfirstname')) + ' ' + str(post.get('cntctlastname')),
            'email_from': post.get('cntctemailaddress'),
            'phone': post.get('cntctphoneno'),
        }

        lead = request.env['crm.lead'].create(lead)

        return request.render('ol_engipartner_web.visitordatasubmit2')