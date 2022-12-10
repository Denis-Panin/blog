from django.core.mail import send_mail


def email_send(email_to, author_name):
    send_mail(
        'Blog',
        'Вы подписались на автора : {}'.format(author_name),
        'denistest13@gmail.com',
        [email_to],
        fail_silently=False
    )
