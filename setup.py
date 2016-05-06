import setuptools

REQUIREMENTS = [
    "docopt>=0.6,<0.7",
    "nose>=1.3,<1.4"
]

if __name__ == "__main__":
    setuptools.setup(
        name="sujmarkov",
        version="1.0.1",
        author="Sujay Mansingh",
        author_email="sujay.mansingh@gmail.com",
        packages=setuptools.find_packages(),
        scripts=[],
        url="https://github.com/sujaymansingh/sujmarkov",
        license="LICENSE.txt",
        description="A markov generator",
        long_description="View the github page (https://github.com/sujaymansingh/sujmarkov) for more details.",
        install_requires=REQUIREMENTS
    )
