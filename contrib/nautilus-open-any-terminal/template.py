pkgname = "nautilus-open-any-terminal"
pkgver = "0.5.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gettext",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "nautilus-python",
    "python-gobject",
]
pkgdesc = "Open a terminal from inside nautilus"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-only"
url = "https://github.com/Stunkymonkey/nautilus-open-any-terminal"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1f66f7588c22486100e72e1efff96d7b2977ae05a05b14674417a143666c6a62"
# no tests
options = ["!check"]
