from django.shortcuts import render
from .form import numForm

def index(request):
  if request.method == 'POST':
    form = numForm(request.POST)
    if form.is_valid():
      n1=int(form.cleaned_data['a'])
      n2=int(form.cleaned_data['b'])
      ans="結果：" + str(n1)+" + "+str(n2)+" = "+str(n1+n2)
  else:
    form=numForm()
    ans=""
  return render(request,'mycalc/index.html',{'form':form, 'ans' : ans})