import boto3 as b

def list_s3():
    s3_resource = b.resource('s3')
    print("Listing my buckets:")
    for bucket in s3_resource.buckets.all():
        print(f"\t{bucket.name}")

if __name__ == '__main__':
    
    response = list_s3()