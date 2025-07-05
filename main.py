from utils.wikipedia import get_wikipedia_content
from utils.text_processing import split_text, get_embeddings
from services.retrieval import build_faiss_index, retrieve_chunks
from services.qa import setup_qa_pipeline, get_answer
from transformers import AutoTokenizer
from sentence_transformers import SentenceTransformer

def main():
    topic = input('Enter a topic to learn about: ')
    document = get_wikipedia_content(topic)
    if document is None:
        print('Could not retrieve information.')
        return

    tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-mpnet-base-v2')
    chunks = split_text(document, tokenizer)

    embedding_model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    embeddings = get_embeddings(chunks, embedding_model)

    index = build_faiss_index(embeddings)

    qa_pipeline = setup_qa_pipeline('deepset/roberta-base-squad2')
    
    while True:
        query = input('\nAsk a question about the topic (or "quit" to exit): ')
        if query.lower() == 'quit':
            break
            
        retrieved_chunks = retrieve_chunks(query, index, embedding_model, chunks)
        context = ' '.join(retrieved_chunks)
        answer = get_answer(qa_pipeline, query, context)
        print(f'Answer: {answer['answer']}')

if __name__ == '__main__':
    main()