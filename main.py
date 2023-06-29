
import praw
import requests
import os

# Set up Reddit API credentials
client_id = 'cLiHJqJNqXkKnXjumPs_cg'
client_secret = 'pMxH1H8n5Yn_vBWkOv1f1RH3ntIugw'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# Choose the subreddit and number of images to download
subreddit_name = 'carsandfilm' # Change the subreddit name as desired
num_images = 10  # Change this number as desired

# Choose which folder to save the images
save_folder = 'PATH_TO_YOUR_WALLPAPER_FOLDER' # Change the folder as necessary

# Creates the save folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Gets the top posts from the subreddit
subreddit = reddit.subreddit(subreddit_name)
top_posts = subreddit.top(limit=num_images)

# Downloads the images
for post in top_posts:
    if 'i.redd.it' in post.url:
        image_url = post.url
        image_filename = os.path.join(save_folder, post.id + '.jpg')
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_filename, 'wb') as f:
                f.write(response.content)
                print(f'Saved image: {image_filename}')
        else:
            print(f'Failed to download image: {image_url}')
