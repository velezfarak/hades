from app.wsgi import *
from core.erp.models import Type, Employee

#query = Type.objects.all()
#tipo = Type(name="Ingeniero").save()
#tipo = Type()
#tipo.name = 'Gerente'
#tipo.save()
#try:
#    t = Type.objects.get(id=5)
#except Exception as e:
#    t = None
#    print(e)
##t.name = 'Aseadora112'
##t.save()
#if t is not None:
    #print(t)
#t.delete()
#query = Type.objects.filter(name__in=['Auxiliar','accionista'])
#conta = query.count()
#print(conta)
query = Employee.objects.filter(type_id=4)
for que in query:
    print(que.id, que.names)



