pkgname = "nicotine-plus"
pkgver = "3.2.9"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "test/unit"
hostmakedepends = [
    "gettext",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = [
    "python-pytest",
    "python-semidbm",
]
depends = [
    "gtk+3",
    "python-gobject",
    "python-semidbm",
]
pkgdesc = "Graphical client for the Soulseek network"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://nicotine-plus.github.io/nicotine-plus"
source = (
    f"https://github.com/Nicotine-Plus/nicotine-plus/archive/{pkgver}.tar.gz"
)
sha256 = "aeaf45742a915345d1635f36ca334c3f332788c7a27262408be9998985f99e41"
