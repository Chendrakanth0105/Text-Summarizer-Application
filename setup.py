import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Application"
AUTHOR_USER_NAME = "Chendrakanth0105"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "peddapuramkanth@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug-tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")
)