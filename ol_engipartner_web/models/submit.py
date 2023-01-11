from odoo import http
from odoo.http import request
from odoo import models, fields, api
from odoo.exceptions import UserError
import base64
import requests


class submit_redline(http.Controller):

    @http.route(['/Submit_Redline'], type='http', auth="user", website=True, csrf=False)
    def index(self, **post):
        current_user = request.env.user.id
        project_project_rec = request.env['project.project'].sudo().search([('user_id', '=', current_user)])


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
        # print('file name',request.session['myfilee'])
        request.session['revision'] = post.get('revision')
        print('chalega', post.get('revision'))
        print(request.httprequest.files.getlist('myfilee'),'khurram')
        request.session['myfilee'] = post.get('myfilee')
        print('filename', post.get('myfilee'))
        # Multiple Attachment by us
        attachments = request.env['ir.attachment']
        listt = []
        for i in request.httprequest.files.getlist('myfilee'):
            print(i)
            name = str(i.filename)
            file = i
            print('heyb', name, 'noice', file)

            print(type(file))

            request.registry['myfilee'] = file
            data = file.read()

            print(type(data))

            request.registry['myfilee_new'] = data
            attachment_id = attachments.sudo().create({
                'name': name,

                'type': 'binary',


                'datas': base64.encodebytes(data),
            })
            value = {
                'attachment': attachment_id
            }
            # Multiple Attachment by us
            request.session["attachment_id"] = attachment_id.id


            print(request.registry['myfilee'])
            print('hello')
            listt.append(attachment_id.id)

        print(listt, 'List Values')

        request.session['listt'] = listt

        lead = request.env['project.project'].sudo().search([('id', '=', request.session['project_project'])])
        print("the value of lead is", lead)
        request.session['leads'] = lead.id
        print(request.session["attachment_id"])
        attachment = request.env["ir.attachment"].sudo().search([("id", "=", request.session['listt'])])
        attachment.res_id = lead.id
        attachment.res_model = lead._name

        lead.write({
            'revision_submission': request.session['revision_submission'],
            'revision_comment':  post.get('revision'),

        })




        return request.render('ol_engipartner_web.sucessfully_submitted')



