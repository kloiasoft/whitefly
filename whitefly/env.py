import json
import line_builder

class Env():
   NAME = "NAME" 
   CONNECTION_STRING = "CONNECTION STRING"
   USERNAME = "USERNAME"
   PASSWORD = "PASSWORD"
   def generateConfigFile(self, type):
      return json.dumps({"type": type})

   def list(self):
      LineBuilder = line_builder.LineBuilder()
      fo = open(".whiteflyconfig", "r")
      conf_content = fo.read()
      conf = json.loads(conf_content)
      (LineBuilder.append_short(self.NAME)
         .append_long(self.CONNECTION_STRING)
         .append_short(self.USERNAME)
         .append_short(self.PASSWORD)
         .println())
      for env in conf["environments"]:
         (LineBuilder.append_short(env.get("name"))
            .append_long(env.get("connection-string"))
            .append_short(env.get("username"))
            .append_short(env.get("password"))
            .println())

         print(name + self.TAB + connectionstring + self.TAB + username + self.TAB + password)

   def help(self):
      print("""usage: whitefly env list
       whitefly env add <name> <connection-string>
       whitefly env update <name> <connection-string>
       whitefly env remove <name>""")

   def env(self, args):
      try:
         if(len(args) == 0):
            self.list()
      except e:
         raise e
