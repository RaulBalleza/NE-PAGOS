from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.auth_user,10)
     populate(db.t_grupos,10)
     populate(db.t_alumnos,10)
     populate(db.t_procesos,10)
     populate(db.t_pagos,10)
