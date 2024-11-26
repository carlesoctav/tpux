import setuptools

setuptools.setup(
    name="tpux",
    version="0.1",
    author="carles",
    author_email="carlesoctavianus@tuta.io",
    description="tpux",
    url="https://github.com/carlesoctav/tpux",
    packages=setuptools.find_packages(),
    install_requires=[
        "psutil",
        "fabric"
    ],
)
