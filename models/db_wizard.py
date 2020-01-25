# we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_grupos',
                Field('f_name', type='string',
                      label=T('Name')),
                auth.signature,
                format='%(f_name)s',
                migrate=settings.migrate)

db.define_table('t_grupos_archive', db.t_grupos, Field(
    'current_record', 'reference t_grupos', readable=False, writable=False))

########################################
db.define_table('t_alumnos',
                Field('f_name', type='string',
                      label=T('Name')),
                Field('f_last_name', type='string',
                      label=T('Last Name')),
                Field('f_grupo', type='reference t_grupos',
                      label=T('Grupo')),
                auth.signature,
                format='%(f_name)s',
                migrate=settings.migrate)

db.define_table('t_alumnos_archive', db.t_alumnos, Field(
    'current_record', 'reference t_alumnos', readable=False, writable=False))

########################################
db.define_table('t_procesos',
                Field('f_name', type='string',
                      label=T('Name')),
                Field('f_description', type='string',
                      label=T('Description')),
                Field('f_amount', type='double',
                      label=T('Amount')),
                auth.signature,
                format='%(f_name)s',
                migrate=settings.migrate)

db.define_table('t_procesos_archive', db.t_procesos, Field(
    'current_record', 'reference t_procesos', readable=False, writable=False))

########################################
db.define_table('t_pagos',
                Field('f_date', type='date', label=T('Date'), default=request.now, update=request.now),
                Field('f_amount', type='double', label=T('Amount')),
                Field('f_alumno', type='reference t_alumnos',
                      label=T('Alumno')),
                Field('f_proceso', type='reference t_procesos',
                      label=T('Proceso')),
                auth.signature,
                format='%(f_name)s',
                migrate=settings.migrate)

db.define_table('t_pagos_archive', db.t_pagos, Field(
    'current_record', 'reference t_pagos', readable=False, writable=False))
