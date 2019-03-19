from setuptools import setup, find_packages


setup(name='apimapper',
      version='0.2',
      description='API Mapper',
      long_description='Maps API responses to desrired schema',
      long_description_content_type='text/x-rst',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Information Analysis',
      ],
      keywords='API Mapper',
      url='https://github.com/gythaogg/apiwrapper',
      author='Gytha Ogg, Ksenia Zaytseva',
      author_email='gythaoggscat@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)
