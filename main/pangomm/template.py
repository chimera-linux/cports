pkgname = "pangomm"
pkgver = "2.56.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["pango-devel", "glibmm-devel", "cairomm-devel"]
pkgdesc = "C++ bindings for Pango"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/pangomm/{pkgver[:-2]}/pangomm-{pkgver}.tar.xz"
sha256 = "539f5aa60e9bdc6b955bb448e2a62cc14562744df690258040fbb74bf885755d"


@subpackage("pangomm-devel")
def _(self):
    return self.default_devel(extra=["usr/lib/pangomm-2.48"])
