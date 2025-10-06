pkgname = "nautilus-open-any-terminal"
pkgver = "0.6.3"
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
sha256 = "bd41e5b66a4a2df13037afb7a5dfb44e2cbdba11d519ab13e1caa4ac7e7976ea"
# no tests
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"
