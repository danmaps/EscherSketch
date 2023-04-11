
- https://developer.twitter.com/en/docs/tutorials/creating-a-twitter-bot-with-python--oauth-2-0--and-v2-of-the-twi

- https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/


```python
import tweepy

# Set your API keys and access tokens
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Function to tweet an image with a caption
def tweet_image(image_path, caption):
    """
    This function takes an image path and a caption as input and posts a tweet with the image and caption.
    :param image_path: The path to the image file
    :param caption: The text to be used as the tweet's caption
    """
    # Upload the image to Twitter
    media = api.media_upload(image_path)

    # Post the tweet with the image and caption
    api.update_status(status=caption, media_ids=[media.media_id])

# Example usage
image_path = 'path/to/your/image.jpg'
caption = 'Your caption here'
tweet_image(image_path, caption)
```
