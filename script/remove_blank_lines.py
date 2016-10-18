import sys

def isGabbage(line):
  if (len(line)==1 and line[0]=='\n'):
    return True
  return line.rstrip('\n').isdigit()

def isNotPara(line):
  c = line.lstrip()[0]
  return c.islower() or c in "ŭĉĝĥĵŝ"

if len(sys.argv) < 2:
  print("Help: python3 remove_blank_lines.py path_to_the_file\n")

path = sys.argv[1]
file = open(path)
lines = file.readlines()
file.close()

# remove gabbages
lines = [line for line in lines if not isGabbage(line)]

# remove blank lines
ret = ""
for i in range(len(lines)):
  if i+1 < len(lines) and isNotPara(lines[i+1]):
    ret = ret + lines[i].rstrip("\n") + " "
  else:
    ret = ret + lines[i] + "\n"

print(ret)

file = open(path, 'w')
file.write(ret)
file.close()
