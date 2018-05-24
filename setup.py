from setuptools import setup
import cnradical

LICENSE = cnradical.__license__
VERSION = cnradical.__version__
setup(
    name='cnradical',
    version=VERSION,
    description='tools for get chinese radical and pinyin',
    license=LICENSE,
    install_requires=["six"],
    classifiers=['Topic :: Text Processing :: Linguistic',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Development Status :: 5 - Production/Stable',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'License :: OSI Approved :: Apache License Version 2.0',
                 'Natural Language :: Chinese (Simplified)',
                 ]
)
