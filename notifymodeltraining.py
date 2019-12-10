import datetime
import json
import socket

import requests

SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'  # os.environ.get('');


class SendNotification:
    def __init__(self, slackChannelName='general', slackUserName='bharat'):
        self.slackChannelName = slackChannelName;
        self.slackUserName = slackUserName;

    def publish_message(self, message):
        """
        :param message:
        :param channel:
        :param username:
        :return:
        """
        data = {"username": self.slackChannelName, "channel": self.slackChannelName, 'text': ''.join(message)}
        print(data)

        print(requests.post(SLACK_WEBHOOK, json.dumps(data)))

    def publish_dict(self, dictionary):
        """
        :param dictionary: Model Training Dictionary, which you want to send to slack
        :param channelName: Channel name, where user want to push training notification
        :param username:  this is slack user name
        :return:
        """
        start_time = datetime.datetime.now()
        data = {"username": self.slackUserName, "channel": self.slackChannelName}
        values = []
        for key, val in dictionary.items():
            values.append(str(key) + " : " + str(val))
        data['text'] = "\n".join(values)
        requests.post(SLACK_WEBHOOK, json.dumps(data))


if __name__ == '__main__':
    # , channelName = 'everythingisdata', username = 'bharat'
    notify = SendNotification(slackChannelName='')
    dictI = {'loss': 0.22, 'HostName': socket.gethostname()}
    notify.publish_dict(dictI)
