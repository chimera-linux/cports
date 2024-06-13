pkgname = "python-impacket"
pkgver = "0.11.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["-k", "not remote"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-charset-normalizer",
    "python-flask",
    "python-ldapdomaindump",
    "python-openssl",
    "python-pyasn1_modules",
    "python-pycryptodomex",
    "python-six",
]
checkdepends = ["python-pytest"] + depends
pkgdesc = "Collection of Python classes for working with network protocols"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "Apache-2.0"
url = "https://github.com/fortra/impacket"
source = f"$(PYPI_SITE)/i/impacket/impacket-{pkgver}.tar.gz"
sha256 = "ee4039b4d2aede8f5f64478bc59faac86036796be24dea8dc18f009fb0905e4a"
