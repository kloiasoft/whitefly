from distutils.core import setup
setup(
  name = 'whitefly',
  packages = ['whitefly'],
  version = '0.0.1',
  description = 'Making the database migrations the easiest step on continuous delivery',
  author = 'Mehmet Ali Aydin',
  author_email = 'maaydin@gmail.com',
  url = 'https://github.com/kloiasoft/whitefly',
  download_url = 'https://github.com/kloiasoft/whitefly/archive/0.0.1.tar.gz',
  keywords = ['db', 'database', 'migration'],
  classifiers = [],
  scripts=['bin/whitefly'],
)