import logging

from celery import shared_task
from django.core.mail import send_mail

from .models import Order

logger = logging.getLogger(__name__)


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Заказ #{order.id}'
    message = (
        f'Уважаемый {order.first_name},\n'
        f'Ваш заказ под номер {order.id}, оформлен.'
    )
    mail_sent = send_mail(
        subject,
        message,
        'admin@shop.ru',
        [order.email],

    )
    logger.info(f'Mail sent: {mail_sent}')
    return mail_sent

