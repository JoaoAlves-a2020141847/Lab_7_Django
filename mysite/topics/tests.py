from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Topic, Comment

# classe que contém os testes unitários
class Tests(TestCase):
    # função de inicialização
    # para os testes que requerem autenticação
    def setUp(self):
        # cria um utilizador de teste
        # com username e password
        self.user = User.objects.create_user(
            username='test',
            password='test1234'
        )

        # cria um tópico de teste para algumas páginas 
        # com título, descrição e autor
        self.topic = Topic.objects.create(
            title="Test1",
            description="Test1",
            author=self.user
        )

    # função que testa a página de índice
    def test_index_page(self):
        # simula um pedido GET para a página index
        response = self.client.get(reverse('index'))
        # afirma-se que o código que a resposta retorna é 200
        self.assertEqual(response.status_code, 200)

    # função que testa a página de detalhes de tópico
    def test_topic_detail_page(self):
        # simula um pedido GET para a página topic_detail,
        # com o id do tópico de exemplo
        response = self.client.get(reverse('topic_detail', args=[self.topic.id]))
        self.assertEqual(response.status_code, 200)

    # função que testa a página de criação de tópico
    def test_new_topic_page(self):
        # é feito o login com o utilizador de exemplo
        # dado que a página necessita de credenciais
        self.client.login(username='test', password='test1234')
        response = self.client.get(reverse('new_topic'))
        self.assertEqual(response.status_code, 200)
        
    # função que testa a página de adição de tópico
    def test_add_comment(self):
        self.client.login(username='test', password='test1234')
        response = self.client.get(reverse('add_comment', args=[self.topic.id]))
        self.assertEqual(response.status_code, 200)

    # função que cria um tópico de exemplo
    def test_create_topic(self):
        self.client.login(username='test', password='test1234')
        # são criados os dados que o tópico irá conter
        topic_data = {
            'title': 'Test2',
            'description': 'Test2'
        }

        # é simulado um POST da página new_topic, 
        # com os dados feitos atrás
        response = self.client.post(reverse('new_topic'), data=topic_data)

        # afirma-se (assert) que o tópico com o título Test2 existe
        self.assertTrue(Topic.objects.filter(title='Test2').exists())
    

    def test_edit_topic(self):
        self.client.login(username='test', password='test1234')

        topic_data = {
            'title': 'New test 1',
            'description': 'New test 1'
        }

        # é simulado um POST da página new_topic, 
        # com o id do topico de exemplo e com os dados feitos atrás
        response = self.client.post(reverse('edit_topic', args=[self.topic.id]), data=topic_data)
        self.assertTrue(Topic.objects.filter(title='New test 1').exists())

    def test_delete_topic(self):
        self.client.login(username='test', password='test1234')
        response = self.client.post(reverse('delete_topic', args=[self.topic.id]))

        # afirma-se (assert) que não existe um tópico com o título especificado
        self.assertFalse(Topic.objects.filter(title='New test 1').exists())
