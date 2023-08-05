# QahtanClassifier
Arabic Dialects classifier




install the library:
pip install git+https://github.com/alshargi/QahtanClassifier.git




using the Library Example: 

from QahtanClassifier import get_pred_label


xx = ['عام ألفين وثلاثة وعشرين']
maxlabel, details = get_pred_label(xx)

print(maxlabel)
print(details)


