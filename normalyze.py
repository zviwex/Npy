import sys
import os

def indent(line, depth):
    line = line.strip()
    return ("    " * depth) + line

def opening_statement(line, depth):
    if line[-1] != ":":
        line = line + ":"
    return indent(line, depth)

def branch(line, depth):
    return indent(line[1:], depth)


def _parse(code, is_module):
    depth = 0
    new_code = []
    for line_idx in xrange(len(code)):
        if is_module:
            code[line_idx] = code[line_idx].replace('"-"-"', '"""')
        if len(code[line_idx]) > 0 and code[line_idx][0] == '{' and line_idx != 0:
            i = -1
            while new_code[i].strip() == "":
                i -= 1
            
            j = -1
            while new_code[j].strip() != new_code[i].strip():
                j -= 1

            new_code[i] = opening_statement(new_code[j], depth)
            line = branch(code[line_idx], depth)
            if line.strip() != "":
                new_code.append(line)
            depth += 1
        elif len(code[line_idx]) > 0 and code[line_idx][0] == '}':
            line = branch(code[line_idx], depth)
            if line.strip() != "":
                new_code.append(line)
            depth -= 1
        else:
            new_code.append(indent(code[line_idx], depth))
    return new_code

def _load(codelist):
    code = "\n".join(codelist)
    exec(code, globals())

def parse_file_and_save(file_path, is_module = False):
    if ".npy" not in file_path[-4:]:
        raise(Exception("Error: not npy file"))

    with open(file_path, 'r') as f:
        code = [x.strip() for x in f.read().splitlines()]
    
    code = _parse(code, is_module)
    
    with open(file_path[:-4] + ".py", 'w') as f:
        f.write("\n".join(code))
    


def as_runner(args):
    is_dir = False
    for arg in args:
        if '-d' == arg:
            is_dir = True
        
    path = os.path.abspath(args[-1])
    
    if is_dir:
        for root, _, files in os.walk(path):
            for ffile in files:
                file_path = os.path.join(root, ffile)
                parse_file_and_save(file_path) 
    else:
        parse_file_and_save(path)



def run(code):
    code = [x.strip() for x in code.splitlines()]
    code = _parse(code, True)

    code = "\n".join(code)
    return(code)


if __name__ == "__main__":
    as_runner(sys.argv)