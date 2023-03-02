import pandas as pd
import argparse

def parse_opt():
   parser = argparse.ArgumentParser()
   parser.add_argument('--file-name', type=str, default='')
   opt = parser.parse_args()
   return opt

def run(file_name=''):
    print(file_name)
    df = pd.read_csv(file_name)
    pd.set_option('mode.chained_assignment', None)
    print(df.shape[0])
    print(df)
    for i in range(df.shape[0]):
        if df.Side[i] == 'bottom':
            df.Side[i] = 'B'
        if df.Side[i] == 'top':
            df.Side[i] = 'T'
    print(df)
    output = pd.DataFrame(
        {'Designator': df.Ref,
        'Footprint': df.Package,
        'Pos X': df.PosX,
        'Pos Y': df.PosY,
        'Ref X': df.Side,
        'Ref Y': df.Rot,
        'Pad X': df.Val})
    output.loc[-1] = ['"', '', '', '', '', '', '']
    output.index = output.index + 1
    output = output.sort_index()
    print(output)    
    output.to_csv('output.csv', index=False)


def main(opt):
    run(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
