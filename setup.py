from setuptools import setup, find_packages

setup(
    name="Ollivanders Shop API Rest",
    version="1.0",
    author="ncocana",
    url="https://github.com/ncocana/ollivanders-shop-api-rest",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "certifi==2022.12.7",
        "charset-normalizer==3.1.0",
        "click==8.1.3",
        "colorama==0.4.6",
        "flask==2.2.3",
        "idna==3.4",
        "itsdangerous==2.1.2",
        "jinja2==3.1.2",
        "markupsafe==2.1.2",
        "requests==2.28.2",
        "urllib3==1.26.15",
        "werkzeug==2.2.3",
    ],
)
