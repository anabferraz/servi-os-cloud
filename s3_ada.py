import boto3
from datetime import datetime

def list_s3():
    s3_resource = boto3.resource('s3')
    print("Listing my buckets:")
    for bucket in s3_resource.buckets.all():
        print(f"\t{bucket.name}")

def create_s3():
    s3_client = boto3.client('s3', region_name='us-east-2')
    date = str(datetime.now().date())
    date_rel = date.replace('-','.')
    bucket_name = "relatorio_"+ date_rel
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' criado com sucesso!")
    except Exception as e:
        print("Error:", e)

def upload_file_s3():
    s3_client = boto3.client('s3', region_name='us-east-2')
    data = str(datetime.now().date())
    data_rel = data.replace('-','.')
    file_path = fr"C:\Users\Usuario\Desktop\Relatorio {data_rel}.docx"
    object_name = f"Relatorio_{data_rel}.docx"
    bucket_name = f"relatorio_{data_rel}"
    
    try:
        s3_client.upload_file(file_path, bucket_name , object_name)
        print(f"Arquivo '{object_name}' foi subido com sucesso ao bucket '{bucket_name}' da AWS!")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    
    list_s3()
    create_s3()
    upload_file_s3()