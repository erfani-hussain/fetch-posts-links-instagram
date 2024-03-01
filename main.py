import instaloader
import time

def fetch_post_links(profile, start_index, end_index, filename):
    # Create a text file to store the post links
    with open(filename, "a") as file:
        # Initialize post count
        post_count = 0
        # Iterate over the posts and write the links to the file
        for post in profile.get_posts():
            if post_count >= start_index and post_count < end_index:
                file.write(f"Post number {post_count+1}\n")
                file.write(f"https://www.instagram.com/p/{post.shortcode}/\n")
                file.write("\n")
            post_count += 1
            # Exit loop if end_index reached
            if post_count == end_index:
                break
        print(f"Fetched links for posts {start_index+1} to {end_index}.")

def get_instagram_post_links(username):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Retrieve profile by username
        profile = instaloader.Profile.from_username(loader.context, username)
        
        # Initialize start and end indices
        start_index = 0
        end_index = 10

        # Keep fetching links until all posts are covered
        while True:
            # Fetch links for the current batch
            fetch_post_links(profile, start_index, end_index, f"{username}_post_links.txt")
            
            # Update indices for the next batch
            start_index = end_index
            end_index += 10

            # Check if all posts have been covered
            if start_index >= profile.mediacount:
                print("All post links have been fetched.")
                break
            
            # Wait for 30 seconds before fetching the next batch
            print("Waiting for 30 seconds before fetching the next batch...")
            time.sleep(30)
    
    except instaloader.exceptions.ProfileNotExistsException:
        print("Error: Profile not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Input Instagram username
    instagram_username = input("Enter Instagram username: ")
    get_instagram_post_links(instagram_username)