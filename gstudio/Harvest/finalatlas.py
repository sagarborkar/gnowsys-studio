# Copyright (c) 2011,  2012 Free Software Foundation

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.


import xmlrpclib
import inflect
from gstudio.models import *
from objectapp.models import *
from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify
from django.db import IntegrityError
from reversion.models import *

s=xmlrpclib.Server('http://sagarborkar:swagger1988@atlas.gnowledge.org/gnowql')

atlasots=s.getAll('gbobjecttypes')
listnew=[]
for i in atlasots:
  listnew.append(i)
# dicto=s.getAll('gbobjecttypes')
# listo=[]
# for i in dicto:
#   listo.append(i)

# listnew=[]
# l=3768
# while(listo[l]<>'ancestor'):
#   listnew.append(listo.pop())
#   l=l-1

# atlasots={}
# for i in dicto:
#    if i in listnew:
#       atlasots.update({i:dicto[i]})

listn=[]
for i in range(0,835):
   listn.append(listnew[i])

for i in atlasots.keys():
   if i in listn:
      del atlasots[i]

pluots=['The Law of Seggregation','checking subtraction by addition','Data (Raw material on which discipline of statistics is built)','compression of gas','expansion of gas','Hammer a Nail in the Wall or Wooden Plank','condensation of chromosomes','collision between molecules','segregation of alternative traits','LayerWise Hierarchial Classification of Programming Languages from Compiler Level to Content Management Level','sequence of symbols','division of a polynomial by a first-degree binomial','Male Enhancement by Sinrex','making half of a half','mutliplication of fractions by whole number','division of fractions by whole number','division of algebraic fractions','reduction of fractions','subtraction of algebraic fractions','elongation of spindle','formation of nuclear envelope','seggregation of chromosomes','dimension of vector space','breakdown of nuclear envelope','unit of measurement','recognition of alphabets','average kinetic energy of solvent molecules','accumulation of heritable traits','Explain your requirement to website designer for efficient website Design','solving division problems that result in reminder','type of types','surface-to-volume-ration','Probability(The measure of the likelihood of a random phenomenon or chance behaviour)','Hypothesis testing(A procedure based on sample evidence and probability, used to test claims regarding a characteristic of one or more populations)','Simple Random sampling(Each element of the universe has equal probability of selecction into the sample)','play with looking glass','go to vegetable market and name the vegetables','speed of light','Line graph of position of an object along a straight line','Line graph showing change in weight of man with age','theory of computation','Create WBS','Rate of Interest','sharing of electrons','divisibility of binomial','subtraction of polynomial','multiplication of polynomials','addition of polynomials','Air Sanitizer | Air Purifier | Deodorizer | Air Cleaner | Disinfectant | Swine Flu Sanitizer | CFL Bulbs','factorization of polynomials','multiplication of monomials','addition of monomials','taking out a common factor','checking division by multiplication','concentration of products','increase in oxidation state','Quinn Hobbs','subtracting large number from a small number','addition of algebraic fractions','divisability by numbers other than 1 and itself','concentration of reactants','order of operations','Ugg Boots, Uggs 100% Sheepskin,20-50% Off All Boots,Buy Now!','structure of a sentence','node of ranvier','nutrition for plants','sense of direction','consumption of energy','division of polynomials','spot the tree by flower','unit of inheritance','taking out common factor','ice in water','Childrens Observation about Plants','divisability by 2','take a note of the events at sunset','Law of Independent Assortment','condensation of chromosomes','acceleration due to gravity','astaga.com lifestyle on the net | mbah gendeng','angle of incidence','Vern Carlson','release of energy']

#atlasots=['22115']
pl=inflect.engine()
for gb in atlasots:

   ssid=atlasots[gb]
   #ssid=gb

   nidstr=str(atlasots[gb])
   #nidstr=str(gb)

   niob=s.getnids([atlasots[gb]])
   #niob=s.getnids([gb])
   #print niob

   nbh=s.getNeighbourhood([ssid],'rendered_nbh')[nidstr]
   #print nbh    #--"This works fine!-->returns the entire neighbourhood of the node"

   rtypes=[]
   rtlist=[]
   rtypesnids={}
   relationsnids=[]
   relationtypes={}
   rolessids_rt=[]
   rolessids_lt=[]
   ni_listrt={}
   ni_listlt={}
   ni_listr=[]
   ni_listl=[]
   ni_listrins={}
   ni_listrdep={}
   ni_listsutype={}
   ni_listlcon={}
   ni_listldep={}
   dict={}
   auth_list_niob=[]
   auth_list_ob=[]
   objdict={}
   attributes={}
   atlist=[]
   atnids={}
  


   if nbh.has_key('relationtypes'):
      rtypes=nbh['relationtypes']
      #print rtypes
      for rt in rtypes:
         rtypesnids.update(s.getnids([rt]))
      #print rtypesnids   
   
   if nbh.has_key('attributetypes'):
      ats = nbh['attributetypes']
      #print '\n\n',ats      
      if ats <> []:
         for at in ats:
            atnids.update(s.getnids([at]))      
            #print'\n\n',atnids  

   if nbh.has_key('relations'):
      relations=nbh['relations']
      #print relations
      relationsnids=relations.keys()

      #print "Relations Are\n",relations   #--"This works fine!-->Returns the relations of the node viz instanceof, contains etc" 
      #print "\n\nRelation Nids Are \n",relationsnids  # --"this works fine!-->Returns the name of the relations viz instanceof, contains, dependson"

      relationtypes=s.getInverseNames(relationsnids)
      #print "\n\nThe Inverse Names Of The Relations Are\n",relationtypes  # --"This works fine!-->Returns the inverse names of all the relations viz instanceof:instance, contains:inverse_of_contains"

      for rt in relationsnids:
         try:
            subjectssidsrt=relations[rt]['rightroles']
            #print "\n\nThe subject ssids of "+rt+" rightroles are as follows :\n"
            #print subjectssidsrt
            
            # print '\n\nEach subjectsssid of '+rt+' is as follows :\n'
            if rt=='subtypeof':
               for i in subjectssidsrt:
                   ni=s.getnids([i])
                   ni_listsutype.update(ni)
 
            if rt =='instanceof':
               for i in subjectssidsrt:
                   ni=s.getnids([i])
                   ni_listrins.update(ni)
           
            if rt =='dependson':
               for i in subjectssidsrt:
                   ni=s.getnids([i])
                   ni_listrdep.update(ni)
               

           
            # for each in subjectssidsrt:
            #     rolessids_rt.append(each)                
            # print rolessids_rt         
             

         except:
            pass
         try:
            subjectssidslt=relations[rt]['leftroles']
            #print '\n\nThe subject ssids of '+rt+' leftroles are as follows :\n'
            #print subjectssidslt     #---This works fine!-->Returns the leftroles for contains and depends on relations.
            # print '\n\nEach subjectssid is as follows :\n'
            if rt == 'contains':
                for i in subjectssidslt:
                    ni=s.getnids([i])
                    ni_listlcon.update(ni)
            if rt == 'dependson':
                for i in subjectssidslt:
                    ni=s.getnids([i])
                    ni_listldep.update(ni)           
         except:
            pass

   if nbh.has_key('attributes'):
      attributes = nbh['attributes']
      #print attributes
      for i in attributes:
         atlist=attributes[i]
         #print atlist[1]
         val=atlist[1]
         

   # print '\n\nSub Type Of',ni_listsutype
   # print '\n\nInstance Of',ni_listrins
   # print '\n\nContains',ni_listlcon
   #print '\n\nDepends On',ni_listldep,'\n'
   #print ni_listrdep

   #for i in ni_listrins:
     # objkeys.append(i)
     # ni_listr.append(ni_listrins[i])
   objdict.update(ni_listrins)
     
   # for i in ni_listrdep:
   #     # objkeys.append(i)
   #     # ni_listr.append(ni_listrdep[i])
   objdict.update(ni_listrdep)

   # for i in ni_listsutype:
   #     # objkeys.append(i)
   #     # ni_listr.append(ni_listsutype[i])
   objdict.update(ni_listsutype)

   # for i in ni_listlcon:
   #      # objkeys.append(i)
   #      # ni_listl.append(ni_listlcon[i])
   objdict.update(ni_listlcon)
    
   # for i in ni_listldep:
   #     # objkeys.append(i)
   #     # ni_listl.append(ni_listldep[i])
   objdict.update(ni_listldep)
   #print ni_listldep

   #print objdict

   listo=[]
   for a in ni_listr:
      listo.append(a)
   for item in ni_listl:
      if not item in listo:
        listo.append(item)

   #print listo

   listobj=[]
   listobj=NID.objects.all()
   listobjs=[]
   for i in listobj:
      listobjs.append(str(i.title))
   #print listobjs

   @reversion.create_revision()
   def create_meta_type():
      try:
         meta=Metatype.objects.all()
         mettitle=[]      
         for i in meta:
            mettitle.append(str(i.title))
         con=s.getnids(['6233'])
         for i in con:
            if not con[i] in mettitle:            
               slu=slugify(con[i])
               mt=Metatype()
               mt.title=con[i]
               mt.slug=slu
               # dict={'title':con[i],'slug':slu}
               # mt=Metatype.objects.create(**dict) 
               with reversion.create_revision():
                  mt.save()
      except IntegrityError:
         pass
   
#   @reversion.create_revision()
   def create_object_type():
      #s=xmlrpclib.Server('http://sagarborkar:swagger1988@atlas.gnowledge.org/gnowql') 
      oterr=['a','D','l','R','s','K','L','concept','']
      try:
         for ob in niob: 
            if not niob[ob] in listobjs and not niob[ob] in oterr:
               objlist=[]
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
                     with reversion.create_revision():
                        user.save() 
                  auth.append(Author.objects.get(username=i))
               slu=slugify(niob[ob])
               if niob[ob] in pluots:
                  plu=niob[ob]
               else:
                  if pl.plural(niob[ob]) == pl.singular_noun(niob[ob]):
                     plu=niob[ob]
                  else:
                     plu=pl.plural(niob[ob])
               ot=Objecttype()
               ot.title=niob[ob]
               ot.slug=slu
               ot.plural=plu
               ot.content=''
               ot.status=2
               ot.save()
               obj=Objecttype.objects.get(title=niob[ob])
               # dict={'title':niob[ob],'slug':slu,'content':'','status':2}
               # obj=Objecttype.objects.create(**dict)            
               obj.sites.add(Site.objects.get_current())
               mt=Metatype.objects.get(title='concept')
               obj.metatypes.add(mt)
               for i in auth:
                  obj.authors.add(i) 
               with reversion.create_revision():
                  obj.save()
               gd=Objecttype.objects.get(title=niob[ob])
               print 'The Objecttype created is ',gd              
               
               objlist=NID.objects.filter(title=niob[ob])
               #print objlist
               if len(objlist) > 1 :
                  obje=objlist[0]
                  obje.delete()
                  del(obje)           
               

               if attributes<>{}:             
                  for i in attributes:
                     ot=Objecttype.objects.get(title=niob[ob])
                     oid=NID.objects.get(id=ot.id)
                     at=Attributetype.objects.get(title=str(i))
                     slua=slugify(val)
                     if niob[ob][0].isupper():
                       atname=val.lower()
                     else:
                       atname=val.capitalize()
                     att=Attribute()
                     att.title=atname
                     att.slug=slua
                     att.svalue=atname
                     att.subject=oid
                     att.attributetype=at
                     # dict={'title':val,'slug':slua,'svalue':val,'subject':oid,'attributetype':at}
                     # att=Attribute.objects.create(**dict) 
                     with reversion.create_revision():
                        att.save() 
      except IntegrityError:
         pass
      
      try:      
         for ob in objdict:            
            nbh1={}
            obj={}
            objrtypes={}
            objrtnids={}
            objattributes={}
            objatlist=[]
            obstr=str(ob)
            
            listsobj=[]
            listsobj=NID.objects.all()
            listsobjs=[]
            for i in listsobj:
              listsobjs.append(str(i.title))

            if not objdict[ob] in listsobjs and not objdict[ob] in oterr:           
               nbh1=s.getNeighbourhood([obstr],'rendered_nbh')
               #print nbh1
               obj=nbh1[ob]
               #print obj
               if obj.has_key('attributes'):
                  objattributes=obj['attributes']
                  #print '\n\n',objattributes
                  for i in objattributes:
                     objatlist=objattributes[i]
                  objval=objatlist[1].capitalize()              

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
                     with reversion.create_revision():
                        user.save()
                  auth.append(Author.objects.get(username=i))
               slu=slugify(objdict[ob])
               if objdict[ob] in pluots:
                  plu=objdict[ob]
               else:
                  if pl.plural(objdict[ob]) == pl.singular_noun(objdict[ob]):
                     plu=objdict[ob]
                  else:
                     plu=pl.plural(objdict[ob])
               ot=Objecttype()
               ot.title=objdict[ob]
               ot.slug=slu
               ot.plural=plu
               ot.content=''
               ot.save()
               # dict={'title':objdict[ob],'slug':slu,'content':'','status':2}
               # obj=Objecttype.objects.create(**dict)         
               obj=Objecttype.objects.get(title=objdict[ob])
               obj.sites.add(Site.objects.get_current())
               mt=Metatype.objects.get(title='concept')
               obj.metatypes.add(mt)
               for i in auth:
                  obj.authors.add(i) 
               with reversion.create_revision():
                  obj.save()
               gd=Objecttype.objects.get(title=objdict[ob])
               print 'The Second Objecttype created is ',gd
               
               objlist1=NID.objects.filter(title=objdict[ob])                           
               if len(objlist1) > 1 :
                  obje=objlist1[0]
                  obje.delete()
                  del(obje)      
               
               if objattributes <> {}:
                  for i in objattributes:
                     #print objattributes[i]
                     ot=Objecttype.objects.get(title=objdict[ob])
                     oid=NID.objects.get(id=ot.id)
                     at=Attributetype.objects.get(title=str(i))
                     objslu=slugify(objval)
                     if objdict[ob][0].isupper():
                       atname=objval.lower()
                     else:
                       atname=objval.capitalize()
                     oatt=Attribute()
                     oatt.title=atname
                     oatt.slug=objslu
                     oatt.svalue=atname
                     oatt.subject=oid
                     oatt.attributetype=at
                     # dict1={'title':objval,'slug':objslu,'svalue':objval,'subject':oid,'attributetype':at}
                     # att=Attribute.objects.create(**dict1)
                     with reversion.create_revision():
                        oatt.save()
      except IntegrityError:
         pass
   
   @reversion.create_revision()
   def create_post_nodes():
      objs=['Y','Relative frequency distribution','a','D','l','R','s','K','L']
      for ob in niob:
        print niob[ob]
        if not niob[ob] in objs:
          try:
            ot=Objecttype.objects.get(title=niob[ob])               
          except Objecttype.DoesNotExist:
            pass
       
          if ni_listrdep <> {}:
            for i in ni_listrdep:
              try:
                rdep=Objecttype.objects.get(title=ni_listrdep[i])
              except Objecttype.DoesNotExist:
                pass
              ot.prior_nodes.add(rdep)
              with reversion.create_revision():
                ot.save()

          if ni_listldep <> {}:
            for j in ni_listldep:
              try:
                ldep=Objecttype.objects.get(title=ni_listldep[j])
              except Objecttype.DoesNotExist:
                pass
              ot.posterior_nodes.add(ldep)
              with reversion.create_revision():
                ot.save()

   @reversion.create_revision()
   def create_relation_type(): 
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
      # try:
      #    if rtypesnids <> {}:
      #       for i in rtypesnids:       
      #          if not i in reltitle: 
      #             rtitle=rtypesnids[i].capitalize()
      #             slu=slugify(rtypesnids[i])
      #             rt=Relationtype()
      #             rt.title=rtitle
      #             rt.slug=slu
      #             rt.inverse=rtitle
      #             rt.left_subjecttype_id=lo.id
      #             rt.right_subjecttype_id=lo.id
      #             rt.content=''
      #             rt.save()
      #             # dict={'title':rtitle,'inverse':rtitle,'slug':slu,'content':'','left_subjecttype_id':lo.id,'right_subjecttype_id':lo.id}
      #             # rt=Relationtype.objects.create(**dict)
      #             rtt=Relationtype.objects.get(title=rtitle)
      #             rtt.sites.add(Site.objects.get_current())
      #             with reversion.create_revision():
      #                rtt.save()
      # except IntegrityError:
      #    pass
   
      try:             
         if relationtypes <> {}:
            for r in relationtypes:
               if not r in reltitle:
                  slu=slugify(r)
                  rt=Relationtype()
                  rt.title=r
                  rt.slug=slu
                  rt.inverse=relationtypes[r]
                  rt.left_subjecttype_id=lo.id
                  rt.right_subjecttype_id=lo.id
                  rt.content=''
                  rt.save()
                  # dict1={'title':rt,'inverse':relationtypes[rt],'slug':slu,'content':'','left_subjecttype_id':lo.id,'right_subjecttype_id':lo.id}
                  # rt=Relationtype.objects.create(**dict1)
                  rtt=Relationtype.objects.get(title=r)
                  rtt.sites.add(Site.objects.get_current())
                  with reversion.create_revision():
                     rtt.save()
      except IntegrityError:
         pass

   @reversion.create_revision()
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
      try:
         if atnids <> []:
            for i in atnids:
               if i not in reltitle:
                  slu=slugify(i)
                  at=Attributetype()
                  at.title=i
                  at.slug=slu
                  at.content=''
                  at.subjecttype_id=loid.id
                  at.save()
                  # dict={'title':i,'slug':slu,'content':'','subjecttype_id':loid.id}
                  # at=Attributetype.objects.create(**dict)
                  att=Attributetype.objects.get(title=i)
                  att.sites.add(Site.objects.get_current()) 
                  with reversion.create_revision():
                     att.save()
      except IntegrityError:
         pass
      
      try:
         if attributes <> []:
            for i in attributes:
               if i not in reltitle:
                  slu=slugify(i)
                  at=Attributetype()
                  at.title=i
                  at.slug=slu
                  at.content=''
                  at.subjecttype_id=loid.id
                  at.save()
                  # dict={'title':i,'slug':slu,'content':'','subjecttype_id':loid.id}
                  # at=Attributetype.objects.create(**dict)
                  att=Attributetype.objects.get(title=i)
                  att.sites.add(Site.objects.get_current())
                  with reversion.create_revision():
                     att.save()
      except IntegrityError:
         pass
                 
            
   @reversion.create_revision()
   def create_relations(): 
      lo=''
      loid=''
      oberror=['','Unix Backups','Hospital','snowbird','University','Work','homogeneous state','Water','a','D','l','R','s','K','L']
      for i in niob :
         if not niob[i] in oberror:
            try:
              lo=Objecttype.objects.get(title=niob[i])
              loid=NID.objects.get(id=lo.id)
            except Objecttype.DoesNotExist:
              pass
           
            if ni_listsutype <> []:
               for i in ni_listsutype: 
                  try:
                     #lo=Objecttype.objects.get(title=niob[i])
                     #loid=NID.objects.get(id=lo.id)    
                     ro=Objecttype.objects.get(title=ni_listsutype[i])
                     rid=NID.objects.get(id=ro.id)
                     rt=Relationtype.objects.get(title='subtypeof')
                     rtid=NID.objects.get(id=rt.id)
                  except Objecttype.DoesNotExist:
                     pass
               
                  try:
                     slu=slugify('sub type of')
                     rts=Relation()
                     rts.title='sub type of'
                     rts.slug=slu
                     rts.left_subject_id=loid.id
                     rts.right_subject_id=rid.id
                     rts.relationtype_id=rtid.id
                     rts.left_subject_scope=''
                     rts.right_subject_scope=''
                     rts.relationtype_scope=''                     
                     # dict={'title':'sub type of','slug':slu,'left_subject_id':loid.id,'right_subject_id':rid.id,'relationtype_id':rtid.id,'left_subject_scope':'','right_subject_scope':'','relationtype_scope':''}
                     # rtt=Relation.objects.create(**dict) 
                     with reversion.create_revision():
                        rts.save()
                  except IntegrityError:
                     pass            

            if ni_listrins <> []:
               for i in ni_listrins:   
                  try:
                     #lo=Objecttype.objects.get(title=niob[i])
                     #loid=NID.objects.get(id=lo.id)    
                     ro=Metatype.objects.get(title=ni_listrins[i])
                     rid=NID.objects.get(id=ro.id)
                     rt=Relationtype.objects.get(title='instanceof')
                     rtid=NID.objects.get(id=rt.id)
                  except Objecttype.DoesNotExist:
                     pass

                  try:                     
                     slu=slugify('instance of')
                     rts=Relation()
                     rts.title='instance of'
                     rts.slug=slu
                     rts.left_subject_id=loid.id
                     rts.right_subject_id=rid.id
                     rts.relationtype_id=rtid.id
                     rts.left_subject_scope=''
                     rts.right_subject_scope=''
                     rts.relationtype_scope=''          
                     # dict={'title':'instance of','slug':slu,'left_subject_id':loid.id,'right_subject_id':rid.id,'relationtype_id':rtid.id,'left_subject_scope':'','right_subject_scope':'','relationtype_scope':''}
                     # rtt=Relation.objects.create(**dict)                     
                     with reversion.create_revision():
                        rts.save()
                  except IntegrityError:
                     pass

            if ni_listrdep <> []:    
               for i in ni_listrdep:   
                  try:
                     #lo=Objecttype.objects.get(title=niob[i])
                     #loid=NID.objects.get(id=lo.id)    
                     ro=Objecttype.objects.get(title=ni_listrdep[i])
                     rid=NID.objects.get(id=ro.id)
                     rt=Relationtype.objects.get(title='dependson')
                     rtid=NID.objects.get(id=rt.id)
                  except Objecttype.DoesNotExist:
                     pass 
                  try:
                     slu=slugify('depends on')
                     rts=Relation()
                     rts.title='depends on'
                     rts.slug=slu
                     rts.left_subject_id=loid.id
                     rts.right_subject_id=rid.id
                     rts.relationtype_id=rtid.id
                     rts.left_subject_scope=''
                     rts.right_subject_scope=''
                     rts.relationtype_scope=''          
                     # dict={'title':'depends on','slug':slu,'left_subject_id':loid.id,'right_subject_id':rid.id,'relationtype_id':rtid.id,'left_subject_scope':'','right_subject_scope':'','relationtype_scope':''}
                     # rtt=Relation.objects.create(**dict)
                     with reversion.create_revision():
                        rts.save()
                  except IntegrityError:
                     pass

            if ni_listlcon <> []:
               for i in ni_listlcon: 
                  try:
                     #lo=Objecttype.objects.get(title=niob[i])
                     #loid=NID.objects.get(id=lo.id)    
                     ro=Objecttype.objects.get(title=ni_listlcon[i])
                     rid=NID.objects.get(id=ro.id)
                     rt=Relationtype.objects.get(title='contains')
                     rtid=NID.objects.get(id=rt.id)
                  except Objecttype.DoesNotExist:
                     pass

                  try:
                     slu=slugify('contains')
                     rts=Relation()
                     rts.title='contains'
                     rts.slug=slu
                     rts.left_subject_id=rid.id
                     rts.right_subject_id=loid.id
                     rts.relationtype_id=rtid.id
                     rts.left_subject_scope=''
                     rts.right_subject_scope=''
                     rts.relationtype_scope=''          
                     # dict={'title':'contains','slug':slu,'left_subject_id':rid.id,'right_subject_id':loid.id,'relationtype_id':rtid.id,'left_subject_scope':'','right_subject_scope':'','relationtype_scope':''}
                     # rtt=Relation.objects.create(**dict)
                     with reversion.create_revision():
                        rts.save()
                  except IntegrityError:
                     pass

            if ni_listldep <> []:
               for i in ni_listldep: 
                  #print ni_listldep[i]
                  try:  
                     #lo=Objecttype.objects.get(title=niob[i])
                     #loid=NID.objects.get(id=lo.id)    
                     ro=Objecttype.objects.get(title=ni_listldep[i])
                     rid=NID.objects.get(id=ro.id)
                     rt=Relationtype.objects.get(title='dependson')
                     rtid=NID.objects.get(id=rt.id)
                  except Objecttype.DoesNotExist:
                     pass
                  try:
                     slu=slugify('depends on')
                     rts=Relation()
                     rts.title='depends on'
                     rts.slug=slu
                     rts.left_subject_id=rid.id
                     rts.right_subject_id=loid.id
                     rts.relationtype_id=rtid.id
                     rts.left_subject_scope=''
                     rts.right_subject_scope=''
                     rts.relationtype_scope=''          
                     # dict={'title':'depends on','slug':slu,'left_subject_id':rid.id,'right_subject_id':loid.id,'relationtype_id':rtid.id,'left_subject_scope':'','right_subject_scope':'','relationtype_scope':''}
                     # rtt=Relation.objects.create(**dict)                     
                     with reversion.create_revision():
                        rts.save()
                  except IntegrityError:
                     pass       


   create_meta_type()
   create_attribute_type()
   create_object_type()
   create_post_nodes()
   create_relation_type()
   create_relations()

        

