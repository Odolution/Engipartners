from odoo import http
from odoo.http import request
from odoo import models, fields, api
from odoo.exceptions import UserError
import base64
import requests


class submit_redline(http.Controller):

    @http.route(['/Submit_Redline'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        project_project_rec = request.env['project.project'].sudo().search([])

        return request.render('ol_engipartner_web.submit_redline',{'project_project_rec': project_project_rec,})

class revision_detail(http.Controller):

    @http.route(['/revision_detail'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        revision_submission_rec = request.env['revision.submission'].sudo().search([])
        request.session['project_project'] = post.get('project_project')
        print('first',post.get('project_project'))


        return request.render('ol_engipartner_web.revision_detail',{'revision_submission_rec': revision_submission_rec,})



class submitfile(http.Controller):

    @http.route(['/sub_upload_file'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        request.session['revision_submission'] = post.get('revision_submission')


        return request.render('ol_engipartner_web.sub_upload_file')



class sucessfully(http.Controller):

    @http.route(['/sucessfully_submitted'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        print('second', request.session['project_project'])
        print('chalega',request.session['revision_submission'])
        request.session['revision'] = post.get('revision')
        print('chalega', post.get('revision'))


        lead = request.env['project.project'].search([('id', '=', request.session['project_project'])])

        lead.write({
            'revision_submission': request.session['revision_submission'],
            'revision_comment':  post.get('revision'),

        })



        return request.render('ol_engipartner_web.sucessfully_submitted')



