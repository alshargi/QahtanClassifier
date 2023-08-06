# -*- coding: utf-8 -*-
# Done By 
## Dr. Faisal ALSHARGI
## New York, US, Aug, 2023
##############################

import joblib
#from sklearn.svm import LinearSVC
#from sklearn.calibration import CalibratedClassifierCV
#from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
#from sklearn.preprocessing import LabelEncoder
import pandas as pd

keepall = []
dict_locs = {} 
decLabels = { 30: 'Gulf',40: 'Yemen',50: 'Maghrib',60: 'Levant', 70: 'Iraq', 80: 'Egypt', 90: 'Sudan',100: 'MSA',101: 'Classic'}
labels_info_gulf = ['NAJD', 'OMAN', 'KWAIT', 'BAHRAIN', 'EMARAT','QATAR']
decLabels_GULF = { 0: 'NAJD', 13: 'OMAN', 14: 'KWAIT', 15: 'BAHRAIN', 17: 'EMARAT', 18: 'QATAR'}

labels_info = ['Gulf', 'Yemen', 'Maghrib', 'Levant', 'Iraq','Egypt', 'Sudan', 'MSA', 'Classic']
decLabels = { 30: 'Gulf', 40: 'Yemen', 50: 'Maghrib', 60: 'Levant',  70: 'Iraq',  80: 'Egypt', 90: 'Sudan', 100: 'MSA', 101: 'Classic'}

decLabels_MOR = { 2: 'MORoco', 7: 'LYBia', 11: 'TUNes', 16: 'MORitania', 19: 'ALGeria'}
labels_info_MOR = ['MORoco', 'LYBia', 'TUNes', 'MORitania', 'ALGeria']

decLabels_LEVANT = { 6: 'SYRIA', 9: 'PALESTINE', 12: 'JORDAN', 21: 'LEBANON'}
labels_info_LEVANT = ['SYRIA', 'PALESTINE', 'JORDAN', 'LEBANON']
flj_xx = "flag-icon flag-icon-"


dict_locs_gulf = {} 
dict_locs_levant = {} 
dict_locs_mor = {} 
dict_locs = {} 
keepall = []

### load models
loaded_calibrated_svc_Main = joblib.load('models/main_svc_model.sav')
loaded_count_vect_Main = joblib.load('models/main_count_vect_M_model.sav')
loaded_tf_transformer_Main = joblib.load('models/main_tfidf_transformer_model.sav')
loaded_label_encoder_Main = joblib.load('models/main_label_encoder_model.sav')
print("main models, Loaded")
# Load gulf
loaded_calibrated_svc_gulf = joblib.load('models/gulf_svc_model.sav')
loaded_count_vect_gulf     = joblib.load('models/gulf_count_vect_M_model.sav')
loaded_tf_transformer_gulf = joblib.load('models/gulf_tfidf_transformer_model.sav')
loaded_label_encoder_gulf  = joblib.load('models/gulf_label_encoder_model.sav')
print("gulf models, Loaded")
# Load levant
loaded_calibrated_svc_levant = joblib.load('models/levant_svc_model.sav')
loaded_count_vect_levant     = joblib.load('models/levant_count_vect_M_model.sav')
loaded_tf_transformer_levant = joblib.load('models/levant_tfidf_transformer_model.sav')
loaded_label_encoder_levant  = joblib.load('models/levant_label_encoder_model.sav')
print("levant models, Loaded")
# Load mor
loaded_calibrated_svc_mor = joblib.load('models/mor_svc_model.sav')
loaded_count_vect_mor    = joblib.load('models/mor_count_vect_M_model.sav')
loaded_tf_transformer_mor = joblib.load('models/mor_tfidf_transformer_model.sav')
loaded_label_encoder_mor  = joblib.load('models/mor_label_encoder_model.sav')
print("mor models, Loaded")



def get_pred_mor(to_predict):
    keepres = []
    p_count = loaded_count_vect_mor.transform(to_predict)
    p_tfidf = loaded_tf_transformer_mor.transform(p_count)
    dres_mor = pd.DataFrame(loaded_calibrated_svc_mor.predict_proba(p_tfidf)*100 , columns=loaded_label_encoder_mor.classes_ )
    for content in dres_mor.items():
        dict_locs_mor[decLabels_MOR[content[0]]]=  content[1][0]
    sorted_val_MOR = sorted(dict_locs_mor.items(), key = lambda kv: kv[1] , reverse = 1)
    for i in sorted_val_MOR:
        keepres.append("{}\t{}".format(i[0], str(round(i[1], 3)) ))

    return keepres

def get_pred_LEvant(to_predict):
    keepres = []
    p_count = loaded_count_vect_levant.transform(to_predict)
    p_tfidf = loaded_tf_transformer_levant.transform(p_count)
    dres_Levant = pd.DataFrame(loaded_calibrated_svc_levant.predict_proba(p_tfidf)*100 , columns=loaded_label_encoder_levant.classes_ )
    for content in dres_Levant.items():
        dict_locs_levant[decLabels_LEVANT[content[0]]]=  content[1][0]
    sorted_val_LEVANT = sorted(dict_locs_levant.items(), key = lambda kv: kv[1] , reverse = 1)
    for i in sorted_val_LEVANT:
        keepres.append("{}\t{}".format(i[0], str(round(i[1], 3)) ))

    return keepres

def get_pred_main(to_predict):
    keepres = []
    p_count = loaded_count_vect_Main.transform(to_predict)
    p_tfidf = loaded_tf_transformer_Main.transform(p_count)
    themax = loaded_calibrated_svc_Main.predict(p_tfidf)              
    dres = pd.DataFrame(loaded_calibrated_svc_Main.predict_proba(p_tfidf)*100 , columns=loaded_label_encoder_Main.classes_ )
    for content in dres.items():
        dict_locs[decLabels[content[0]]]=  content[1][0]
    sorted_val = sorted(dict_locs.items(), key = lambda kv: kv[1] , reverse = 1)
    for i in sorted_val:
        keepres.append("{}\t{}".format(i[0], str(round(i[1], 3)) ))
    return str(labels_info[themax[0]]), keepres

def get_pred_gulf(to_predict):
    keepres = []
    p_count = loaded_count_vect_gulf.transform(to_predict)
    p_tfidf = loaded_tf_transformer_gulf.transform(p_count)
    dres_gulf = pd.DataFrame(loaded_calibrated_svc_gulf.predict_proba(p_tfidf)*100 , columns=loaded_label_encoder_gulf.classes_ )
    for content in dres_gulf.items():
        dict_locs_gulf[decLabels_GULF[content[0]]]=  content[1][0]
    sorted_val_GULF = sorted(dict_locs_gulf.items(), key = lambda kv: kv[1] , reverse = 1)
    for i in sorted_val_GULF:
        keepres.append("{}\t{}".format(i[0], str(round(i[1], 5))))
    return keepres #result_all_GULF


def findres(X_new):
    X_new_counts = loaded_count_vect_Main.transform(X_new)
    X_new_transformed = loaded_tf_transformer_Main.transform(X_new_counts)
    predicted_new = loaded_calibrated_svc_Main.predict(X_new_transformed)
    predicted_labels_original = loaded_label_encoder_Main.inverse_transform(predicted_new)
    return X_new, decLabels[predicted_labels_original[0]]

#################
def get_pred_label(to_predict):
    keepallFinal = []
    for tx in to_predict:
        maxres, res_main = get_pred_main([tx])
        if str(maxres) == str('Gulf'):
            keepall = get_pred_gulf(to_predict)
            keepallFinal.append("{}\tMax Result:{}\t{}".format(tx, maxres, keepall))
        elif str(maxres) == str('Levant'):
            keepall = get_pred_LEvant(to_predict)
            keepallFinal.append("{}\tMax Result:{}\t{}".format(tx, maxres, keepall))

        elif str(maxres) == str('Maghrib'):
            keepall = get_pred_mor(to_predict)
            keepallFinal.append("{}\tMax Result:{}\t{}".format(tx, maxres, keepall))

        else:
            keepall = res_main
            keepallFinal.append("{}\tMax Result:{}".format(tx,res_main))

            
    return keepallFinal


