import sys
import os

def indent(line, debth):
    line = line.strip()
    return ("    " * debth) + line

def opening_statement(line, debth):
    if line[-1] != ":":
        line = line + ":"
    return indent(line, debth)

def branch(line, debth):
    return indent(line[1:], debth)


def _parse(code, is_module):
    # TODO: check long string (""" val """)
    debth = 0
    new_code = []
    for line_idx in xrange(len(code)):
        if is_module:
            if "import normalyze" in code[line_idx] or "from normalyze" in code[line_idx] or "normalyze.run" in code[line_idx]:
                continue
        if len(code[line_idx]) > 0 and code[line_idx][0] == '{' and line_idx != 0:
            i = -1
            while new_code[i].strip() == "":
                i -= 1
            
            j = -1
            while new_code[j].strip() != new_code[i].strip():
                j -= 1

            new_code[i] = opening_statement(new_code[j], debth)
            line = branch(code[line_idx], debth)
            if line.strip() != "":
                new_code.append(line)
            debth += 1
        elif len(code[line_idx]) > 0 and code[line_idx][0] == '}':
            line = branch(code[line_idx], debth)
            if line.strip() != "":
                new_code.append(line)
            debth -= 1
        else:
            new_code.append(indent(code[line_idx], debth))
    return new_code

def _load(codelist):
    code = "\n".join(codelist)
    exec(code)

def parse_file_and_load(file_path, is_module = False):
    if ".npy" not in file_path[-4:]:
        raise(Exception("Error: not npy file"))

    with open(file_path, 'r') as f:
        code = [x.strip() for x in f.read().splitlines()]
    
    code = _parse(code, is_module)

    _load(code)


def main(args):
    is_dir = False
    for arg in args:
        if '-d' == arg:
            is_dir = True
        
    path = os.path.abspath(args[-1])
    
    if is_dir:
        for root, _, files in os.walk(path):
            for ffile in files:
                file_path = os.path.join(root, ffile)
                parse_file_and_load(file_path) 
    else:
        parse_file_and_load(path)


def parse_importer_file(file_path):
    parse_file_and_load(file_path, True)

def run(file_path):
    parse_importer_file(os.path.realpath(file_path))

#if __name__ == "normalyze":

if __name__ == "__main__":
    main(sys.argv)