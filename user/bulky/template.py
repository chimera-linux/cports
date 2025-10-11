pkgname = "bulky"
pkgver = "3.9"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["gettext"]
depends = [
    "base-files-doc",
    "gtk+3",
    "python-gobject",
    "python-setproctitle",
    "python-unidecode",
]
pkgdesc = "Bulk renamer"
license = "GPL-3.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/bulky/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f3edbe183be3e5e341e5cc64e9a85d87b47a83a1701902426e4ff1c22995534f"
# Test script requires write access to the cbuild container's root
options = ["!check"]


def install(self):
    self.install_files("usr", "")
    with open(self.destdir / "usr/share/bulky/version", "w") as verfile:
        verfile.write(self.pkgver)
