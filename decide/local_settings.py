ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
<<<<<<< HEAD
    'authentication':'http://localhost:8000',
    'base':'http://localhost:8000',
    'booth':'http://localhost:8000',
    'census':'http://localhost:8000',
    'mixnet':'http://localhost:8000',
    'postproc':'http://localhost:8000',
    'store':'http://localhost:8000',
    'visualizer':'http://localhost:8000',
    'voting':'http://localhost:8000',
=======
    'authentication': 'http://localhost:8000',
    'base': 'http://localhost:8000',
    'booth': 'http://localhost:8000',
    'census': 'http://localhost:8000',
    'mixnet': 'http://localhost:8000',
    'postproc': 'http://localhost:8000',
    'store': 'http://localhost:8000',
    'visualizer': 'http://localhost:8000',
    'voting': 'http://localhost:8000',
>>>>>>> ee6725a5ba89fb230131d6159311989fec2f346b
}

BASEURL = 'http://localhost:8000'

DATABASES = {
<<<<<<< HEAD
    'default' : {
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'decide',
        'USER':'decide',
        'PASSWORD':'decide',
        'HOST':'localhost',
        'PORT':'5432',
=======
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'decide',
        'USER': 'decide',
        'PASSWORD': 'decide',
        'HOST': 'localhost',
        'PORT': '5432',
>>>>>>> ee6725a5ba89fb230131d6159311989fec2f346b
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
