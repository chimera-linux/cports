pkgname = "libdex"
pkgver = "0.7.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Db_ndebug=true",
    "-Deventfd=enabled",
    "-Dexamples=false",
    "-Dliburing=enabled",
]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "libucontext-devel",
    "liburing-devel",
    "linux-headers",
]
pkgdesc = "Future-based programming for GLib-based applications"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later AND BSD-3-Clause"
url = "https://gitlab.gnome.org/GNOME/libdex"
source = f"$(GNOME_SITE)/libdex/{'.'.join(pkgver.rsplit('.')[:-1])}/libdex-{pkgver}.tar.xz"
sha256 = "c0b13e97b340057dc4e7c53f17e5d7ecd310a1fa2abc9a729670f02261a40a9b"
# for liburing
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# gobject-introspection
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libdex-devel")
def _(self):
    return self.default_devel()
