from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from .models import Topic, Comment
from . import views
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# classe que define o form para os comentários
class CommentForm(ModelForm):
    class Meta:
        model = Comment #considera o modelo Comment
        fields = ['topic', 'text'] #onde o form comtém os espaços seguintes

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

# classe que define o form para os tópicos
class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        

# função que cria a página inicial, listando todos os tópicos
def index(request):
    # armazena todos os tópicos numa variável
    topics = Topic.objects.all()
    # retorna o render da página html em questão,
    # passando para dentro dessa o dicionário (context dictionary) de tópicos
    return render(request, 'topic_list.html', {'topics': topics})

# função que mostra os detalhes do tópico, com um espaço para os comentários
def topic_detail(request, topic_id):
    # armazena o tópico especificado pelo id numa varíavel
    # caso não exista, é retornado um erro 404
    topic = get_object_or_404(Topic, id=topic_id)
    comments = topic.comments.all()
    return render(request, 'topic_detail.html', {'topic': topic, 'comments': comments})

# função que cria a página de adição de um novo comentário, contendo o respetivo formulário
@login_required
def add_comment(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('topic_detail', topic_id)

    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'topic': topic, 'form': form})

# função que cria a página de adição de um novo tópico, contendo o respetivo formulário
@login_required
def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect('index')
        
    else:
        form = TopicForm()

    return render(request, 'new_topic.html', {'form': form})

# função que cria a página de edição de um tópico, contendo o respetivo formulário
@login_required
def edit_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if topic.author != request.user:
        messages.error(request, "You are not the author of this post, aborting.")
        return redirect('topic_detail', topic_id=topic.id)

    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = TopicForm(instance=topic)

    return render(request, 'edit_topic.html', {'topic': topic, 'form': form})

# função que cria a página de eliminação de um tópico
@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if topic.author != request.user:
        messages.error(request, "You are not the author of this post, aborting.")
        return redirect('topic_detail', topic_id=topic.id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            topic.delete()
            messages.success(request, "Topic deleted successfully!")
            return redirect('index')
        elif 'cancel' in request.POST:
            messages.info(request, "Action cancelled.")
            return redirect('topic_detail', topic_id=topic.id)

    return render(request, 'delete_topic.html', {'topic': topic})