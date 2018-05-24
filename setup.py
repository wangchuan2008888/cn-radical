from setuptools import setup
# import cnradical

LICENSE = "License :: OSI Approved :: Apache Software License"
VERSION = "0.0.2"
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
                 "License :: OSI Approved :: Apache Software License",
                 'Natural Language :: Chinese (Simplified)',
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 ]
)
