pkgname = "geany"
pkgver = "2.0.0"
pkgrel = 2
build_style = "gnu_configure"
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "gtk+3-devel",
]
checkdepends = ["bash"]
pkgdesc = "Gtk+3 IDE"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://geany.org"
source = f"https://github.com/geany/geany/releases/download/{pkgver}/geany-{pkgver[:-2]}.tar.gz"
sha256 = "50d28a45ac9b9695e9529c73fe7ed149edb512093c119db109cea6424114847f"


@subpackage("geany-devel")
def _(self):
    return self.default_devel()
