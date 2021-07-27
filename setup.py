import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proxychecker_Mp",
    version="0.0.3",
    author="Batuhan Olgac",
    author_email="mares4l@hotmail.com",
    description="You can check the availability of the proxy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IMaresaLI/Proxy_Checker",
    project_urls={
        "Bug Tracker": "https://github.com/IMaresaLI/Proxy_Checker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
