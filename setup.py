import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openaccess_cma", # Replace with your own username
    version="0.0.1",
    author="Cleveland Museum of Art",
    author_email="openaccess@clevelandart.org",
    description="A wrapper function for using the Cleveland Museum of Art's open access API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ClevelandMuseumArt/openaccess_cma_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
