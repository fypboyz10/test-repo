from bert_score import score
predictions = [
    "A cat sits on a mat",
    "Nike builds strong customer relationships"
]
references = [
    "The cat is sitting on the mat",
    "Nike focuses on building relationships with customers"
]
P, R, F1 = score(predictions, references, lang="en", verbose=True)
print("BERTScore Results:\n")
for i in range(len(predictions)):
    print(f"Example {i+1}:")
    print(f"Precision: {P[i].item():.3f}")
    print(f"Recall:    {R[i].item():.3f}")
    print(f"F1:        {F1[i].item():.3f}")
    print()
print("Average Scores:")
print(f"Precision: {P.mean().item():.3f}")
print(f"Recall:    {R.mean().item():.3f}")
print(f"F1:        {F1.mean().item():.3f}")
