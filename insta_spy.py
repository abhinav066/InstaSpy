import instaloader

# Function to retrieve details of followers for a given Instagram username
def get_followers_details(username):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()
    # Retrieve profile information for the given username
    profile = instaloader.Profile.from_username(L.context, username)

    followers = []
    # Iterate through each follower of the profile
    for follower in profile.get_followers():
        # Extract relevant information for each follower and store it in a dictionary
        follower_info = {
            'Username': follower.username,
            'Full Name': follower.full_name,
            'Is Private': follower.is_private,
            'External URL': follower.external_url,
            'Profile Pic URL': follower.profile_pic_url,
            'Followed by Viewer': follower.followed_by_viewer,
            'Follows Viewer': follower.follows_viewer
        }
        followers.append(follower_info)  # Append follower details to the list
    
    return followers  # Return the list of follower details

# Function to retrieve details of followees (accounts followed by a given account) for a given Instagram username
def get_followees_details(username):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()
    # Retrieve profile information for the given username
    profile = instaloader.Profile.from_username(L.context, username)

    followees = []
    # Iterate through each followee (account followed by the given username)
    for followee in profile.get_followees():
        # Extract relevant information for each followee and store it in a dictionary
        followee_info = {
            'Username': followee.username,
            'Full Name': followee.full_name,
            'Is Private': followee.is_private,
            'External URL': followee.external_url,
            'Profile Pic URL': followee.profile_pic_url,
            'Followed by Viewer': followee.followed_by_viewer,
            'Follows Viewer': followee.follows_viewer
        }
        followees.append(followee_info)  # Append followee details to the list
    
    return followees  # Return the list of followee details

# Function to retrieve account details for a given Instagram username
def get_account_details(username):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()
    # Retrieve profile information for the given username
    profile = instaloader.Profile.from_username(L.context, username)
    
    account_details = {
        'Username': profile.username,
        'Full Name': profile.full_name,
        'Is Private': profile.is_private,
        'External URL': profile.external_url,
        'Profile Pic URL': profile.profile_pic_url,
        'Biography': profile.biography,
        'Followers': profile.followers,
        'Followees': profile.followees,
        'Is Verified': profile.is_verified
    }
    
    return account_details  # Return the account details

# Function to print text in a box
def print_box(title, details):
    print('\u250F' + '\u2501' * (len(title) + 2) + '\u2513')
    print('\u2503', title, '\u2503')
    print('\u2523' + '\u2501' * (len(title) + 2) + '\u252B')
    for key, value in details.items():
        print('\u2503', f"{key}: {value}", '\u2503')
    print('\u2517' + '\u2501' * (len(title) + 2) + '\u251B')

if __name__ == "__main__":
    # InstaSpy ASCII art
    instaspy_ascii = """
     ___  ____    ____  __ _    ____  _   _ 
    |_ _||  _ \  / ___|/ _` |  / ___|| | | |
     | | | |_) || |  _| (_| | | |  _ | | | |
     | | |  __/ | |_| | (_| | | |_| || |_| |
    |___||_|     \____|\__,_|  \____| \___/ 
    """

    # Print InstaSpy ASCII art
    print(instaspy_ascii)

    # Ask user to input the Instagram username
    username = input("Enter Instagram username: ")
    
    # Retrieve and print account details
    account_details = get_account_details(username)
    print_box("Account Details", account_details)
    
    # Retrieve and print followers details
    followers_details = get_followers_details(username)
    print_box("Followers Details", followers_details)
    
    # Retrieve and print followees details
    followees_details = get_followees_details(username)
    print_box("Followees Details", followees_details)
    
    # Print copyright notice
    print("\nCopyright © @abhinav066")

