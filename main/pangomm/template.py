pkgname = "pangomm"
pkgver = "2.54.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["pango-devel", "glibmm-devel", "cairomm-devel"]
pkgdesc = "C++ bindings for Pango"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/pangomm/{pkgver[:-2]}/pangomm-{pkgver}.tar.xz"
sha256 = "4a5b1fd1b7c47a1af45277ea82b5abeaca8e08fb10a27daa6394cf88d74e7acf"


@subpackage("pangomm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/pangomm-2.48",
        ]
    )
