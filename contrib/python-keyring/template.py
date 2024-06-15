pkgname = "python-keyring"
pkgver = "25.2.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    # TODO: add a global keyring provider dependency
    "python-jaraco.context",
    "python-jaraco.functools",
]
checkdepends = depends + ["python-pytest"]
pkgdesc = "Store and access your passwords safely"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jaraco/keyring"
source = f"$(PYPI_SITE)/k/keyring/keyring-{pkgver}.tar.gz"
sha256 = "daaffd42dbda25ddafb1ad5fec4024e5bbcfe424597ca1ca452b299861e49f1b"


def post_install(self):
    self.install_license("LICENSE")
