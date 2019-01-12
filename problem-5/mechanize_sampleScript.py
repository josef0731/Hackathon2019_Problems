'''
This will help you to login to one site and download a page for example:
https://stackoverflow.com/questions/3516655/python-auto-fill-with-mechanize
'''

import mechanize
import os

def submit_form(input_type, input, TM = False, organism_group = 'eukaryote'):
    '''
    submit form depending on input_type
    :param input_type: type of input; either 'file' or 'sequences'
    :param input: the input; format:
        ## if input_type is 'file': a string pointing to the file to be uploaded
        ## if input_type is 'sequence': a list of dictionary of format {seqname: seq}
    :param TM: whether to use the transmembrane (TM) version of the algorithm or not. Default False.
    :organism_group: any one of 'eukaryote', 'gram_pos' or 'gram_neg'. Default 'eukaryote'.
    '''
    if isinstance(TM, bool) is False:
        raise TypeError('TM has to be a bool.')
    if isinstance(organism_group, str) is False or organism_group not in ['eukaryote', 'gram_pos', 'gram_neg']:
        raise TypeError('organism_group has to be a str and any one of "eukaryote", "gram_pos" or "gram_neg".')
    if isinstance(input_type, str) is False or input_type not in ['file', 'sequences']:
        raise TypeError('input_type has to be a str and any one of "file" or "sequences".')

    br=mechanize.Browser()
    br.open('http://www.cbs.dtu.dk/services/SignalP/')
    br.select_form(nr=0) #check yoursite forms to match the correct number

    if input_type is 'sequences':
        inputstr = ''
        for item in input:
            if isinstance(item, dict) is False:
                raise TypeError('input should be a list of dictionaries of format {seqname: seq}.')
            else:
                inputstr += '>' + item.keys()[0] + '\r' + items.values()[0] + '\r'
        br['SEQPASTE'] = inputstr # fill sequences into textbox
    elif input_type is 'file':

    # select TM or noTM
    if TM is True:
        br.find_control("method").get("notm").selected = True

    # select organism_group
    if organism_group is 'gram_pos':
        br.find_control("orgtype").get("gram+").selected = True
    elif organism_group is 'gram_pos':
        br.find_control("orgtype").get("gram-").selected = True

    response = br.submit() # submit
    resultpage = response.geturl() # get results
    if isinstance(resultpage, str) is True:
        newpage = br.open(newpage)
        return newpage.read()

    return None

def find_link(html, regex, base = '', dl = True):
    '''
    find links in html and download if indicated
    :param html: str of html texts (not splitted by line yet), as obtained from submit_form
    :param regex: the regex with which to find the suitable line from html and extract the href
    :param base: str of base website to concatenat the link with. Default is empty.
    '''        
