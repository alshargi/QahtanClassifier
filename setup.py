

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='QahtanClassifier',
    version='0.0.4',
    author='Faisal Alshargi',
    author_email='alshargi@hotmail.de',
    description='Arabic classifier',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/alshargi/QahtanClassifier.git',
    project_urls = {
        "Bug Tracker": "https://github.com/alshargi/QahtanClassifier.git/issues"
    },
    license='MIT',
    packages=['QahtanClassifier'],
    package_data={'QahtanClassifier': ['models/*.sav']}, 
    install_requires=['requests'],
)
