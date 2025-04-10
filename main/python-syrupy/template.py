pkgname = "python-syrupy"
pkgver = "4.9.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python-pytest"]
checkdepends = [*depends]
pkgdesc = "Pytest snapshot plugin"
license = "Apache-2.0"
url = "https://syrupy-project.github.io/syrupy"
source = f"$(PYPI_SITE)/s/syrupy/syrupy-{pkgver}.tar.gz"
sha256 = "b7d0fcadad80a7d2f6c4c71917918e8ebe2483e8c703dfc8d49cdbb01081f9a4"
# unpackaged dependencies
options = ["!check"]
