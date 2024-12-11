pkgname = "cjs"
pkgver = "6.4.0"
pkgrel = 0
build_style = "meson"
# Profiler does not build on musl libc, see https://bugs.gentoo.org/937390
configure_args = [
    "--libexecdir=/usr/lib",  # XXX: drop libexec
    "-Dinstalled_tests=true",
    "-Dprofiler=disabled",
    "-Dskip_gtk_tests=true",
]
hostmakedepends = [
    "dbus",
    "gobject-introspection",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "gtk4-devel",
    "libffi-devel",
    "mozjs128-devel",
    "readline-devel",
]
pkgdesc = "Cinnamon JavaScript interpreter"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "MIT OR LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cjs/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "55d730fdb331a9778a0d569e45c968ac68c8f218876e5d2d475cb5af21b6935a"
patch_style = "patch"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("cjs-devel")
def _(self):
    return self.default_devel()


@subpackage("cjs-tests-static")
def _(self):
    self.subdesc = "installed tests"

    return ["usr/lib/installed-tests/cjs/*.a"]


@subpackage("cjs-tests")
def _(self):
    self.subdesc = "installed tests"

    return ["usr/lib/installed-tests", "usr/share/installed-tests"]
