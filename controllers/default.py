import os
# -*- coding: utf-8 -*-
# required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request, db)
def call(): return service()
# end requires


def generar_pdf():
    from gluon.contrib.fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Hello World!')

    current_dir = os.getcwd()
    work_dir = request.folder+'/reportes'
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
        os.chdir(work_dir)

    pdf.output(work_dir+'/reporte_pagos.pdf')


def my_download():
    base_path = 'reportes'  # /path
    filename = 'reporte_pagos.pdf'
    fullpath = os.path.join(request.folder, base_path, filename)
    response.stream(os.path.join(request.folder, fullpath))


def index():
    datos = request.vars
    if datos['rows']:
        response.flash = 'Reporte generado'
        rows = datos['rows']
    pagados = db(db.t_pagos.f_proceso == 11).count()
    pendientes = db(db.t_alumnos.id > 0).count()
    pendientes = pendientes-pagados
    reporte = datos['reporte']
    if reporte == '1':
        fecha_inicio = datos['fecha_inicio']
        fecha_fin = datos['fecha_fin']
#        my_download()
    return locals()


def error():
    return dict()


@auth.requires_login()
def pagos_new():
    datos = request.vars
    alumno_id = datos['alumno_id']
    rows = db(db.t_alumnos.id == alumno_id).select(db.t_alumnos.ALL)
    for row in rows:
        alumno_name = row.f_name
    new = datos['new']
    if new == '1':
        db.t_pagos.insert(f_amount=datos['f_amount'],
                          f_alumno=datos['f_alumno'],
                          f_proceso=datos['f_proceso'],
                          )
        redirect(URL('default', 'alumnos_manage',
                     vars=dict(message='Pago concretado')))
    return locals()


@auth.requires_login()
def grupos_manage():
    table = request.args(0) or 't_grupos'
    # query = db.t_grupos
    links = [lambda row: A('Ver alumnos', _class='btn btn-primary',
                           _href=URL('default', 'alumnos_manage', vars=dict(group_id=row.id)))]
    fields = []
    linked_tables = []
    if not table in db.tables():
        redirect(URL('error'))
    form = SQLFORM.smartgrid(db[table], linked_tables=linked_tables, fields=fields,
                             details=False, csv=False, links=links, onupdate=auth.archive)
    return locals()


@auth.requires_login()
def alumnos_manage():
    datos = request.vars
    if datos['message']:
        response.flash = datos['message']
    table = 't_alumnos'
    group_id = request.vars['group_id']
    if group_id != None:
        query = ((db.t_alumnos.f_grupo == group_id))
    else:
        query = ((db.t_alumnos.id > 0))
    links = []
    Flag = False
    rows = db(db.t_alumnos.id >= 0).select(db.t_alumnos.id)
    for row in rows:
        if not Flag:
            links.append(lambda row:
                         A('Pagar', _class='btn btn-primary',
                           _href=URL('default', 'pagos_new', vars=dict(alumno_id=row.id)))
                         if not db(db.t_pagos.f_alumno == row.id).select()
                         else A('Ya ah pagado', _class='btn btn-success disabled',
                                _href=URL('default', 'pagos_manage', args=[row.id])))
            Flag = True
    fields = []
    linked_tables = []
    if not table in db.tables():
        redirect(URL('error'))
    form = SQLFORM.grid(query=query, fields=fields,
                        details=False, csv=False, links=links, onupdate=auth.archive)
    return locals()


@auth.requires_login()
def procesos_manage():
    form = SQLFORM.grid(db.t_procesos, onupdate=auth.archive,
                        details=False, csv=False)
    return locals()


@auth.requires_login()
def pagos_manage():
    form = SQLFORM.grid(db.t_pagos, onupdate=auth.archive,
                        details=False, csv=False)
    return locals()


@auth.requires_login()
def reports():
    return dict()
