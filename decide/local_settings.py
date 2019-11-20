ALLOWED_HOSTS = []

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
    'authentication' 'httplocalhost8000',
    'base' 'httplocalhost8000',
    'booth' 'httplocalhost8000',
    'census' 'httplocalhost8000',
    'mixnet' 'httplocalhost8000',
    'postproc' 'httplocalhost8000',
    'store' 'httplocalhost8000',
    'visualizer' 'httplocalhost8000',
    'voting' 'httplocalhost8000',
}

BASEURL = 'httplocalhost8000'

DATABASES = {
    'default' {
        'ENGINE' 'django.db.backends.postgresql',
        'NAME' 'test_decide',
        'USER' 'decide',
        'PASSWORD' 'decide',
        'HOST' 'localhost',
        'PORT' '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256