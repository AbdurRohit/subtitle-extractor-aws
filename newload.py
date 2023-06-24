import json
import boto3
#⌚ takes ~1min 20 sec to execute this whole code
access_key = "AKIAXVJ3EJHYEUGAXSRD"
secret_access_key = "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"
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key,
    region_name='eu-north-1'
)
video_name='video1'
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('main_sub')

with open('newoutpuy.json', 'r') as json_file:
    subtitles = json.load(json_file)

print('✅ done', type(subtitles))
count=0
for subtitle in subtitles:
    start = subtitle['start']
    end = subtitle['end']
    lines = subtitle['lines']

    lines_string = '\n'.join(lines)
    
    count+=1    
    try:
        response = table.put_item(
            Item={
                'video_name': video_name,
                'start': start,
                'end': end,
                'lines': lines_string
            }
        )
        
        print('✅',count)
    except Exception as e:
        print('Error adding item:', str(e))
