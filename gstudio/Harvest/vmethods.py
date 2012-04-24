from gstudio.models import *
from objectapp.models import *
from django.db import IntegrityError
from django.template.defaultfilters import slugify
from django.db import IntegrityError
from reversion.models import *

obtype=[]
otlist=[]
auth_list=[]
authors=[]

@reversion.create_revision()
def create_meta_type(mtname):
    slu=slugify(mtname)
    dict={'title':mtname,'slug':slu}
    mt=Metatype.objects.create(**dict)
    mt.save()

@reversion.create_revision()
def create_object_type(metaname,otname,authname):
    obtype=Objecttype.objects.all()
    for i in obtype:
        otlist.append(str(i.title))
    if not otname in otlist:
        for i in Author.objects.all():
            authors.append(str(i.username))
        auth=[]
        user = User(
            username=authname,
            is_active=True,
            is_staff=True,
            is_superuser=False)
        user.save()
        auth.append(Author.objects.get(username=authname))
        slu=slugify(otname)
        dict={'title':otname,'content':'','slug':slu,'status':2}
        ot=Objecttype.objects.create(**dict)
        if metaname <> '':
            mt=Metatype.objects.get(title=metaname)
            ot.metatypes.add(mt)
        ot.sites.add(Site.objects.get_current())
        ot.save()    
        gd=Objecttype.objects.get(title=otname)
        # print 'The Object type created was ',gd

def create_attribute_type(atname,ottype,):
    ot=Objecttype.objects.get(title=ottype)
    oid=NID.objects.get(id=ot.id)
    dict={'title':atname,'slug':atname,'content':'','subjecttype_id':oid.id}
    at=Attributetype.objects.create(**dict)
    at.sites.add(Site.objects.get_current())
    at.save()
    gd=Attributetype.objects.get(title=atname)
    print 'The Attribute type created was ',gd

def create_relation_type(rtname,irname,lottype,rottype,lc,rc):
    lo=Objecttype.objects.get(title=lottype)
    loid=NID.objects.get(id=lo.id)
    ro=Objecttype.objects.get(title=rottype)
    roid=NID.objects.get(id=ro.id)
    dict={'title':rtname,'inverse':irname,'slug':rtname,'left_subjecttype_id':loid.id,'right_subjecttype_id':roid.id,'left_cardinality':lc,'right_cardinality':rc}
    rt=Relationtype.objects.create(**dict)
    rt.sites.add(Site.objects.get_current())
    rt.save()
    gd=Relationtype.objects.get(title=rtname)
    print 'The Relation type created was ',gd


def create_objects(oname,ottype):
    dict1={'title':oname,'content':'','slug':oname}
    obj=Gbobject.objects.create(**dict1)
    obj.objecttypes.add(Objecttype.objects.get(title=ottype))
    obj.sites.add(Site.objects.get_current())
    obj.save()  
    gd=Gbobject.objects.get(title=oname)
    print 'The Object created was ',gd
    

def create_attributes(aname,sobject,attype):  
    ot=Gbobject.objects.get(title=sobject)
    oid=NID.objects.get(id=ot.id)
    at=Attributetype.objects.get(title=attype)
    aid=NID.objects.get(id=at.id)
    dict1={'title':aname,'slug':aname,'svalue':aname,'subject':oid,'attributetype':at}
    att=Attribute.objects.create(**dict1)
    att.save()
    gd=Attribute.objects.get(title=aname)
    print 'The Attribute created was ',gd
    
def create_relations(rname,lobject,robject,rttype,lscope,rscope):
    lo=Gbobject.objects.get(title=lobject)
    lid=NID.objects.get(id=lo.id)
    ro=Gbobject.objects.get(title=robject)
    rid=NID.objects.get(id=ro.id)
    rt=Relationtype.objects.get(title=rttype)
    rtid=NID.objects.get(id=rt.id)
    dict={'title':rname,'slug':rname,'left_subject_id':lid.id,'right_subject_id':rid.id,'relationtype_id':rtid.id,'left_subject_scope':lscope,'right_subject_scope':rscope}
    rtt=Relation.objects.create(**dict)
    rtt.save()
    gd=Relation.objects.get(title=rname)
    print 'The Relation created was ',gd
