pkgname = "pangomm"
pkgver = "2.50.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["pango-devel", "glibmm-devel", "cairomm-devel"]
pkgdesc = "C++ bindings for Pango"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ccc9923413e408c2bff637df663248327d72822f11e394b423e1c5652b7d9214"


@subpackage("pangomm-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/pangomm-2.48",
        ]
    )
