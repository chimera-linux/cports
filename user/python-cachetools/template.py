pkgname = "python-cachetools"
pkgver = "7.1.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
]
checkdepends = ["python-pytest"]
pkgdesc = "Extensible memoizing collections and decorators"
license = "MIT"
url = "https://github.com/tkem/cachetools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9e7593c977cc71dc0a9bfcabce97c03ef8fdef970244f0367331920b3af931f2"


def post_install(self):
    self.install_license("LICENSE")
