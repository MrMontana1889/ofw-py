from setuptools import setup

with open('DESCRIPTION.txt') as file:
    long_description = file.read()

REQUIREMENTS = ['pythonnet']

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Water Distribution',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.9'
]

setup(
    name="OpenFlowsAPI-Water-Stubs-Bentley",
    version='0.0.4',
    description="Python stubs for OpenFlowsAPI for Water (a.k.a. WaterObjectsLite)",
    long_description=long_description,
    url="https://github.com/MrMontana1889/OpenFlowsAPI-water-stubs",
    author="Kristopher L. Culin",
    license="MIT",
    # packages=['OpenFlows'],
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    keywords='water distribution openflows waterbojectslite'
)