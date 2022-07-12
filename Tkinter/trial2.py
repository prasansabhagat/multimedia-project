import os
a="C:/Users/crksh/Downloads/carrier.jpg"
b="C:/Users/crksh/Downloads/hide.jpg"
c="C:/Users/crksh/Downloads/output.png"
os.system(f'python trial.py merge --image1={a} --image2={b} --output={c}')
os.system(f'python trial.py unmerge --image={c} --output=res/output2.png')