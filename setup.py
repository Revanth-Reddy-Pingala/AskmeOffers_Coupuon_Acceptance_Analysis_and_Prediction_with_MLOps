import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "1.0.0"

REPO_NAME = "AskmeOffers_Coupuon_Acceptance_Analysis_and_Prediction_with_MLOps(Mlflow)"
AUTHOR_USER_NAME = "Revanth Reddy Pingala"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "pingalarevanthreddy144@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)