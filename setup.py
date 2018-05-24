import setuptools

# import cnradical

LICENSE = "License :: OSI Approved :: Apache Software License"
VERSION = "0.0.4"
setuptools.setup(
    name='cnradical',
    version=VERSION,
    author="Andrew Wang",
    author_email="wangchuan2008888@gmail.com",
    description='tools for get chinese radical and pinyin',
    license=LICENSE,
    install_requires=["six"],
    url='https://github.com/wangchuan2008888/cn-radical',
    packages=['cnradical'],
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
