import os

file_list = os.listdir('data')

with open('output.pgn', 'w') as outfile:
  for name in file_list:
    with open('data/' + name, 'r') as f:
      for line in f:
        outfile.write(line)