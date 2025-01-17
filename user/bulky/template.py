pkgname = "bulky"
pkgver = "3.6"
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
sha256 = "f98e412cf5f15839ee2d143c0bf733982a5cd12725cfffb94c1f66bb46a00874"
# Test script requires write access to the cbuild container's root
options = ["!check"]


def install(self):
    self.install_files("usr", "")
    with open(self.destdir / "usr/share/bulky/version", "w") as verfile:
        verfile.write(self.pkgver)
