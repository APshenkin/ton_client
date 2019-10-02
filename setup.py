from setuptools import setup

setup(
    author='Oleg Gaidukov',
    name='ton_client',
    version='0.5',
    packages=['ton_client'],
    test_suite='testsuite',
    install_requires=[
        "ed25519~=1.5",
        "ujson>=1.35",
        "uvloop==*",
        "mnemonic==*",
        "crc16==*"
    ],
    #setup_requires=[
    #     'flake8',
    #     'wheel',
    #     'pipenv'
    #],
    package_data={
        'ton_client': [
            'distlib/darwin/*',
            'distlib/linux/*',
        ]
    },
    zip_safe=True,
    tests_require=[    
        "pipenv>=2018.11.26",
        "flake8>=3.7.8",
        "wheel>=0.33.6"
    ],
    python_requires='>=3.6'
)
