import boto3

def consume_queue():
    sqs_client = boto3.client('sqs', region_name='us-east-2')
    response = sqs_client.receive_message(
        QueueUrl="https://sqs.us-east-2.amazonaws.com/248735089137/QueueTest",
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10
    )
    
    for message in response.get('Messages', []):
        body = message.get('Body', 'No body')
        print("Mensagem recebida: "+body)

if __name__ == '__main__':

    response = consume_queue()