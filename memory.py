# This file will store conversation history for each user
# we will use simple dictionary for that

# Structure will look like this:
# {
#     123456:[     ← user's telegram id
        # {'role':'user', 'content':'hello'},
        # {'role':'assistant', 'content':'hi'},
#     ]
# }

conversations = {} # stores chat history per user

# Return thr user's conversation history and returns an empty list if new user
def get_history(user_id: int) -> list:
    return conversations.get(user_id, [])

def add_message(user_id: int, role: str, content: str):
    # role is either 'user' or 'assistant'
    if user_id not in conversations:
        conversations[user_id] = [] # create empty list for new user

    conversations[user_id].append({
        'role': role,
        'content': content
    })


    # only keep last 6 messages (3 from user, 3 from bot) to prevent sending too much data to model
    if len(conversations[user_id]) > 6:
        conversations[user_id] = conversations[user_id][-6:]

# this wipes conversation when user reset chat
def clear_history(user_id:int):
    conversations[user_id] = []
