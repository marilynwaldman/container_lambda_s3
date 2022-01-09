import sys
import boto3
import folium as fl
from io import StringIO


s3_client = boto3.client('s3')


def handler(event, context):
    string = "I love dogs and cats"
    encoded_string = string.encode("utf-8")

    BUCKET = "map-2022-01-08"
    FILE_NAME = "map.txt"
    S3_PATH = "2022/01/09/" + FILE_NAME
    #mbr = fl.Map(location=[40.0,-95.0],zoom_start=4,tiles="Stamen Toner")

    #str_obj = StringIO() # instantiate in-memory string object
    #mbr.save(str_obj, 'html') # saving to memory string object
    #buf = str_obj.getvalue().encode() # convert in-memory string to bytes

   # Upload as bytes
    s3_client.put_object(
         Bucket=BUCKET, 
         Key=S3_PATH, 
         Body=encoded_string
    )


    return 'I love dogs and cats is in s3!' + sys.version + '!'        
