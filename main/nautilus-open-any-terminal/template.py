pkgname = "nautilus-open-any-terminal"
pkgver = "0.6.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gettext",
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "nautilus-python",
    "python-gobject",
]
pkgdesc = "Open a terminal from inside nautilus"
license = "GPL-3.0-only"
url = "https://github.com/Stunkymonkey/nautilus-open-any-terminal"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "30f6569bbf2e05166669467d523fae6328d15e5f7ea83e8b93af46353990f8b2"
# no tests
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"
