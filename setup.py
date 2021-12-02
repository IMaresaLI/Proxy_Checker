import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proxyCheck_mp",
    version="0.1.1",
    author="Batuhan Olgac",
    author_email="mares4l@hotmail.com",
    description="You can check the availability of the proxy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/IMaresaLI/Proxy_Checker",
    project_urls={
        "Bug Tracker": "https://github.com/IMaresaLI/Proxy_Checker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires = ["requests","requests[socks]","syscolors"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
)