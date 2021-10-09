import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='calculator',
    version='0.0.1',
    author='Liucija Svinkunaite',
    author_email='liucijasvinkunaite@gmail.com',
    description='Calculator package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LiucijaSvink/calculator',
    project_urls = {
        "Bug Tracker": "https://github.com/LiucijaSvink/calculator/issues"
    },
    license='MIT',
    packages=['calculator'],
    python_requires=">=3.9",
    install_requires=['typing', 'pytest'],
)