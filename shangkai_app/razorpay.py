import razorpay
import os
from dotenv import load_dotenv
load_dotenv()

client = razorpay.Client(
    auth=(os.getenv('RAZORPAY_CLIENT_ID'), os.getenv('RAZORPAY_CLIENT_SECRET')))


def demo():
    print(os.getenv('RAZORPAY_CLIENT_ID'))
    print(os.getenv('RAZORPAY_CLIENT_SECRET'))


def verify_payment(payment_id, order_id, signature):
    return client.utility.verify_payment_signature(
        dict(
            razorpay_payment_id=payment_id,
            razorpay_order_id=order_id, 
            razorpay_signature=signature))
