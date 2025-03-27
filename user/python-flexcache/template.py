pkgname = "python-flexcache"
pkgver = "0.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Cache on disk the result of expensive calculations"
license = "BSD-3-Clause"
url = "https://github.com/hgrecco/flexcache"
source = f"$(PYPI_SITE)/f/flexcache/flexcache-{pkgver}.tar.gz"
sha256 = "18743bd5a0621bfe2cf8d519e4c3bfdf57a269c15d1ced3fb4b64e0ff4600656"


def post_install(self):
    self.install_license("LICENSE")
