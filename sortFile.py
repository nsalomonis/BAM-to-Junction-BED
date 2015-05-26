import string,sys

def exportSorted(filename, ouput_file, col_sort):
    index = []
    f = open(filename)
    firstLine = True
    while True:
        offset = f.tell()
        line = f.readline()
        if not line: break
        length = len(line)
        col = line.split('\t')[sort_col].strip()
        if firstLine:
            header = line
            firstLine = False
        else:
            index.append((col, offset, length))
    f.close()
    index.sort()
    
    o = open(ouput_file,'w')
    f = open(filename)
    o.write(header)
    for col, offset, length in index:
        #print col, offset, length
        f.seek(offset)
        o.write(f.read(length))
    o.close()
    
if __name__ == '__main__':
    filename = 'exp.myeloblast-steady-state.txt'
    sort_col = 0
    exportSorted(filename, sort_col)