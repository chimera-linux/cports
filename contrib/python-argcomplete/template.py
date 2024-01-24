pkgname = "python-argcomplete"
pkgver = "3.2.2"
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
sha256 = "85f4bccc5af94fd9fb5f6e8a51e24119d05af8a428721699cf84cd27db03e29d"
# missing pexpect
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"
