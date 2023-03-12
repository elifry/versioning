import setuptools

setuptools.setup(
    name="elifry_versioning",
    version='0.0.1',
    author="Eli Fry",
    description="Format version numbers, build strings for various uses, classes for versioning schemes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
