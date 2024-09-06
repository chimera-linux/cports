pkgname = "bulky"
pkgver = "3.4"
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
sha256 = "dd3350ccb98ce1b1f3df67151ca091430df67e41f19162a415550ef8ebd67c45"
# Test script requires write access to the cbuild container's root
options = ["!check"]


def install(self):
    self.install_files("usr", "")
    with open(self.destdir / "usr/share/bulky/version", "w") as verfile:
        verfile.write(self.pkgver)
