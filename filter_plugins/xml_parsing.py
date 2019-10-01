import sys
import json
import re
import os

class FilterModule(object):
    ''' A filter to parse shell outputs to dictionaries '''
    def filters(self):
        return {
            'xml_parsing': xml_parsing
        }

def xml_parsing(content):
    xml_data=content
    F1=[]
    output={}
    domains=0

    print xml_data

    for i in range(0,len(xml_data)):
        if '<domain type=' in xml_data[i]:
            domains += 1
            while not '</domain>' in xml_data[i]:
                F1.append(xml_data[i])
                i += 1
            F1.append(xml_data[i])
            with open('vm_'+str(domains)+'.xml', 'w') as f:
                for item in F1:
                    print >> f, item
            output['domains'+str(domains)]=F1
            os.remove('vm_'+str(domains)+'.xml')
            F1=[]
    
    return json.dumps(output,ensure_ascii=False)
