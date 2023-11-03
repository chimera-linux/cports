pkgname = "python-argcomplete"
pkgver = "3.1.4"
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
sha256 = "71d9152436f2eb1396c5ff84417f8b76a36a23aa6831cddda570c015716e3efb"
# missing pexpect
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"
