import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pykitables",
    version="0.0.1",
    author="Omshi Samal",
    author_email="omshisamal72@gmail.com",
    description="Get neatly formatted tables from any Wikipedia article",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omshii/pykitables",
    install_requires=['beautifulsoup4', 'requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
