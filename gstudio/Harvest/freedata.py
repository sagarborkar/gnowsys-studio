import freebase
from gstudio.models import *
from objectapp.models import *

dict={}

query = {
     "id" : "/en/tom_and_jerry_kids_show",
     "type" :"/tv/tv_program",
     "name" :"Tom and Jerry Kids Show",    
     "program_creator":[],
     "genre":[],
     "country_of_origin":[],
     "episodes": [{
            "name":[],
            "season":[],
            "episode_number":[]
     }]     
     
}

results=freebase.mqlread(query)
#print "PROGRAM CREATOR"
pro_list1=[]
for e in results.program_creator:    
    pro_list1.append(str(e))
    #print e

dict={'prog_creator':pro_list1}
pro_list=[]

for e in results.country_of_origin:
    pro_list.append(e)
    #print e

dict.update({'co_of_orig':pro_list})
pro_list=[]

genre=[]
for e in results.genre:
    genre.append(str(e))
    #print e

dict.update({'genre':genre})
pro_list=[]

dict1={}

epi_name=[]
epi_seas=[]
epi_epino=[]
for n  in results.episodes:
     # dict1.update({'ep1_name':n.name,'epi_season':n.season,'epi_no':n.episode_number})
     #print n.name
     #print n.season
     #print n.episode_number   
    epi_name.append(n.name)
    list=[]
    list=[str(item) for item in n.season]
    for s in list:
        epi_seas.append(s)
    epi_epino.append(n.episode_number)

epis={'epi_name':epi_name,'epi_seas':epi_seas,'epi_no':epi_epino}

dict.update({'episodes':epis})

#print dict

def create_objects():
    dict1={'title':'Tom And Jerry Kids Show1','content':'','slug':'TJKS'}
    obj=Gbobject.objects.create(**dict1)
    obj.objecttypes.add(Objecttype.objects.get(title='tv_program'))
    obj.sites.add(Site.objects.get_current())
    obj.save()

    # dict2={'title':'Cartoon Episodes','content':'','slug':'Tom_And_Jerry_Kids_Show_Episodes'}
    # obj1=Gbobject.objects.create(**dict2)
    # obj1.objecttypes.add(Objecttype.objects.get(title='Episodes'))
    # obj1.sites.add(Site.objects.get_current())
    # obj1.save()

    

def create_attributes():   
    ast=pro_list1[0]
    ot=Gbobject.objects.get(title='Tom And Jerry Kids Show1')
    oid=NID.objects.get(id=ot.id)
    at=Attributetype.objects.get(title='Program Creator')
    aid=NID.objects.get(id=at.id)
    dict1={'title':ast,'slug':ast,'svalue':ast,'subject':oid,'attributetype':at}
    att=Attribute.objects.create(**dict1)
    att.save()

    for e in genre:
        ot=Gbobject.objects.get(title='Tom And Jerry Kids Show1')
        oid=NID.objects.get(id=ot.id)
        at=Attributetype.objects.get(title='Genre')
        aid=NID.objects.get(id=at.id)
        dict1={'title':e,'slug':e,'svalue':e,'subject':oid,'attributetype':at}
        att=Attribute.objects.create(**dict1)
        att.save()

    # for s in epi_seas:        
    #     ot=Gbobject.objects.get(title='Tom And Jerry Kids Show1')
    #     oid=NID.objects.get(id=ot.id)
    #     at=Attributetype.objects.get(title='Episode Season')
    #     aid=NID.objects.get(id=at.id)
    #     dict1={'title':s,'slug':s,'svalue':s,'subject':oid,'attributetype':at}
    #     att=Attribute.objects.create(**dict1)
    #     att.save()

# def create_relations():
#     lo=Gbobject.objects.get(title='Tom And Jerry Kids Show')
#     lid=NID.objects.get(id=lo.id)
#     ro=Gbobject.objects.get(title='Cartoon Episodes')
#     rid=NID.objects.get(id=ro.id)
#     rt=Relationtype.objects.get(title='has')
#     rtid=NID.objects.get(id=rt.id)
#     dict={'title':'has','slug':'has','left_subject_id':lid.id,'right_subject_id':rid.id,'relationtype_id':rtid.id,'left_subject_scope':1,'right_subject_scope':1000}
#     rtt=Relation.objects.create(**dict)
#     rtt.save()



