from setuptools import setup

setup(
    name="followups",
    version="0.0.1",
    description="Followups",
    py_modules=["main"],
    package_dir={'':'src'},
    install_requires=[
        "redis >= 4.3.4",
        "fastapi >= 0.78.0",
        "uvicorn >= 0.18.2",
        "neo4j >= 4.4.5"
    ],
)
