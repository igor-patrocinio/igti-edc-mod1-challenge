import boto3
import os

files_path = '/home/igor/projects/engcloud/cap1/rais/'
client = boto3.client('s3')

for file in os.listdir(files_path):
    client.upload_file(files_path+file, 'datalake-igor-igti-edc-mod2-desafio', "raw/rais/"+file)
    


