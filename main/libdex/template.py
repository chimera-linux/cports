pkgname = "libdex"
pkgver = "0.10.1"
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
license = "LGPL-2.1-or-later AND BSD-3-Clause"
url = "https://gitlab.gnome.org/GNOME/libdex"
source = f"$(GNOME_SITE)/libdex/{'.'.join(pkgver.rsplit('.')[:-1])}/libdex-{pkgver}.tar.xz"
sha256 = "7472e88090db2b228307505edeba4483e872681340cb0404ae64ac3da5bed0a6"
# for liburing
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE"],
}
# gobject-introspection
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libdex-devel")
def _(self):
    return self.default_devel()
