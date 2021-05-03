import spacy
import nltk
import ssl
import re
import requests
from bs4 import BeautifulSoup
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()

model = spacy.load(
    "/Users/sabrinakoumoin/Desktop/Code/Capstone 2021/privacy-policy/privacy-policy-model")


entities = {
    "Device": [],
    "Habits and Behavior": [],
    "Identification": [],
    "Location": [],
    "Personal metadata": [],
    # It truncated my Third-party label to third? Add that to my data. Might need to retrain model to ensure third party works! Re-annotate and then re-train...
    "Third": [],
    "Tracking": []
}
full_sentences = {
    "Device": [],
    "Habits and Behavior": [],
    "Identification": [],
    "Location": [],
    "Personal metadata": [],
    "Third": [],
    "Tracking": []
}
len_original_text = 0
len_extracted_sentences = 0


def getText(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.select("body")[0].text.strip()
    # print("hi there")
    # print(soup.select("body")[0])
    return(text)
    # return (str(soup.select("body")[0]))


def extract_ent(text):
    doc = model(text)
    for ent in doc.ents:  # ent is the text that's identified as an entity
        # We have to stringify the ent because though when printed it looks like a string it's actually of type spacy token, and later on the .find() method requires a string as input
        entities[ent.label_].append(str(ent))


def get_full_sentences(text):
    sentences = nltk.sent_tokenize(text)
    len_original_text = len(sentences)
    print(len_original_text)
    for sent in sentences:  # For each sentence, we check if it has a detected entity
        for entity in entities:
            entity_text_list = entities[entity]
            for text in entity_text_list:
                if sent.find(text) != -1:
                    full_sentences[entity].append(sent)


len_extracted_sentences = len(full_sentences["Device"]) + len(full_sentences["Habits and Behavior"]) + len(
    full_sentences["Identification"]) + len(full_sentences["Location"]) + len(full_sentences["Tracking"])

# print("Original Text # of Sentences:" + str(len_original_text) +
#       " \n Summarized Text # of Sentences: " + str(len_extracted_sentences))


# If there is only one \n, I want to leave it. If there's more than one, then I want to keep only one
# Could work better but works fine for now
def removeNewLine(txt):
    num_matches = len(re.findall("\n", txt))
    if num_matches > 1:
        x = re.sub("\n", ".", txt, num_matches-1)
        return x
    else:
        return txt


# We delete all but the first occurrence. Not the most efficient but works for now. **To refactor**
def removeDuplicates(items_list, txt):
    occurrences = items_list.count(txt)
    if occurrences > 1:
        first_occurrence_index = items_list.index(txt)
        for i in range(occurrences):
            items_list.remove(txt)
        items_list.insert(first_occurrence_index, txt)
    return items_list


def cleanDuplicates():
    full_sentences_copy = full_sentences
    for entity in full_sentences_copy:
        sent_list = full_sentences[entity]
        for sent in sent_list:
            removeDuplicates(sent_list, sent)


def cleanText():
    for entity in full_sentences:
        sent_list = full_sentences[entity]
        for i in range(len(sent_list)):
            sent = sent_list[i]
            # removing extra enter spaces
            cleaned_up_sentence = removeNewLine(
                sent)
            # Removing random JS tags and embeds (like from Facebook's data policy)
            if "{" in cleaned_up_sentence or "0" in cleaned_up_sentence or len(cleaned_up_sentence) <= 3:
                cleaned_up_sentence = ""

            sent_list[i] = cleaned_up_sentence


def printText():
    with open("source_code2.html", "w") as source_code:
        final_text = ""
        for entity in full_sentences:
            final_text += "<h1>" + entity + "</h1> <br></br> <ul>"
            for sent in full_sentences[entity]:
                final_text += "<li>" + sent + "</li>"
            final_text += "</ul><br></br>"
        source_code.write(final_text.strip())
        final_text2 = final_text


privacy_policy = getText("https://policies.google.com/privacy?hl=en-US")
extract_ent(privacy_policy)
get_full_sentences(privacy_policy)
cleanText()
cleanDuplicates()
printText()
