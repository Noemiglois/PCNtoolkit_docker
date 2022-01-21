from setuptools import setup, find_packages

REQUIRED_PACKAGES=['argparse', 'nibabel==3.2.1', 'six', 'sklearn==0.0', 'bspline==0.1.1',
      'matplotlib==3.4.2', 'pandas==1.2.4', 'torch==1.9.0',  'pymc3==3.8', 
      'Theano==1.0.5', 'arviz==0.11.0', 'brotlipy==0.7.0', 'cached-property==1.5.2',
      'certifi==2020.6.20', 'cftime==1.5.0', 'cycler==0.10.0', 'h5py==3.2.1', 
      'joblib==1.0.1', 'kiwisolver==1.3.1', 'netCDF4==1.5.6', 'numpy==1.20.3', 
      'patsy==0.5.1', 'Pillow==8.2.0', 'pycosat==0.6.3', 'pymc3==3.8', 'pyparsing==2.4.7',
      'python-dateutil==2.8.1', 'pytz==2021.1', 'ruamel-yaml==0.15.87', 'scikit-learn==0.24.2',
      'scipy==1.6.3', 'threadpoolctl==2.1.0', 'typing-extensions==3.10.0.0', 'xarray==0.18.2']

setup(name='pcntoolkit',
      version='0.21',
      description='Predictive Clinical Neuroscience toolkit',
      url='http://github.com/amarquand/nispat',
      author='Andre Marquand',
      author_email='a.marquand@donders.ru.nl',
      license='GNU GPLv3',
      packages=find_packages(),
      install_requires=REQUIRED_PACKAGES,
      zip_safe=False)

