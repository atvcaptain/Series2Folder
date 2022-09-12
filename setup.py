from distutils.core import setup
import setup_translate

pkg = 'Extensions.Series2Folder'
setup(name='enigma2-plugin-extensions-series2folder',
       version='1.11',
       description='File series recordings into folders',
       long_description='Series2Folder can automatically, or under manual control move series recordings into folders named for the series.',
       author='prl',
       url='https://bitbucket.org/prl/series2folder/src/master/',
       package_dir={pkg: 'plugin'},
       packages=[pkg],
       package_data={pkg:
           ['locale/*/LC_MESSAGES/*.mo', 'locale/*/LC_MESSAGES/*.po']},
       cmdclass=setup_translate.cmdclass, # for translation
      )
