import sys
import release

def version():
	print("whitefly version " + release.__version__ + " (" + release.__code__ + ")")

def help():
	print("usage: whitefly [--version] <command> [<args?]")

def main():
	if len(sys.argv) == 1:
		help()
	elif sys.argv[1] == "--version" or args == "-v":
		version()
	else:
		help() 