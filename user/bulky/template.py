pkgname = "bulky"
pkgver = "3.5"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["gettext"]
depends = [
    "base-files-doc",
    "gtk+3",
    "python-gobject",
    "python-magic",
    "python-setproctitle",
]
pkgdesc = "Bulk renamer"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/bulky/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "84d449535553f5f1857812d88c70252730473c8f85760e80be1381d53290028c"
# Test script requires write access to the cbuild container's root
options = ["!check"]


def install(self):
    self.install_files("usr", "")
    with open(self.destdir / "usr/share/bulky/version", "w") as verfile:
        verfile.write(self.pkgver)
