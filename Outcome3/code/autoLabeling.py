from sklearn.preprocessing import label_binarize
from transformers import pipeline
import pandas as pd

# input sentences
sentences = pd.read_csv('Outcome3/data/morphology_fixed.csv', encoding='utf-16')['sentence']

# Output labels
candidate_labels = ['Confused', 'Not confused']
label2idx = {'Confused':0, 'Not confused':1}
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli") # device = 0(for GPU)

labels = []
for i in range(len(sentences)):
  input_text = sentences[i]

  if isinstance(input_text, str)==False:
    continue
  
  # multi_label=True will return confidence score for both labels independently 
  model_dict = classifier(input_text, candidate_labels, multi_label=True)
  result_dict = dict(zip(model_dict.get('labels'), model_dict.get('scores')))
  label = max(result_dict, key=result_dict.get)
  
  print("Input : ", input_text)
  print("Selected label : ", label)

  labels.append(label2idx[label])

# save the labled data
result_df = pd.DataFrame(
    {'id': sentences,
     'pred': labels
    })

result_df.to_csv("Outcome3/result/labeled_morphology.csv", index=False)