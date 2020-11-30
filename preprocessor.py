import sys
import re
import os


if len(sys.argv) != 3:
    sys.stderr.write("Invalid amount of arguments\n");
    sys.stderr.write(f"Usage: {__name__}" + r"{inputfile} {outputfile}" + "\n");
    sys.exit()

inp_fl = sys.argv[1]
out_fl = sys.argv[2]

start_index = 0
end_index = 0

lines = []

if os.path.exists(inp_fl):
    with open(inp_fl, "r") as f:
        lines = f.read().split("\n")

        for line in lines:
            if re.findall("^start", line) != []:
                break;
            else:
                start_index += 1
        start_index += 1

        for line in lines[start_index:]:
            if re.findall("^end", line) != []:
                break;
            else:
                end_index += 1;


with open(out_fl, "w") as f:
    f.write("\n".join(lines[start_index:start_index + end_index]))
