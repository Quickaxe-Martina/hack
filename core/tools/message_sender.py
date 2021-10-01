import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_to_ws(group, data, message_type='data.message'):
    try:
        channel_layer = get_channel_layer()
        text = json.dumps(data, ensure_ascii=False)
        async_to_sync(channel_layer.group_send)(str(group), {"type": "user_message", "text": text})
        print(f'В сокет группу {group} отправлено сообщение: {data}')
    except ConnectionRefusedError as e:
        print(f'Ошибка подключения: {e}')


def user_send_to_ws(user, data):
    group = f'user_{user.pk}'
    send_to_ws(group, data, 'user_message')
