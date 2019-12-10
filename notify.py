from knockknock import email_sender

@email_sender(recipient_emails=["<your_email@address.com>", "<your_second_email@address.com>"], sender_email="<grandma's_email@gmail.com>")
def train_your_nicest_model(your_nicest_parameters):
    import time
    time.sleep(10000)
    return {'loss': 0.9} # Optional return value