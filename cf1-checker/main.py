import os
import requests
import xmltodict
from google.cloud import firestore

# Configuration - Replace with your actual values!
RSS_FEED_URL = os.environ.get('RSS_FEED_URL', 'https://feeds.acast.com/public/shows/theuksurfshow')  # e.g., 'https://example.com/podcast.rss'
FIRESTORE_COLLECTION = os.environ.get('FIRESTORE_COLLECTION', 'podcast_episodes')


def check_podcast_feed(request):
    """Cloud Function triggered on a schedule (e.g., daily)."""
    print('Checking for new podcast episodes...')

    db = firestore.Client()  # Initializes Cloud Firestore

    try:
        # 1. Fetch the RSS feed
        response = requests.get(RSS_FEED_URL)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        xml = response.content

        # 2. Parse the XML
        feed = xmltodict.parse(xml)

        # 3. Extract episodes from the RSS feed
        items = feed['rss']['channel']['item']

        # 4. Get the list of processed episodes from Firestore
        processed_episodes = get_processed_episodes(db)

        # 5. Iterate through the episodes and process new ones
        for item in items:
            episode_title = item['title']
            episode_link = item['link']

            # Check if the episode has already been processed
            if episode_link not in processed_episodes:
                # 6. Process the new episode
                print('New episode found:', episode_title)
                process_new_episode(episode_title, episode_link)  # Replace with your processing logic

                # 7. Save the episode link to Firestore to avoid reprocessing
                save_processed_episode(db, episode_link)
            else:
                print('Episode already processed:', episode_title)

        print('Finished checking podcast feed.')
        return 'OK', 200  # Return a success status

    except requests.exceptions.RequestException as e:
        print(f'Error fetching feed: {e}')
        return f'Error fetching feed: {e}', 500
    except Exception as e:
        print(f'Error processing feed: {e}')
        return f'Error processing feed: {e}', 500


def get_processed_episodes(db):
    """Retrieves the list of processed episode links from Firestore."""
    processed_episodes = []
    collection_ref = db.collection(FIRESTORE_COLLECTION)
    docs = collection_ref.stream()
    for doc in docs:
        processed_episodes.append(doc.id)
    return processed_episodes


def process_new_episode(title, link):
    """Processes a new podcast episode (replace with your custom logic)."""
    # *** REPLACE THIS WITH YOUR ACTUAL PROCESSING LOGIC ***
    # This is where you would add your code to:
    # - Send a notification
    # - Update a database
    # - Perform any other actions
    print(f'Processing episode: {title} - {link}')
    # Simulate some asynchronous work
    import time
    time.sleep(1)
    print(f'Finished processing episode: {title}')


def save_processed_episode(db, episode_link):
    """Saves the episode link to Firestore to avoid reprocessing."""
    db.collection(FIRESTORE_COLLECTION).document(episode_link).set({})
    print('Saved episode as processed:', episode_link)
