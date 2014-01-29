import setuptools

REQUIREMENTS = [
]

if __name__ == "__main__":
    setuptools.setup(
        name="sujmarkov",
        version="0.0.1",
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
