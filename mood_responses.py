
def mood_response(mood):
    lower_mood_response = mood.lower()
    for m, r in user_responses.items():
        if m.lower() == lower_mood_response:
            return r 
    return "I'm not sure I understand that feeling"
        
user_responses = {
    "depressed": "I'm sorry you're feeling like that. Do something that makes you happy, to help ease your feelings.",
    "lonely": "Get out there and make some new friends! It'll be good for you!",
    "calm": "Calm is good it means You're thinking with a somewhat level head.",
    "curious": "You know what they say....Curiosity killed the cat. Just kidding, to be curious is good.",
    "funny": "Good, if you can make someone laugh then laughter is contagious!",
    "anxious": "Calm your nerves. whatever you are anxious about may never come to pass.",
    "angry":  "Don't let your anger get the best of you.",
    "relieved": "Glad you are feeling relieved its a great feeling."
    }
