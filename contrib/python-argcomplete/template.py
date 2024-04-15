pkgname = "python-argcomplete"
pkgver = "3.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
    "python-wheel",
]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Python tab completion plugin"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/kislyuk/argcomplete"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "84631dde4cda5814836ea875625b78518669ce769a09a0ad865f1437b8e88ad3"
# missing pexpect
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"
