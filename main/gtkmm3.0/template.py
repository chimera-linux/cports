pkgname = "gtkmm3.0"
pkgver = "3.24.11"
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
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = (
    f"$(GNOME_SITE)/gtkmm/{pkgver[: pkgver.rfind('.')]}/gtkmm-{pkgver}.tar.xz"
)
sha256 = "19e383c82d5dd89db275e00b82864e90414d4c3fb3d100b2f996bcc2338a4cc7"


@subpackage("gtkmm3.0-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/gtkmm-3.0",
        ]
    )
