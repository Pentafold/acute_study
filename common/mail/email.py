import os
from email.mime.image import MIMEImage
from functools import lru_cache
from threading import Thread

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template

EMAIL_CONFIG = {
    'brand_enquiry': ('New Brand Enquiry Received', 'email/brand_enquiry.html'),
    'fra_questionnaire_submit': ('FRA Questionnaire', 'email/fra_questionnaire.html'),
    'fra_questionnaire_user_submit': ('FRA Questionnaire', 'email/fra_questionnaire_user.html'),
    'fra_questionnaire_form': ('FRA Questionnaire', 'email/fra_questionnaire_form.html'),
    'fra_questionnaire_user_form': ('FRA Questionnaire', 'email/fra_questionnaire_user_form.html'),
    'fra_submit': ('FRA Site Visit Scheduled', 'email/fra_site_visit.html'),
    'fdp_request': ('Franchise Development Program Request', 'email/business_request.html'),
    'sme_request': ('SME Support Request', 'email/business_request.html'),
    'payment_confirm': ('Payment Confirmation', 'email/payment_confirm.html'),
    'academy_request': ('Academy Request', 'email/academy_request.html'),
    'academy_user_request': ('Academy User Request', 'email/academy_user_request.html'),
}


def send_email(to_email, email_type, context_data, attachments=[]):
    subject, template = EMAIL_CONFIG.get(email_type)
    email_template = get_template(template)
    html = email_template.render(context_data)
    message = EmailMultiAlternatives(
        subject=subject,
        body=html,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=to_email if type(to_email) == list else [to_email],
        # cc=[settings.CC_EMAIL],
        # bcc=[settings.BCC_EMAIL],
    )
    message.mixed_subtype = 'related'
    message.attach_alternative(html, "text/html")
    for attachment in attachments:
        message.attach_file(attachment)

    t = Thread(target=message.send, args=(True,))
    t.start()

def email_user(subject, message, to_email, from_email=None, **kwargs):
    """
        Sends an email to this User.
    """
    send_mail(subject, message, from_email, [to_email], **kwargs)


@lru_cache()
def logo_data():
    with open(os.path.join(settings.BASE_DIR, 'static/images/mail_logo.png'), 'rb') as f:
        logo_data = f.read()
    logo = MIMEImage(logo_data)
    logo.add_header('Content-ID', '<image1>')
    return logo
