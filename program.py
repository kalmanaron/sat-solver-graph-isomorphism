import CNFConstructor as CNFC
import Graph as G
import ResultDecoder as RD
import subprocess
import sys
import tempfile
import os

PATH_TO_GLUCOSE = '../glucose/simp/glucose'
PATH_TO_CNF_CREATED = './_formula.cnf'
PATH_TO_RESULTS_CREATED = './_results.txt'

def upon_exit():
    os.remove(PATH_TO_CNF_CREATED)
    os.remove(PATH_TO_RESULTS_CREATED)

def help_message():
    print('USAGE:')
    print('python program.py file1 file2 OPTIONS')
    print('    - file[1,2] are the paths to the 2 graphs tested for being isomorphic')
    print('    - OPTIONS = [ -show-cnf, -show-stats ]')    

if (len(sys.argv) < 3):
    help_message()
    exit()

try:
    G1 = G.Graph()
    G2 = G.Graph()
    G1.loadGraphFromFile(sys.argv[1])
    G2.loadGraphFromFile(sys.argv[2])

except FileNotFoundError:
    print('Enter valid file paths')
    help_message()
    exit()
except ValueError:
    print('Enter a valid files with the adjency matrixes')
    help_message()
    exit()
except IndexError:
    print('Enter 2 valid file paths as arguments.')
    help_message()
    exit()

CNF = CNFC.CNFConstructor(G1,G2)
CNF.generateCNF()
CNF.writeDIMACS_CNFinto(PATH_TO_CNF_CREATED)

process = subprocess.run(
    [
    PATH_TO_GLUCOSE,
    PATH_TO_CNF_CREATED,
    PATH_TO_RESULTS_CREATED
    ],
    capture_output=True,
    text=True
)

if process.stderr != '':
    print('Unknown error occured in Glucose')
    print(process.stderr)
    exit()

if 'UNSATISFIABLE' in process.stdout:
    print('The graphs are not isomorphic.')
elif 'SATISFIABLE' in process.stdout:
    decoder = RD.ResultDecoder(G1.getNumberOfVertecies())
    decoder.decodeFromFile(PATH_TO_RESULTS_CREATED)
    decoder.output()

if '-show-cnf' in sys.argv:
    print()
    print('---------------- DIMACS CNF ----------------')
    print(CNF.getDimacsCNF()[:-1])
    print('----------------  CNF END   ----------------')
if '-show-stats' in sys.argv:
    print()
    print('------------ GLUCOSE STATISTICS ------------')
    print(process.stdout)

upon_exit()