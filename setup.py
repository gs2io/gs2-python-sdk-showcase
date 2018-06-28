import os

from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='gs2-python-sdk-showcase',
    version='1.1.8',
    package_dir={'': 'src'},
    packages=[
        "",
        "gs2_showcase_client",
        "gs2_showcase_client.control",
        "gs2_showcase_client.model",
    ],
    license='Apache License 2.0',
    description='GS2-Showcase SDK for Python.',
    url='https://gs2.io/',
    author='Game Server Services Co., LTD',
    author_email='admin@gs2.io',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)