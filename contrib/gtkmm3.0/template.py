pkgname = "gtkmm3.0"
pkgver = "3.24.9"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dbuild-demos=false", "-Dbuild-tests=true"]
make_check_wrapper = ["xwfb-run", "--"]
hostmakedepends = ["meson", "pkgconf", "glib-devel"]
makedepends = [
    "atkmm1.6-devel",
    "cairomm1.0-devel",
    "gdk-pixbuf-devel",
    "gtk+3-devel",
    "pangomm1.4-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "C++ bindings for Gtk+3"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/gtkmm/{pkgver[:-2]}/gtkmm-{pkgver}.tar.xz"
sha256 = "30d5bfe404571ce566a8e938c8bac17576420eb508f1e257837da63f14ad44ce"


@subpackage("gtkmm3.0-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/gtkmm-3.0",
        ]
    )
