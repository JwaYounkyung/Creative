from transformers import pipeline

# Output labels
candidate_labels = ["Confused", "Not confused"]

# device=0 for GPU usage
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli", device=0)

# Sample code to see labels for first five rows in df
for i in range(5):
  input_text = df['User Answers'].iloc[i]
  
  # multi_label=True will return confidence score for both labels independently 
  model_dict = classifier(input_text, candidate_labels, multi_label=True)

  # Zip results to dict
  result_dict = dict(zip(model_dict.get('labels'), model_dict.get('scores')))
  
  # Print confidence scores
  print("Input Text for the model : ", input_text)
  print("Confidence Score for Confused Class : ", result_dict.get('Confused'))
  print("Confidence Score for Not-Confused Class : ", result_dict.get('Not confused'), end='\n\n')