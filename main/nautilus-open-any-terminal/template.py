pkgname = "nautilus-open-any-terminal"
pkgver = "0.7.0"
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
sha256 = "352b823b8a06ca44f57f586b04a64e28daeb0249f15ab4b6526fc06c4a3d91dd"
# no tests
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"
