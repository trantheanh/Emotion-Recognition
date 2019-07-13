__author__ = 'vietbq'

from pushjack import APNSSandboxClient
from data import DATA_PATH
import os

class PushNotification:
    def __init__(self):
        cert_path = os.path.join(DATA_PATH, 'Certificates.pem')
        self.client = APNSSandboxClient(certificate=cert_path,
                    default_error_timeout=1,
                    default_expiration_offset=2592000,
                    default_batch_size=10,
                    default_retries=1)
        self.token = 'D1C879F76E14A76DDCD804B592D0FE735762E19E7E87C09449BABFC46353B643'

    def push_to_client(self, message):
        alert = message
        res = self.client.send(self.token,
                  alert,
                  badge='0',
                  sound='sound to play',
                  category='category',
                  content_available=True,
                  title='Notification',
                  title_loc_key='t_loc_key',
                  title_loc_args='t_loc_args',
                  action_loc_key='a_loc_key',
                  loc_key='loc_key',
                  launch_image='path/to/image.jpg',
                  extra={'custom': 'data'})
        return res

# pusher = PushNotification()
# pusher.push_to_client('Hello Dat')