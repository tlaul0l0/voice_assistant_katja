import re
import wikipediaapi
from _04_dialog_manager.event import subscribe, post_event
from _04_dialog_manager.manual_learning.voice_assistant_bot_helper import lookup_entry

REGEX_FIND_PARENTHESIS_PAIRS = "\\(.*?\\)"

def handle_wikipedia_search_event(slots):
    """
    retrieves page from wikipedia api then returns response
    @param slots: dict of recognized slot values 'slotName' : 'slotValue'
    @return: response text
    """
    if len(slots) == 0:
        response = "Zu deinem Suchbegriff konnte leider nichts gefunden werden!"
        return response

    search_term = slots['term']

    # replace whitespaces with an underscore and make the first letter of every word uppercase
    term = search_term.replace(" ", "_").title()

    wikipedia = wikipediaapi.Wikipedia(language = 'de')
    wikipedia_page = wikipedia.page(title = term)

    # no wikipedia page found
    if not wikipedia_page.exists():
        ###Learning###
        new_search_term = lookup_entry()
        print(f"new_search_term {new_search_term}")

        # check if something in entries was found
        if new_search_term:
            wikipedia_page = wikipedia.page(title = new_search_term)

        # nothing was found for search_term from entries or no entry was found
        if wikipedia_page.exists() or not new_search_term:
            response = f"Zu dem Suchbegriff {search_term} existiert leider kein Wikipedia-Eintrag!"
            return response
        ###Learning###

    page_summary = wikipedia_page.summary
    page_summary = re.sub(REGEX_FIND_PARENTHESIS_PAIRS, "", page_summary)


    first_sentence = page_summary.split('.')[0]

    ###Learning###
    post_event("start_learning", 2)
    ###Learning###

    return first_sentence


def setup_wikipedia_event_handlers():
    """
    subcribes all events
    """
    subscribe("search_definition", handle_wikipedia_search_event)
