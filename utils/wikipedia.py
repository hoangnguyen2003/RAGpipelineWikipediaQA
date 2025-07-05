import wikipedia

def get_wikipedia_content(topic):
    try:
        page = wikipedia.page(topic)
        return page.content
    except wikipedia.exceptions.PageError:
        return None
    except wikipedia.exceptions.DisambiguationError as e:
        print(f'Ambiguous topic. Please be more specific. Options: {e.options}')
        return None