from django.shortcuts import render

# Create your views here.


# Create your views here.
def home(request):
    return render(request, 'home.html')



def main(request):
    return render(request, 'main.html')


def chatbot(request):
    return render(request, 'chatbot.html')





def introduce(request):
    return render(request, 'introduce.html')



def search(request):
    return render(request, 'search.html')




def contactUs(request):
    return render(request, 'contactUs.html')



def result(request):
    return render(request, 'result.html')