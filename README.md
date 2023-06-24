# Subtitle-extractor-amazon aws
So basically it extracts subtitles from the video and previews it with the subtitle, but there is more to it, 
1. It takes the video file and stores it locally and extracts the subtitle. 
2. It stores the video to a **AWS S3 bucket** along with the subtitles.
3. The subtitles are sent to **dynamodb** as well (in JSON format). 
4. It generates a pre-signed URL for the video and the subtitle and redirects to the `view_video` page.
5. In `view_video` it shows the output video with the subtitle and there is a search box where you can search words and get the time stamp form
dynamodb.


![sub-ext main drawio](https://github.com/AbdurRohit/subtitle-extractor-aws/assets/96853180/c045b3c7-0602-4ae5-99e7-6115fadb4d32)


