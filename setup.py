from setuptools import find_packages, setup

with open("requirements.txt", encoding="utf-8") as f:
    reqs = [
        line.strip()
        for line in f.read().splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]

setup(
    name="melotts",
    version="0.2.1",
    description="MeloTTS inference library",
    python_requires=">=3.12",
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
    package_data={
        "": ["*.txt", "*.json"],
    },
)
