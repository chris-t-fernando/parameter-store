from distutils.core import setup

setup(
    name="parameter_store",
    version="0.14",
    description="Interface and concretes for saving parameters for scripts",
    author="Chris Fernando",
    author_email="chris.t.fernando@gmail.com",
    url="https://github.com/chris-t-fernando/parameter-store",
    packages=["parameter_store"],
    install_requires=["boto3"],
)
