# QahtanClassifier
Arabic Dialects classifier


#### install the library:
```bash
pip install git+https://github.com/alshargi/QahtanClassifier.git
```
#### Demo of some of the features:
```python
# -*- coding: utf-8 -*-
from QahtanClassifier import get_pred_label

xx = ['راني باغي جوج منهم','عام ألفين وثلاثة وعشرين', 'مقلع ما معك هانا يا عق والديك']
MyResult = get_pred_label(xx)
for i in MyResult:
    subRes =  i.split("\t")
    for s in subRes:
        print(s)
    print("########")
```

#### Result
```bash
Max Result:Maghrib
راني باغي جوج منهم
['MORoco\t97.905', 'ALGeria\t2.048', 'LYBia\t0.022', 'MORitania\t0.015', 'TUNes\t0.009']
```
```bash
عام ألفين وثلاثة وعشرين

Max Result:['Classic\t46.845', 'MSA\t42.748', 'Levant\t9.023', 'Gulf\t0.799', 'Iraq\t0.324', 'Yemen\t0.195', 'Sudan\t0.053', 'Maghrib\t0.007', 'Egypt\t0.007']
```
```bash
مقلع ما معك هانا يا عق والديك

Max Result:['Yemen\t98.249', 'Levant\t1.683', 'Egypt\t0.035', 'Sudan\t0.022', 'Classic\t0.006', 'Maghrib\t0.002', 'Gulf\t0.001', 'Iraq\t0.001', 'MSA\t0.001']
```



