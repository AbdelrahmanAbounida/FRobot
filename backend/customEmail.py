from djoser import email


class ActivationEmail(email.ActivationEmail):
    print("activation email")
    template_name = 'email/activation.html'