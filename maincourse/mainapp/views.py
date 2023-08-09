from django.shortcuts import render
from django.shortcuts import redirect

def homepage(request):
    return render(request, 'homepage.html')

def dictionary(request):
    with open('dictionary.txt', 'r') as file:
        content = {'words': file.readlines()}
    return render(request, 'dictionary.html', content)

def add_word(request):
    if request.method == 'GET':
        return render(request, 'add_form.html')
    else:
        data = request.POST
        word = data['word']
        translate = data['translate']
        with open('dictionary.txt', 'a') as file:
            file.write(f"""{word}-{translate}\n""")
        return redirect('dictionary')