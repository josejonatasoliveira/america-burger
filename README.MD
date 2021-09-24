# Crie um ambiente Python isolado

```bash
conda create -n <nome_variavel>

conda activate -n <nome_variavel>

```

# Instalação da dependencias (executar dentro da pasta do projeto)

```bash
pip install -r requirements.txt
```

# Modificar o arquivo launch.json para apontar para o env criado

# Para atualizar modificações feitas em arquivos estaticos

```bash
python manage.py collectstatic
```

# Para criar um app dentro do projeto

```bash
django-admin startapp <nome_app> <pasta_app>
```

# Para criar um projeto Django

```bash
django-admin startproject <nome_projeto>
```

# Para atualizar o banco de dados 

```bash
python manage.py makemigrations

python manage.py migrate

```

