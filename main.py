import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('I am ValluvarBot, a virtual disciple of Thiruvalluvar, the revered Tamil poet and philosopher. How may I assist you today?', ['who','are','you','introduce','yourself'], required_words=['who'])
    response('My purpose is to guide you on the path of wisdom and virtue. How may I assist you today?', ['what', 'do', 'you', 'do'], required_words=['what', 'you'])
    response('I\'m ValluvarBot', ['what', 'is', 'your', 'name'], required_words=['what','name'])

    response('A virtuous heart knows no sorrow, how fare thee?', ['how', 'are', 'you', 'feeling'], required_words=['how'])
    response('Just as the bee gathers nectar from flowers, I gather wisdom from life.', ['how', 'do', 'you', 'seek', 'knowledge'], required_words=['knowledge'])
    response('In the garden of life, may your virtues bloom like flowers.', ['how', 'is', 'your', 'day'], required_words=['how', 'day'])
    response('Even the smallest act of kindness can brighten the darkest day.', ['how', 'may', 'I', 'help', 'you'], required_words=['help','you'])
    response('Life\'s journey is enriched by the company of wise companions.', ['how', 'can', 'we', 'grow', 'together'], required_words=['grow'])
    response('In the vast ocean of knowledge, let us navigate together. How can I guide you today?', ['how', 'can', 'I', 'assist', 'you'], required_words=['assist', 'you'])
    response('The path of righteousness leads to eternal bliss.', ['how', 'do', 'you', 'walk', 'the', 'path', 'of', 'virtue'], required_words=['virtue'])
    response('In the realm of wisdom, let us exchange pearls of knowledge.', ['how', 'do', 'you', 'seek', 'wisdom'], required_words=['wisdom'])
    response('Like the river that flows ceaselessly, may your spirit flow with perseverance.', ['how', 'do', 'you', 'keep', 'going'], required_words=['going'])
    response('As the sun rises each day, may your aspirations soar high.', ['how', 'do', 'you', 'chase', 'your', 'dreams'], required_words=['dreams'])
    response('Just as the lotus blooms amidst adversity, may your spirit rise above challenges.', ['how', 'do', 'you', 'face', 'hardships'], required_words=['hardships'])
    response('In the garden of life, may your actions be the seeds of virtue.', ['how', 'do', 'you', 'practice', 'goodness'], required_words=['goodness'])
    response('As the moon waxes and wanes, may your wisdom grow with each passing day.', ['how', 'do', 'you', 'nourish', 'your', 'mind'], required_words=['nourish'])
    response('In the tapestry of life, may your deeds weave threads of righteousness.', ['how', 'do', 'you', 'serve', 'humanity'], required_words=['humanity'])
    response('Like the silent breeze that caresses the earth, may your words bring comfort to others.', ['how', 'do', 'you', 'show', 'compassion'], required_words=['compassion'])
    response('In the symphony of existence, may your actions be harmonious with nature.', ['how', 'do', 'you', 'maintain', 'balance'], required_words=['balance', 'maintain'])
    response('Just as the tree provides shade to weary travelers, may your presence bring solace to those in need.', ['how', 'do', 'you', 'comfort', 'others'], required_words=['comfort'])
    response('In the crucible of life, may your character be forged with integrity.', ['how', 'do', 'you', 'embrace', 'ethics'], required_words=['ethics'])
    response('Like the river that quenches the thirst of all, may your generosity flow boundlessly.', ['how', 'do', 'you', 'give', 'back'], required_words=['give'])
    
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)
    #print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))