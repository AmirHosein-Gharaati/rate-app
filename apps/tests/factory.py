import random


def generate_rating_with_random_user(post_id: int, score: int) -> dict:
    user_id = random.randint(1, 1000)
    return {"post": post_id, "user_id": f"device-id-{user_id}", "score": score}
