import re
import unidecode

def RecursivePrintDict(dictio, of, indent=0, start='- '):
    for k, v in dictio.items():
        key = re.sub(r'\s+', '_', f'{k}')
        key = unidecode.unidecode(key)
        if isinstance(v, dict):
            of.write('  ' * indent + f'{start}{key}:\n')
            if k == 'requisitos' or k == 'oferecimento' or k == 'vagas' or k == 'aulas':
                RecursivePrintDict(v, of, indent+1)
            else:
                RecursivePrintDict(v, of, indent+1, start='')
        else:
            val = f'{v}'.replace('"', '')
            if 'docente' in k:
                of.write('  ' * indent + f'{start}{key}: {val}\n')
            else:
                of.write('  ' * indent + f'{start}{key}: "{val}"\n')