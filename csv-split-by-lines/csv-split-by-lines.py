# #!/usr/bin/env python3

# def main():
#     chunk_size = 2000  # lines

#     def write_chunk(part, lines):
#         with open('/Users/romansozinov/MyProjects/Web-Parser-Python/examples/csv-split-by-lines/output_file_data_part_'+ str(part) +'.csv', 'w') as f_out:
#             f_out.write(header)
#             f_out.writelines(lines)

#     with open('/Users/romansozinov/MyProjects/Web-Parser-Python/examples/csv-split-by-lines/input_file.csv', 'r') as f:
#         count = 0
#         header = f.readline()
#         lines = []
#         for line in f:
#             count += 1
#             lines.append(line)
#             if count % chunk_size == 0:
#                 write_chunk(count // chunk_size, lines)
#                 lines = []
#         # write remainder
#         if len(lines) > 0:
#             write_chunk((count // chunk_size) + 1, lines)

# if __name__ == '__main__':
#     main()
    
    
    
    
csvfile = open('/Users/romansozinov/MyProjects/Web-Parser-Python/examples/csv-split-by-lines/input_file.csv', 'r').readlines()

filename = 1
for i in range(len(csvfile)):
    if i % 2000 == 0:
        open('/Users/romansozinov/MyProjects/Web-Parser-Python/examples/csv-split-by-lines/output_file_data_part_' + str(filename) + '.csv', 'w+').writelines(csvfile[i:i+2000])
        filename += 1    