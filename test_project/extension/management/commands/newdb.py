import urllib
from bs4 import BeautifulSoup
import re
from django.core.management.base import BaseCommand
from institution.models import Institute
from django.db import IntegrityError
urls="http://www.jagranjosh.com/institutes-colleges/list-az-"
urls1="http://www.jagranjosh.com"

class Command(BaseCommand):
    def handle(self,*args,**options):
        def get_course_detail(urlss):
                try:
                        a = []
                        html=urllib.urlopen(urls1+urlss)
                        bsObj=BeautifulSoup(html,"html.parser")
                        text=bsObj.find("",{"class":"pB5 innerHeadings fL"})
                        collegename = text.get_text()
                        print collegename
                        text2=bsObj.find("",{"class":"fF pB10 bdr-b"})
                        collegeabout = text2.get_text().replace('"',' ')
                        for link in bsObj.find("",{"class":"select"}).findAll("a",href=re.compile("^(/institutes-colleges/)")):
                                if 'href' in link.attrs:
                                        urls2=link.attrs['href']
                                        html1=urllib.urlopen(urls1+urls2)
                                        bsObj1=BeautifulSoup(html1,"html.parser")
                                        for link1 in bsObj1.findAll("",{"class":"insti_box"}):
                                                for link2 in link1.findAll("a",href=re.compile("^(/institutes-colleges/)")):
                                                    a.append(link2.get_text())
                        collegecourses="\n".join(a)
                        print collegecourses
                        inst=Institute(name=collegename,about=collegeabout,courses=collegecourses)
                        inst.save()
                        print"--------------------------------------------"
                except AttributeError,IndexError:
                        return
                
        i=97
        while i<123:
            var=chr(i)
            print var
            html=urllib.urlopen(urls+var)
            bsObj=BeautifulSoup(html, "html.parser")
            var1=bsObj.findAll("",{"class":"listitems_bulletline"})
            for name in var1:
                for link in name.findAll("a",href=re.compile("^(/institutes-colleges/)")):
                    if 'href' in link.attrs:
                        get_course_detail(link.attrs['href'])
            k=0
            j=1
            while j>=1:
                r = str(j)
                print r
                bsa=urllib.urlopen(urls+var+'-'+r+"-20")
                bsObj=BeautifulSoup(bsa,"html.parser")
                var1=bsObj.findAll("",{"class":"listitems_bulletline"})
                j+=1
                for name in var1:
                     wer = name.findAll("a",href=re.compile("^(/institutes-colleges/)"))
                     if wer:
                            for link in wer:
                                if 'href' in link.attrs:
                                    sop=link.attrs['href']
                                    if sop and sop.strip():
                                                    get_course_detail(sop)                      
                                    else:
                                                    break
                     else:
                         k=1
                         break
                if k==1:
                     break
                            
            i+=1