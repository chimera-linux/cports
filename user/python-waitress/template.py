pkgname = "python-waitress"
pkgver = "3.0.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Waitress WSGI server"
license = "ZPL-2.1"
url = "https://github.com/Pylons/waitress"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4c5583cee40bee842b48443ed899b5d445947c5d88fe170d31c3becab09710c3"
