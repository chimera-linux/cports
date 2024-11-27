pkgname = "nautilus-open-any-terminal"
pkgver = "0.6.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://github.com/Stunkymonkey/nautilus-open-any-terminal"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "96a1cf9ebd24b3a0b33c70c37f6ab39b11e6d11dc374c9199e54a0b1f19e163a"
# no tests
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"
