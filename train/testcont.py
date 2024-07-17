import re


entity_types = [
    'Test', 'Disease', 'Anatomy', 'Test_Value', 'Drug', 'Symptom',
    'Reason', 'Amount', 'Treatment', 'Level', 'Duration', 'SideEff',
    'Operation', 'Method', 'Frequency'
]


entity_counts = {entity: 0 for entity in entity_types}

with open('ruijinyiyuan/output/train_sample.txt', 'r', encoding='utf-8') as file:
    for line in file:
        
        for entity in entity_types:
            entity_counts[entity] += len(re.findall(rf'\bB-{entity}\b|\bI-{entity}\b', line))

print(entity_counts)
