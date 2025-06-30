from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

def setup_qa_pipeline(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    return pipeline("question-answering", model=model, tokenizer=tokenizer)

def get_answer(qa_pipeline, question, context):
    return qa_pipeline(question=question, context=context)