from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import FileUploadForm
import subprocess
from django.shortcuts import render
import webvtt
import boto3
from django.http import JsonResponse
from boto3.dynamodb.conditions import Key
from io import BytesIO
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import sys
import os



# Create your views here.


def upload(request):
    return render(request, 'index.html')


def player(request):
    videourl = "https://mainvideobucket.s3.eu-north-1.amazonaws.com/test_video.mp4?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCmFwLXNvdXRoLTEiRzBFAiEA%2B5ip4QVIi3%2FeNn683jeFtrPVGw%2BGg6vSkxZArQJqGtcCIFjwRfn10PriLKKCXPsFqimBUO5Vc6iGujIk%2FlzHJHaqKuQCCCcQABoMNTI2Nzk0Mzc3NzEyIgx3W4ZKtptlS9dT0YUqwQJueehl0S4GCN27SZpkdpvrbRzRsvcy0Xzg%2FiJw1MUmv%2BeE0Z766vYfxJqMCaEDojmouQ94TuSnCIqBpUDhSTDU6CDVltJoOqTjVDSjt%2BhXXP%2B9EmSF75z5crxM%2B0TESXcL08WdNlUCNZM2aHu9pb0yqSEp2xfPSZEE48OaxMQG2cldhRiEaAKnSt0bHWwqShBFE4ELX5NT01%2BihihMTFiTj%2B%2BI9%2BA54tzKwr2NmSXZ05%2BU4HKKmcTRWt477I%2Fn7Wp0Nfh5LZR1UaJa5CgcxYgEkVMdvRmoPkdHrx3ATcX1jo8CEke1tibQ3ZtIiA%2FMB1DtQYjembEy9mXxKLmK12t8C7NoAngviHAhZmO9frmtuGJjY7tdJE9URRgStJoP79ZLYborlQL%2BOo6vymrFyWAMivo0Z4vbILfy%2BYJkLgDtY3IwhcWqpAY6swKTIkjm592i0BvJmJYdf5ys%2FeQAVmds0KTvmtTqNFk6tWuGaQF9kJbYaTV%2B1DWrdtcL4BcEIve8Ec3RGTSSN0uUHxnrhWij5sWqZlf9IG%2B1r1jMyGqnLPM%2FpV04QRGzA8Mp5UEKG3uuKKXz1wnSQGyH8%2Bbfw2GJD5bvMFPWWUHa9v%2FEG6GvGUcwMdhtTsxMW0%2Bgo1o2Ow3PsXGNMHRu5GFAQn7FacuGRSKE%2BemZl3%2B17rJQdHkaUMkFye9YqKW%2BhD8tj47WwbIjNtKkHiGDu2GDK%2Fh62gL4sVi3R%2B6COzQexHPMSVG9%2F3HS7K%2F0iXHyvFrSJ8BPrKcH9PET55rWfpIM4nyLBJWvuoUO%2B%2FqNcB5wtPbiBTwNadfY6QJrK9MJAbvdJ4Q1VYAYByef0nyoxoDcWWws&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230615T124543Z&X-Amz-SignedHeaders=host&X-Amz-Expires=10800&X-Amz-Credential=ASIAXVJ3EJHYET3IN6B7%2F20230615%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Signature=7bd60aeb53945703ac88a364f835908af46cec26a8546bb79c532226abca8979"
    subtitle = "https://subsforvideo.s3.eu-north-1.amazonaws.com/output.vtt?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCmFwLXNvdXRoLTEiRzBFAiEA%2B5ip4QVIi3%2FeNn683jeFtrPVGw%2BGg6vSkxZArQJqGtcCIFjwRfn10PriLKKCXPsFqimBUO5Vc6iGujIk%2FlzHJHaqKuQCCCcQABoMNTI2Nzk0Mzc3NzEyIgx3W4ZKtptlS9dT0YUqwQJueehl0S4GCN27SZpkdpvrbRzRsvcy0Xzg%2FiJw1MUmv%2BeE0Z766vYfxJqMCaEDojmouQ94TuSnCIqBpUDhSTDU6CDVltJoOqTjVDSjt%2BhXXP%2B9EmSF75z5crxM%2B0TESXcL08WdNlUCNZM2aHu9pb0yqSEp2xfPSZEE48OaxMQG2cldhRiEaAKnSt0bHWwqShBFE4ELX5NT01%2BihihMTFiTj%2B%2BI9%2BA54tzKwr2NmSXZ05%2BU4HKKmcTRWt477I%2Fn7Wp0Nfh5LZR1UaJa5CgcxYgEkVMdvRmoPkdHrx3ATcX1jo8CEke1tibQ3ZtIiA%2FMB1DtQYjembEy9mXxKLmK12t8C7NoAngviHAhZmO9frmtuGJjY7tdJE9URRgStJoP79ZLYborlQL%2BOo6vymrFyWAMivo0Z4vbILfy%2BYJkLgDtY3IwhcWqpAY6swKTIkjm592i0BvJmJYdf5ys%2FeQAVmds0KTvmtTqNFk6tWuGaQF9kJbYaTV%2B1DWrdtcL4BcEIve8Ec3RGTSSN0uUHxnrhWij5sWqZlf9IG%2B1r1jMyGqnLPM%2FpV04QRGzA8Mp5UEKG3uuKKXz1wnSQGyH8%2Bbfw2GJD5bvMFPWWUHa9v%2FEG6GvGUcwMdhtTsxMW0%2Bgo1o2Ow3PsXGNMHRu5GFAQn7FacuGRSKE%2BemZl3%2B17rJQdHkaUMkFye9YqKW%2BhD8tj47WwbIjNtKkHiGDu2GDK%2Fh62gL4sVi3R%2B6COzQexHPMSVG9%2F3HS7K%2F0iXHyvFrSJ8BPrKcH9PET55rWfpIM4nyLBJWvuoUO%2B%2FqNcB5wtPbiBTwNadfY6QJrK9MJAbvdJ4Q1VYAYByef0nyoxoDcWWws&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230615T124518Z&X-Amz-SignedHeaders=host&X-Amz-Expires=7200&X-Amz-Credential=ASIAXVJ3EJHYET3IN6B7%2F20230615%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Signature=96d710d73cb279252b1298b2e97938655493bbe39cd47b4f60f15ef7115731fe"
    context = {'videourl': videourl,
               'sub': subtitle
               }
    return render(request, 'player.html', context)

# creating view for the form


# INITIATING THOSE VERIABLES AS GLOBAL
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = "mainvideobucket"
AWS_REGION = "eu-north-1"
pre_signed_url_video = ""
pre_signed_url_vtt = ""


def extract_subtitles(request):
    if request.method == 'POST':
        video = request.FILES['video']
        with open('temp_file.mp4', 'wb') as temp_file:
            for chunk in video.chunks():
                temp_file.write(chunk)

        video_name = video.name

        sp_list = video_name.split('.')
        video_name_sub = sp_list[0]  # SPLITTING .mp4 from the name

        print('chunkking done ✅')
        subprocess.run(['CCExtractor_win_portable\ccextractorwinfull.exe',
                        'temp_file.mp4', '-o', 'subtitles/'+video_name_sub+'.srt'])  # GETS THE VTT FILE
        
        print('extraction done ✅')
        
        input_path = 'subtitles/'+video_name_sub+'.srt'
        output_path = 'subtitles/'+video_name_sub+'.vtt'
        captions = webvtt.from_srt(input_path)
        captions.save(output_path) #srt to vtt

        # adding S3 upload code
        subprocess.run(['webvtt-to-json', 'subtitles/'+video_name_sub+'.vtt', '-o', 'subtitles/'+video_name_sub+'.json'])#CONVERTING TO JSON FILE
        upload_json_to_dynamodb(video_name_sub)#UPLOADING TO DYNAMODB
        # THIS CODE WILL SAVE THE VIDEO IN S3 AND MAKES A PRESIGNED URL FROM IT
        s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                 region_name=AWS_REGION,)
        print('s3 client done ✅')

        default_storage.save(video_name, video)

        print("upload success ✅")

        pre_signed_url_video = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': AWS_STORAGE_BUCKET_NAME,
                'Key': video_name
            },
            ExpiresIn=3600)  # URL expiration time in seconds

        print('✅Video url created : ', pre_signed_url_video)

    # end adding s3 upload code

        file_name = video_name_sub+'.vtt'
        with open('subtitles/'+video_name_sub+'.vtt', 'rb') as vtt_file:
            default_storage.save(file_name, vtt_file)  # SAVES VTT FILE

        print('subtitle uploaded to s3 done ✅')

        pre_signed_url_vtt = s3_client.generate_presigned_url(  # GENERATES PRESIGNED UR OF VTT FILE
            'get_object',
            Params={
                'Bucket': AWS_STORAGE_BUCKET_NAME,
                'Key': file_name
            },
            ExpiresIn=3600  # URL expiration time in seconds
        )
    print('✅This is the subtitle link : ', pre_signed_url_vtt)
    return render(request, 'view_video.html', {'video_file': pre_signed_url_video, 'sub': pre_signed_url_vtt})


vtt_file_path = pre_signed_url_vtt


def view_video(request):
    response = []
    result = []
    if request.method == 'POST':
        search_word = request.POST.get('search')
        print('🔍 search word:',search_word)

        TABLE_NAME = "main_sub"

        # Creating the DynamoDB Client
        dynamodb_client = boto3.client('dynamodb', region_name="eu-north-1")

        # Creating the DynamoDB Table Resource
        dynamodb = boto3.resource('dynamodb', region_name="eu-north-1")
        table = dynamodb.Table(TABLE_NAME)
        response = table.query(
        KeyConditionExpression=Key('lines').eq(search_word))
        result=response['Items']
        print(response['Items'])
        
        print('✅ items are: ',response)

        print('list creation done ✅')

    return render(request, 'view_video.html', {'results': result})

    # return render(request, 'view_video.html', context)


def upload_json_to_dynamodb(video_name_sub):
   # ⌚ takes ~1min 20 sec to execute this whole code
    access_key = ""
    secret_access_key = ""
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key,
        region_name='eu-north-1'
    )
    video_name = video_name_sub
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('main_sub')

    with open('subtitles/'+video_name_sub+'.json', 'r') as json_file:
        subtitles = json.load(json_file)

    print('✅ done', type(subtitles))
    count = 0
    for subtitle in subtitles:
        start = subtitle['start']
        end = subtitle['end']
        lines = subtitle['lines']

        lines_string = '\n'.join(lines)

        count += 1
        try:
            response = table.put_item(
                Item={
                    'video_name': video_name,
                    'start': start,
                    'end': end,
                    'lines': lines_string
                }
            )
            print('✅ .vtt-json input:', count)
        except Exception as e:
            print('Error adding item:', str(e))
    print('✅done uploading to dynamodb :',response)
    
    
