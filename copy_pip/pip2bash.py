import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--Except', default=None,
                    help='except package name')
parser.add_argument('-o', '--output', default="pip_install.sh",
                    help='output file name')

args = parser.parse_args()

if args.Except is not None:
    with open(args.Except, "r") as f:
        except_package = [line.replace("\n", "").replace(" ", "") for line in f.readlines()]
else:
    except_package = []

pip_list = subprocess.Popen("pip list", 
                 stdout=subprocess.PIPE, 
                 shell=True).communicate()[0]
pip_list = pip_list.decode("utf-8").split("\n")

with open(args.output, "w") as fw:
    for line in pip_list[2:]:
        line = line.split()
        if len(line) != 2:
            continue
        package, version = line
        if package in except_package:
            continue
        fw.write("pip install "+package+"=="+version+"\n")
