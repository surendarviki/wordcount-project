from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request,'home.html')


def counter(request):
	ft = request.POST['fulltext']
	wc = ft.split(" ")

	worddict = {}

	for word in wc:
		if word in worddict:
			worddict[word] = worddict[word] + 1;
		else:
			worddict[word] = 1


	sitems = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)


	return render(request,'count.html',{'ft':ft,'wc':len(wc),'wdict':sitems})