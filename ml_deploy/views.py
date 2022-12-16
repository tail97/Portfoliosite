from django.views.generic import TemplateView
from django.shortcuts import render
import pickle
import numpy as np

class IrisHome(TemplateView):
    template_name = 'ml_deploy/iris_home.html'

def irisPredict(request):
    #post request일때
    if request.method == 'POST' :
        form = request.POST
        print(form)
        print(len(form))

        # names = 'abcd'
        # cnt = 0 
        # for i in names:
        #     val = form[names[i]]
        #     try : 
        #         float(val)
        #         cnt += 1 

        #     except :
        #         print('형변환실패')
        # if cnt = 4 : 


        # print(form['a'].isdigit())
        
        # cond2 = form['a'].isdigit()
        # print(cond2)

        cond = len(form)>4 and form['a'].isdigit() and form['b'].isdigit() and form['c'].isdigit() and form['d'].isdigit()
        print(len(form)>4 and form['a'].isdigit() and form['b'].isdigit() and form['c'].isdigit() and form['d'].isdigit())
        print(cond)

        if  cond : 
            model = pickle.load(open('static/models/iris_model_svc.pkl', 'rb'))
            data1 = float(form['a'])
            data2 = float(form['b'])
            data3 = float(form['c'])
            data4 = float(form['d'])
            arr = np.array([[data1, data2, data3, data4]])
            pred = model.predict(arr)
            context = {'pred_result' : pred}

        else : 
            print('조건 충족 안 됨')
            context = {"warning" : "문자열입력불가"}

    return render(request, 'ml_deploy/iris_predict.html', context)