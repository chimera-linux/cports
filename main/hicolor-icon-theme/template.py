pkgname = "hicolor-icon-theme"
pkgver = "0.18"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Default fallback theme for freedesktop.org icon themes"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/icon-theme"
source = f"http://icon-theme.freedesktop.org/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "db0e50a80aa3bf64bb45cbca5cf9f75efd9348cf2ac690b907435238c3cf81d7"


@subpackage("hicolor-icon-theme-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
