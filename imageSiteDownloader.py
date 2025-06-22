#! python3
"""
Image Site Downloader
Write a program that goes to a photo-sharing site like Flickr or Imgur, 
searches for a category of photos, 
and then downloads all the resulting images. 
You could write a program that works with any photo site that has a search feature.
"""


import requests, os, bs4

url = str(input("Enter the URL after searching whatever you want to be downloaded")) # starting url
os.makedirs('ImageSiteDownloaderoutput', exist_ok=True) # store images  in ./ImageSiteDownloaderoutput
i=0
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    img_tags = soup.find_all('img')
    
    if img_tags == []:
        print('Could not find comic image.')
    else:
        img_tags = 'https:' + img_tags[i].get('src')
        # Download the image.
        print('Downloading image %s...' % (img_tags))
        res = requests.get(img_tags)
        res.raise_for_status()
        i=i+1

        # Save the image to ./ImageSiteDownloaderoutput.
        imageFile = open(os.path.join('ImageSiteDownloaderoutput', os.path.basename(img_tags)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

print('Done.')