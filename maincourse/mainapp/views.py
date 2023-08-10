from django.shortcuts import render
from django.shortcuts import redirect

def homepage(request):
    return render(request, 'homepage.html')

def dictionary(request):
    with open('dictionary.txt', 'r') as file:
        content = file.read().splitlines()
        data = {}
        context = {}
        for line in content:
            word, translate = line.split('-')
            data[word] = translate
            context['items'] = data.items()
    return render(request, 'dictionary.html', context)

def add_word(request):
    if request.method == 'GET':
        return render(request, 'add_form.html')
    else:
        data = request.POST
        word = data['word1']
        translate = data['word2']
        with open('dictionary.txt', 'a') as file:
            file.write(f"""{word}-{translate}\n""")
        return redirect('dictionary')