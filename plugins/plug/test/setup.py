from setuptools import setup, find_packages

setup(
    name="test",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["quantcrafter"],
    entry_points={
        "quantcrafter": [
            "test_advisor = test:register_advisors"
        ]
    },
)
