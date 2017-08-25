import sys
import release
import init
import env

class CLI():
   def __init__(self):
      self.action = None
      self.args = []
      self.error = False

   def parse(self, args):
      if len(sys.argv) == 1:
         self.error = True
         self.errorDisplay = "help"
      elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
         self.action = "help"
      elif sys.argv[1] == "--version" or sys.argv[1] == "-v":
         self.action = "version"
      elif sys.argv[1] == "init":
         if len(sys.argv) == 4:
            self.action = "init"
            self.args.append(sys.argv[2])
            self.args.append(sys.argv[3])
         else:
            self.error = True
            self.action = "init_help"
      elif sys.argv[1] == "env":
         if len(sys.argv) == 2:
            self.error = True
            self.action = "env_help"
         elif sys.argv[2] == "list" and len(sys.argv) == 3 :
            self.action = "env_list"
         elif sys.argv[2] == "add" and len(sys.argv) == 5 :
            self.action = "env_add"
            self.args.append(sys.argv[3])
            self.args.append(sys.argv[4])
         elif sys.argv[2] == "update" and len(sys.argv) == 5 :
            self.action = "env_update"
            self.args.append(sys.argv[3])
            self.args.append(sys.argv[4])
         elif sys.argv[2] == "remove" and len(sys.argv) == 4 :
            self.action = "env_remove"
            self.args.append(sys.argv[3])
         else:
            self.error = True
            self.action = "env_help"
      else:
         self.error = True
         self.action = "help"

   def execute(self, args):
      self.parse(args)
      fn = getattr(self, "execute_%s" % self.action)
      fn()
      if self.error:
         sys.exit(1)

   def execute_init(self):
      try:
         Init = init.Init()
         Init.init(self.args)
      except:
         sys.exit(1)

   def execute_env_list(self):
      try:
         Env = env.Env()
         Env.env(self.args)
      except:
         sys.exit(1)

   def execute_version(self):
      print("whitefly version " + release.VERSION + " (" + release.CODENAME + ")")

   def execute_help(self):
      self.help()

   def execute_init_help(self):
      Init = init.Init()
      Init.help()

   def execute_env_help(self):
      Env = env.Env()
      Env.help()

   def help(self):
      print("usage: whitefly [--version] [--help] <command> [<args?]")
      print("")
      print("These are common Whitefly commands used in various situations:")
      print("")
      print("Start a working area:")
      print("init       Create an empty Whitefly workspace")
