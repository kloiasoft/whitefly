class LineBuilder():
   def __init__(self):
      self.LINE = ""
   def append_short(self, text):
      return self.append(16, text)

   def append_long(self, text):
      return self.append(48, text)

   def append(self, length, text):
      self.LINE = self.LINE + ("{:<" + str(length) + "}").format(text) + "\t"
      return self

   def printf(self):
      printf(self.LINE)

   def println(self):
      print(self.LINE)
      self.reset()

   def reset(self):
      self.LINE = ""
