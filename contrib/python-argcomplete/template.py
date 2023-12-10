pkgname = "python-argcomplete"
pkgver = "3.2.1"
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
sha256 = "9d840bb9ffbc44fc9ca9dd2c94d771a19989571653676e60b89ba832c3c12476"
# missing pexpect
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"
