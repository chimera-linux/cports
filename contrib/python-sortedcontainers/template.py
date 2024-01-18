pkgname = "python-sortedcontainers"
pkgver = "2.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python library for sorting collections and containers"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "Apache-2.0"
url = "https://github.com/grantjenks/python-sortedcontainers"
source = f"https://github.com/grantjenks/python-sortedcontainers/archive/v{pkgver}.tar.gz"
sha256 = "70e22f4fd29b204f75f989e3c1e847aa1de267a028aab4233c0db783aaff78c1"
