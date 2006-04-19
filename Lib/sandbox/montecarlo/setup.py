import numpy
from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration
from os.path import join

def configuration(parent_package='', top_path=None):

    config = Configuration('montecarlo', parent_package, top_path)

    # This code requires 'randomkit' to have been built using 'add_extension' in
    # numpy/random/setup.py.

    config.add_extension('_intsampler',
              include_dirs = [numpy.get_numpy_include(),
                    # The following path needs to be extracted in a portable way.
                    # This points to the default installation location used by
                    # config.add_data_files().
                   '/usr/lib/python2.4/site-packages/numpy/random/'],
              libraries=['randomkit'],
              library_dirs=['/usr/lib/python2.4/site-packages/numpy/random/'],
              runtime_library_dirs=['/usr/lib/python2.4/site-packages/numpy/random/'],
              sources = [join('src', f) for f in
                        ['_intsamplermodule.c', 'compact5table.c']]
              ) 
    config.add_data_dir('tests')
    config.add_data_dir('examples')
    config.add_data_dir('doc')

    return config

if __name__ == '__main__':
    setup(**configuration(top_path='').todict())
