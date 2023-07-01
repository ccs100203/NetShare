# from os import listdir, system
# from os.path import isfile, exists
import os


# input_base = './input/caida'
# output_base = './output/caida'

# input_base = './exp_data/input'
# output_base = './exp_data/output'

# input_base = './numberofFlow/input'
# output_base = './numberofFlow/output'

input_base = './numberofPkt/input'
output_base = './numberofPkt/output'

dir_list = [input_base]

cnt = 0

while dir_list:
    cur_dir = dir_list.pop(0)
    cur_list = os.listdir(cur_dir)
    for cur in cur_list:
        path = cur_dir + '/' + cur
        # is a pcap file, run pcapParser
        if (os.path.isfile(path)):
            # print(cur)
            output_path = output_base + '/' + path.replace(input_base, '')[:-5] + '.csv'
            cmd = f'./pcapParser {path} {output_path}'
            # print(cmd)

            # print(output_path.split('/'))
            out_dir = ''
            for tmp in output_path.split('/')[:-1]:
                out_dir = out_dir + tmp + '/'
            # print(out_dir)
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
        
            os.system(cmd)
            print(cmd)
            cnt += 1
        # isdirectory, push to list
        else:
            dir_list.append(path)

print(f'files count: {cnt}')