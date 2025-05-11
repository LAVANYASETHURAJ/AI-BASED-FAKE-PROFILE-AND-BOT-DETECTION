from gan_detector_simple import detect_gan_artifacts
from bot_behavior_simple import detect_bot_posting_behavior
import pandas as pd

# GAN image check
print("Image Check:")
print(detect_gan_artifacts("sample_profile.jpg"))

# Bot behavior check
print("\nBot Behavior Check:")
sample_data = pd.DataFrame({
    'username': ['bot1', 'user1'],
    'post_times': [
        [1, 2, 3, 4],     # suspicious bot-like
        [1, 5, 12, 23]    # human-like
    ]
})
print(detect_bot_posting_behavior(sample_data))
