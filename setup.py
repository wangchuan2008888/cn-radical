from setuptools import setup
import cnradical

LICENSE = cnradical.__license__
setup(
    name='cnradical',
    description='tools for get chinese radical and pinyin',
    license=LICENSE,
    install_requires=["six"]
)
