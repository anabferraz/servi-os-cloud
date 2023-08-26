import boto3

def send_message():
    sqs_client = boto3.client('sqs', region_name='us-east-2')
    queue_url='https://sqs.us-east-2.amazonaws.com/248735089137/QueueTest'
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageBody=(
            'Foi feito o upload do relatório na AWS.'
        )
    )
    print(response)

if __name__ == '__main__':

    response = send_message()