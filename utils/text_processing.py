def split_text(text, tokenizer, chunk_size=256, chunk_overlap=20):
    tokens = tokenizer.tokenize(text)
    chunks = []
    start = 0
    while start < len(tokens):
        end = min(start + chunk_size, len(tokens))
        chunks.append(tokenizer.convert_tokens_to_string(tokens[start:end]))
        if end == len(tokens):
            break
        start = end - chunk_overlap
    return chunks

def get_embeddings(chunks, embedding_model):
    return embedding_model.encode(chunks)