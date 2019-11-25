import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rede edi",
    version="0.0.4",
    author="Marcio Correa",
    author_email="marcioinfo.correa@gmail.com",
    description="A package to handle rede EDI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darleisantossoares/rede_edi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
