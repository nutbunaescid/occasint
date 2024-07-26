from transformers import pipeline

model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
result = sentiment_task("Covid cases are increasing fast!")

print(result)
