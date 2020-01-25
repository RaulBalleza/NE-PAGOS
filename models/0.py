from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'SIstema de pagos'
settings.subtitle = None
settings.author = 'Raul Balleza'
settings.author_email = 'raullb15@gmail.com'
settings.keywords = None
settings.description = None
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '0911a8f4-6a24-483b-8cdb-63d8c887917a'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = None
settings.login_method = 'local'
settings.login_config = None
settings.plugins = []
