pkgname = "pangomm1.4"
pkgver = "2.46.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["pango-devel", "glibmm2.4-devel", "cairomm1.0-devel"]
pkgdesc = "C++ bindings for Pango (2.46)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/pangomm/{pkgver[:-2]}/pangomm-{pkgver}.tar.xz"
sha256 = "b92016661526424de4b9377f1512f59781f41fb16c9c0267d6133ba1cd68db22"


@subpackage("pangomm1.4-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/pangomm-1.4",
        ]
    )
