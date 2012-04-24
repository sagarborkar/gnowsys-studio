import xmlrpclib
from gstudio.models import *
from objectapp.models import *
from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify
from django.db import IntegrityError
from gstudio.Harvest.functioncalls import *

s=xmlrpclib.Server('http://sagarborkar:swagger1988@atlas.gnowledge.org/gnowql')

# ssid=9075
# nidstr=str(9075)

# niob=s.getnids(['9075'])
# #print niob

# nbh=s.getNeighbourhood([ssid],'rendered_nbh')[nidstr]
# #print nbh    #--"This works fine!-->returns the entire neighbourhood of the node"

# rtypes=[]
# rtlist=[]
# rtypesnids={}
# relationsnids=[]
# rolessids_rt=[]
# rolessids_lt=[]
# ni_listrt={}
# ni_listlt={}
# ni_listr=[]
# ni_listl=[]
# ni_listrins={}
# ni_listrdep={}
# ni_listsutype={}
# ni_listlcon={}
# ni_listldep={}
# dict={}
# auth_list_niob=[]
# auth_list_ob=[]
# objdict={}
# attributes={}
# atlist=[]
# st=2

# if nbh.has_key('relationtypes'):
#    rtypes=nbh['relationtypes']
#    #print rtypes
#    for rt in rtypes:
#       rtypesnids.update(s.getnids([rt]))
#    #print rtnids   
   
# if nbh.has_key('attributetypes'):
#    ats = nbh['attributetypes']
#    #print '\n\n',ats
#    atnids={}
#    if ats <> []:
#       for at in ats:
#         atnids.update(s.getnids([at]))      
#    #print'\n\n',atnids  

# if nbh.has_key('relations'):
#     relations=nbh['relations']
#     #print relations
#     relationsnids=relations.keys()

#     #print "Relations Are\n",relations   #--"This works fine!-->Returns the relations of the node viz instanceof, contains etc" 
#     #print "\n\nRelation Nids Are \n",relationsnids  # --"this works fine!-->Returns the name of the relations viz instanceof, contains, dependson"

#     relationtypes=s.getInverseNames(relationsnids)
#     #print "\n\nThe Inverse Names Of The Relations Are\n",relationtypes  # --"This works fine!-->Returns the inverse names of all the relations viz instanceof:instance, contains:inverse_of_contains"

#     for rt in relationsnids:
#         try:
#             subjectssidsrt=relations[rt]['rightroles']
#             #print "\n\nThe subject ssids of "+rt+" rightroles are as follows :\n"
#             #print subjectssidsrt
            
#             # print '\n\nEach subjectsssid of '+rt+' is as follows :\n'
#             if rt=='subtypeof':
#                for i in subjectssidsrt:
#                    ni=s.getnids([i])
#                    ni_listsutype.update(ni)
 
#             if rt =='instanceof':
#                for i in subjectssidsrt:
#                    ni=s.getnids([i])
#                    ni_listrins.update(ni)
           
#             if rt =='dependson':
#                for i in subjectssidsrt:
#                    ni=s.getnids([i])
#                    ni_listrdep.update(ni)
               

           
#             # for each in subjectssidsrt:
#             #     rolessids_rt.append(each)                
#             # print rolessids_rt         
             

#         except:
#             pass
#         try:
#             subjectssidslt=relations[rt]['leftroles']
#             #print '\n\nThe subject ssids of '+rt+' leftroles are as follows :\n'
#             #print subjectssidslt     #---This works fine!-->Returns the leftroles for contains and depends on relations.
#             # print '\n\nEach subjectssid is as follows :\n'
#             if rt == 'contains':
#                 for i in subjectssidslt:
#                     ni=s.getnids([i])
#                     ni_listlcon.update(ni)
#             if rt == 'dependson':
#                 for i in subjectssidslt:
#                     ni=s.getnids([i])
#                     ni_listldep.update(ni)           
#         except:
#             pass

# if nbh.has_key('attributes'):
#    attributes = nbh['attributes']
#    #print attributes
#    for i in attributes:
#       atlist=attributes[i]
#       #print atlist[1]
#       val=atlist[1]
   
   


# #print '\n\nSub Type Of',ni_listsutype
# # print '\n\nInstance Of',ni_listrins
# # print '\n\nContains',ni_listlcon
# # print '\n\nDepends On',ni_listldep

# # for i in ni_listrins:
# #      # objkeys.append(i)
# #      # ni_listr.append(ni_listrins[i])
# objdict.update(ni_listrins)
     
# # for i in ni_listrdep:
# #     # objkeys.append(i)
# #     # ni_listr.append(ni_listrdep[i])
# objdict.update(ni_listrdep)

# # for i in ni_listsutype:
# #     # objkeys.append(i)
# #     # ni_listr.append(ni_listsutype[i])
# objdict.update(ni_listsutype)

# # for i in ni_listlcon:
# #      # objkeys.append(i)
# #      # ni_listl.append(ni_listlcon[i])
# objdict.update(ni_listlcon)
    
# # for i in ni_listldep:
# #     # objkeys.append(i)
# #     # ni_listl.append(ni_listldep[i])
# objdict.update(ni_listldep)

# #print objdict

# listo=[]
# for a in ni_listr:
#     listo.append(a)
# for item in ni_listl:
#     if not item in listo:
#         listo.append(item)

# #print listo


def create_meta_type():
      meta=Metatype.objects.all()
      mettitle=[]
      authors=[]
      for i in meta:
         mettitle.append(str(i.title))
      con=s.getnids(['6233'])
      for i in con:
         if not con[i] in mettitle:
            for n in s.getAllSnapshots('ssid',str(i)):
               auth=s.getUsernamefromUserId(s.getAuthor(n))
            for au in Author.objects.all():
               authors.append(str(au.username))
            if not auth in authors:
               user = User(
                    username=auth,                 
                    is_active=True,
                    is_staff=True,
                    is_superuser=False)
               user.save()
            uauth=Author.objects.get(username=auth)
            slu=slugify(con[i])
            dict={'title':con[i],'slug':slu}
            mt=Metatype.objects.create(**dict)
            mt.authors.add(uauth)
            mt.save()

listobj=[]
listobj=NID.objects.all()
listobjs=[]
for i in listobj:
    listobjs.append(str(i.title))
#print listobjs

def create_object_type():
   for ob in niob: 
        if not niob[ob] in listobjs and niob[ob]<>'concept':
           auth_list_niob=[]
           for n in s.getAllSnapshots('ssid',str(ob)):
              auth_list_niob.append(s.getUsernamefromUserId(s.getAuthor(n)))
           #print auth_list_niob
           authors=[]     
           for i in Author.objects.all():
              authors.append(str(i.username))
           auth=[]
           for i in auth_list_niob:
              if not i in authors:
                 user = User(
                   username=i,                 
                   is_active=True,
                   is_staff=True,
                   is_superuser=False)
                 user.save() 
              auth.append(Author.objects.get(username=i))
              slu=slugify(niob[ob])
              dict={'title':niob[ob],'slug':slu,'content':'','status':2}
              obj=Objecttype.objects.create(**dict)
              mt=Metatype.objects.get(title='concept')
              obj.metatypes.add(mt)
              for i in auth:
                 obj.authors.add(i)
              obj.save()         

              if attributes<>{}:             
                 for i in attributes:
                    ot=Objecttype.objects.get(title=niob[ob])
                    oid=NID.objects.get(id=ot.id)
                    at=Attributetype.objects.get(title=str(i))
                    slua=slugify(val)
                    dict={'title':val,'slug':slua,'svalue':val,'subject':oid,'attributetype':at}
                    att=Attribute.objects.create(**dict)
                    att.save()          
          
   for ob in objdict: 
        nbh1={}
        obj={}
        objattributes={}
        objatlist=[]
        obstr=str(ob)
        if not objdict[ob] in listobjs and objdict[ob]<>'concept':           
           nbh1=s.getNeighbourhood([obstr],'rendered_nbh')
           #print nbh1
           obj=nbh1[ob]
           #print obj
           if obj.has_key('attributes'):
              objattributes=obj['attributes']
              #print '\n\n',objattributes
              for i in objattributes:
                 objatlist=objattributes[i]
              objval=objatlist[1]
              #objslu=objatlist[0]
              #print '\n\n',objatlist

           auth_list_ob=[]
           for n in s.getAllSnapshots('ssid',str(ob)):
              auth_list_ob.append(s.getUsernamefromUserId(s.getAuthor(n)))
           authors=[]     
           for i in Author.objects.all():
              authors.append(str(i.username))
           auth=[]
           for i in auth_list_ob:
              if not i in authors:
                 user = User(
                   username=i,                 
                   is_active=True,
                   is_staff=True,
                   is_superuser=False)
                 user.save()
              auth.append(Author.objects.get(username=i))
              slu=slugify(objdict[ob])
              dict={'title':objdict[ob],'slug':slu,'content':'','status':2}
              obj=Objecttype.objects.create(**dict)          
              obj.sites.add(Site.objects.get_current())
              mt=Metatype.objects.get(title='concept')
              obj.metatypes.add(mt)
              for i in auth:
                 obj.authors.add(i)
              obj.save()         

              if objattributes <> {}:
                 for i in objattributes:
                    #print objattributes[i]
                    ot=Objecttype.objects.get(title=objdict[ob])
                    oid=NID.objects.get(id=ot.id)
                    at=Attributetype.objects.get(title=str(i))
                    objslu=slugify(objval)
                    dict1={'title':objval,'slug':objslu,'svalue':objval,'subject':oid,'attributetype':at}
                    att=Attribute.objects.create(**dict1)
                    att.save()              

def create_relation_type(): 
    st=-1
    rel_list=[]
    relid_list=[]
    relnid=[]
    reltitle=[]
    lo=Metatype.objects.get(title='concept')
    loid=NID.objects.get(id=lo.id)
    rel_list=Relationtype.objects.all()
    for i in rel_list:
        relid_list.append(i.id)
    for s in relid_list:
        relnid.append(NID.objects.get(id=s))
    for s in relnid:
        reltitle.append(str(s.title))
    if rtypesnids <> {}:

       for i in rtypesnids:       
          if not i in reltitle: 
             slu=slugify(rtypesnids[i])
             dict={'title':rtypesnids[i],'inverse':rtypesnids[i],'slug':slu,'content':'','left_subjecttype_id':lo.id,'right_subjecttype_id':lo.id}
             rt=Relationtype.objects.create(**dict)
             rt.sites.add(Site.objects.get_current())
             rt.save()
             
    if relationtypes <> {}:
       for rt in relationtypes:
          if not rt in reltitle:
             slu=slugify(rt)
             dict1={'title':rt,'inverse':relationtypes[rt],'slug':slu,'content':'','left_subjecttype_id':lo.id,'right_subjecttype_id':lo.id}
             rt=Relationtype.objects.create(**dict1)
             rt.sites.add(Site.objects.get_current())
             rt.save()

def create_attribute_type():
   rel_list=[]
   relid_list=[]
   relnid=[]
   reltitle=[]
   lo=Metatype.objects.get(title='concept')
   loid=NID.objects.get(id=lo.id)
   rel_list=Attributetype.objects.all()
   for i in rel_list:
        relid_list.append(i.id)
   for s in relid_list:
        relnid.append(NID.objects.get(id=s))
   for s in relnid:
        reltitle.append(str(s.title))
   if atnids <> []:
      for i in atnids:
         if i not in reltitle:
            slu=slugify(i)
            dict={'title':i,'slug':slu,'content':'','subjecttype_id':loid.id}
            at=Attributetype.objects.create(**dict)
            at.sites.add(Site.objects.get_current())
            at.save()
   if attributes <> []:
      for i in attributes:
         if i not in reltitle:
            slu=slugify(i)
            dict={'title':i,'slug':slu,'content':'','subjecttype_id':loid.id}
            at=Attributetype.objects.create(**dict)
            at.sites.add(Site.objects.get_current())
            at.save()


# def create_objects(obtype):    
#     for ob in niob: 
#         if not niob[ob] in listobjs:
#            auth_list_niob=[]
#            for n in s.getAllSnapshots('ssid',str(ob)):
#               auth_list_niob.append(s.getUsernamefromUserId(s.getAuthor(n)))
#            #print auth_list_niob
#            authors=[]     
#            for i in Author.objects.all():
#               authors.append(str(i.username))
#            auth=[]
#            for i in auth_list_niob:
#               if not i in authors:
#                  user = User(
#                    username=i,                 
#                    is_active=True,
#                    is_staff=True,
#                    is_superuser=False)
#                  user.save() 
#               auth.append(Author.objects.get(username=i))
#            dict={'title':niob[ob],'content':'','slug':ob}
#            obj=Gbobject.objects.create(**dict)
#            obj.objecttypes.add(Objecttype.objects.get(title=obtype))
#            obj.sites.add(Site.objects.get_current())
#            for i in auth:
#                obj.authors.add(i)
#            obj.save()
           
#            if attributes<>{}:             
#               for i in attributes:
#                  ot=Gbobject.objects.get(title=niob[ob])
#                  oid=NID.objects.get(id=ot.id)
#                  at=Attributetype.objects.get(title=str(i))
#                  dict={'title':val,'slug':slu,'svalue':val,'subject':oid,'attributetype':at}
#                  att=Attribute.objects.create(**dict)
#                  att.save()
 
#     for ob in objdict: 
#         nbh1={}
#         obj={}
#         objattributes={}
#         objatlist=[]
#         obstr=str(ob)
#         if not objdict[ob] in listobjs:           
#            nbh1=s.getNeighbourhood([obstr],'rendered_nbh')
#            #print nbh1
#            obj=nbh1[ob]
#            #print obj
#            if obj.has_key('attributes'):
#               objattributes=obj['attributes']
#               #print '\n\n',objattributes
#               for i in objattributes:
#                  objatlist=objattributes[i]
#               objval=objatlist[1]
#               objslu=objatlist[0]
#               #print '\n\n',objatlist

#            auth_list_ob=[]
#            for n in s.getAllSnapshots('ssid',str(ob)):
#               auth_list_ob.append(s.getUsernamefromUserId(s.getAuthor(n)))
#            authors=[]     
#            for i in Author.objects.all():
#               authors.append(str(i.username))
#            auth=[]
#            for i in auth_list_ob:
#               if not i in authors:
#                  user = User(
#                    username=i,                 
#                    is_active=True,
#                    is_staff=True,
#                    is_superuser=False)
#                  user.save()
#               auth.append(Author.objects.get(username=i))
#            dict={'title':objdict[ob],'content':'','slug':ob}
#            obj=Gbobject.objects.create(**dict)
#            obj.objecttypes.add(Objecttype.objects.get(title=obtype))
#            obj.sites.add(Site.objects.get_current())
#            for i in auth:
#                obj.authors.add(i)
#            obj.save()   
           
#            if objattributes <> {}:
#               for i in objattributes:
#                  print objattributes[i]
#                  ot=Gbobject.objects.get(title=objdict[ob])
#                  oid=NID.objects.get(id=ot.id)
#                  at=Attributetype.objects.get(title=str(i))
#                  dict1={'title':objval,'slug':objslu,'svalue':objval,'subject':oid,'attributetype':at}
#                  att=Attribute.objects.create(**dict1)
#                  att.save()      
                 
                 
            

def create_relations():    
    for i in niob:
        lo=Objecttype.objects.get(title=niob[i])
        loid=NID.objects.get(id=lo.id)    
    
        if ni_listsutype <> []:
          for i in ni_listsutype:         
            ro=Objecttype.objects.get(title=ni_listsutype[i])
            rid=NID.objects.get(id=ro.id)
            rt=Relationtype.objects.get(title='subtypeof')
            rtid=NID.objects.get(id=rt.id)
            try:
               slu=slugify('sub type of')
               dict={'title':'sub type of','slug':slu,'left_subject_id':loid.id,'right_subject_id':rid.id,'relationtype_id':rtid.id,'left_subject_scope':'','right_subject_scope':'','relationtype_scope':''}
               rtt=Relation.objects.create(**dict)
               rtt.save()
            except IntegrityError:
               pass
            

        if ni_listrins <> []:
          for i in ni_listrins:          
              ro=Metatype.objects.get(title=ni_listrins[i])
              rid=NID.objects.get(id=ro.id)
              rt=Relationtype.objects.get(title='instanceof')
              rtid=NID.objects.get(id=rt.id)
              try:
                 slu=slugify('instance of')
                 dict={'title':'instance of','slug':slu,'left_subject_id':loid.id,'right_subject_id':rid.id,'relationtype_id':rtid.id,'left_subject_scope':'','right_subject_scope':'','relationtype_scope':''}
                 rtt=Relation.objects.create(**dict)
                 rtt.save()
              except IntegrityError:
                 pass

        if ni_listrdep <> []:    
          for i in ni_listrdep:          
              ro=Objecttype.objects.get(title=ni_listrdep[i])
              rid=NID.objects.get(id=ro.id)
              rt=Relationtype.objects.get(title='dependson')
              rtid=NID.objects.get(id=rt.id)
              try:
                 slu=slugify('depends on')
                 dict={'title':'depends on','slug':slu,'left_subject_id':loid.id,'right_subject_id':rid.id,'relationtype_id':rtid.id,'left_subject_scope':'','right_subject_scope':'','relationtype_scope':''}
                 rtt=Relation.objects.create(**dict)
                 rtt.save()
              except IntegrityError:
                 pass

        if ni_listlcon <> []:
          for i in ni_listlcon:          
              ro=Objecttype.objects.get(title=ni_listlcon[i])
              rid=NID.objects.get(id=ro.id)
              rt=Relationtype.objects.get(title='contains')
              rtid=NID.objects.get(id=rt.id)
              try:
                 slu=slugify('contains')
                 dict={'title':'contains','slug':slu,'left_subject_id':rid.id,'right_subject_id':loid.id,'relationtype_id':rtid.id,'left_subject_scope':'','right_subject_scope':'','relationtype_scope':''}
                 rtt=Relation.objects.create(**dict)
                 rtt.save()
              except IntegrityError:
                 pass

        if ni_listldep <> []:
          for i in ni_listldep:          
              ro=Objecttype.objects.get(title=ni_listldep[i])
              rid=NID.objects.get(id=ro.id)
              rt=Relationtype.objects.get(title='dependson')
              rtid=NID.objects.get(id=rt.id)
              try:
                 slu=slugify('depends on')
                 dict={'title':'depends on','slug':slu,'left_subject_id':rid.id,'right_subject_id':loid.id,'relationtype_id':rtid.id,'left_subject_scope':'','right_subject_scope':'','relationtype_scope':''}
                 rtt=Relation.objects.create(**dict)
                 rtt.save()
              except IntegrityError:
                 pass
              



        

