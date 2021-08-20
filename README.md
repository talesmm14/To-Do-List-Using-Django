# To-Do List feito com Django Rest Framework
Projeto desenvolvido para mostrar minhas habilidades em Django com Rest.


## Como executar o projeto
 
### Subir projeto
docker-compose up

### Pegar ID do container
docker ps

### Fazer migrações
docker exec -it <id_container> python manage.py migrate

### Criar super usuario
docker exec -it <id_container> python manage.py createsuperuser

## Chamadas urls
### Entrar no Django Admin
localhost:8000/admin/

### [REST] Visualizar e criar To-Do's
localhost:8000/api/tasks

### [REST] Obter, atualizar e deletar To-Do's
localhost:8000/api/tasks

### [FORM] To-Do List em html
localhost:8000/
