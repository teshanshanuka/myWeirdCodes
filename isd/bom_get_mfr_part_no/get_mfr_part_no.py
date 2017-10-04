links = 'links.csv'

wf = open('extracted_data.csv', 'w')

with open(links, 'r') as f:
    while True:
        url = f.readline()
        if url == '':
            break
        ll = url.split('/')
        try:
            mfr_index = ll.index('ProductDetail')+1
            mfr_part_no_index = mfr_index+1
            wf.write(','.join((url.replace('\n',''), ll[mfr_index], ll[mfr_part_no_index])) + '\n')
            print(','.join((url.replace('\n',''), ll[mfr_index], ll[mfr_part_no_index])))
        except ValueError:
            wf.write(url.replace('\n','') + ',' + 'not a mouser part\n')
wf.close()
