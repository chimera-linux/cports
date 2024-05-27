pkgname = "libdex"
pkgver = "0.6.0"
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
sha256 = "1e88d2b00628e586b723b7fba515cce9752faf12122cde5a3c0d5b883998522a"
# for liburing
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# gobject-introspection
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libdex-devel")
def _devel(self):
    return self.default_devel()
