import time

# stores last message time for each user {user_id: timestamp}
last_message_time = {}
# How many seconds user must wait b/w messages
COOLDOWN_SECONDS = 3

def is_allowed(user_id: int) -> bool:
    """
    Returns True if user can send message.
    Returns False if they are sending too fast.
    """
    now = time.time()
    last_time = last_message_time.get(user_id, 0)

    if now - last_time < COOLDOWN_SECONDS:
        return False
    last_message_time[user_id] = now
    return True

def remaining_time(user_id: int) -> int:
    """
    Returns how many seconds user still needs to wait
    """
    now = time.time()
    last_time = last_message_time.get(user_id, 0)
    remaining = COOLDOWN_SECONDS - (now - last_time)
    return max(0, int(remaining))
