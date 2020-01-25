response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Grupos'),URL('default','grupos_manage')==URL(),URL('default','grupos_manage'),[]),
(T('Alumnos'),URL('default','alumnos_manage')==URL(),URL('default','alumnos_manage'),[]),
(T('Procesos'),URL('default','procesos_manage')==URL(),URL('default','procesos_manage'),[]),
(T('Pagos'),URL('default','pagos_manage')==URL(),URL('default','pagos_manage'),[]),
]