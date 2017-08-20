import os
import json
import color
import readme

class Init():
   def __init__(self):
      self.WORKSPACE_DIR=".whitefly"
      self.validTypes = ["oracle","mongo","cassandra"]

   def generateReadMe(self, type):
      return readme.CONTENT

   def generateConfig(self, type):
      return json.dumps({"type": type})

   def validateType(self, type):
      if not type in self.validTypes:
         msg = color.RED + color.BOLD + type + color.END + " is not a valid type.\n"
         msg = msg + "\nValid types are:"
         for validType in validTypes:
            msg = msg + "\n\t* " + color.BOLD + validType + color.END
         raise Exception(msg)

   def createWhiteflyDir(self, whiteflyDir):
      os.mkdir(whiteflyDir)
      os.mkdir(os.path.join(whiteflyDir, self.WORKSPACE_DIR))

   def createGitignoreFile(self, whiteflyDir):
      fo = open(os.path.join(whiteflyDir, ".gitignore"), "w")
      fo.write(self.WORKSPACE_DIR)
      fo.close()

   def createConfigFile(self, whiteflyDir, type):
      fo = open(os.path.join(whiteflyDir, ".whiteflyconfig"), "w")
      fo.write(self.generateConfig(type))
      fo.close()

   def createReadMeFile(self, whiteflyDir, type):
      fo = open(os.path.join(whiteflyDir, "README.md"), "w")
      fo.write(self.generateReadMe(type))
      fo.close()

   def createUpdateFile(self, whiteflyDir, type):
      fo = open(os.path.join(whiteflyDir, "update.sql"), "w")
      fo.close()

   def createRollbackFile(self, whiteflyDir, type):
      fo = open(os.path.join(whiteflyDir, "rollback.sql"), "w")
      fo.close()

   def help(self):
      print("usage: whitefly init [db-type] [db-name]")

   def init(self, args):
      try:
         type = args[0].lower()
         name = args[1].lower()
         self.validateType(type)
         whiteflyDir = os.path.join(os.getcwd(), name)
         self.createWhiteflyDir(whiteflyDir)
         self.createGitignoreFile(whiteflyDir)
         self.createConfigFile(whiteflyDir, type)
         self.createReadMeFile(whiteflyDir, type)
         self.createUpdateFile(whiteflyDir, type)
         self.createRollbackFile(whiteflyDir, type)
         print("Initialized empty whitefly workspace in " + whiteflyDir)
      except OSError, e:
         if e.errno == os.errno.EEXIST:
            print 'ERROR - Workspace is already created.'
         else:
            print e
         raise e
         
