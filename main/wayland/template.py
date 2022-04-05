pkgname = "wayland"
pkgver = "1.20.0"
pkgrel = 0
build_style = "meson"
# "Tests must not be built with NDEBUG defined, they rely on assert()."
configure_args = ["-Ddocumentation=false", "-Db_ndebug=false"]
hostmakedepends = ["meson", "pkgconf", "flex"]
makedepends = [
    "libexpat-devel", "libffi-devel", "libfl-devel-static", "libxml2-devel"
]
pkgdesc = "Wayland compositor infrastructure"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "b8a034154c7059772e0fdbd27dbfcda6c732df29cae56a82274f6ec5d7cd8725"

if self.profile().cross:
    hostmakedepends += ["wayland-progs"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("wayland-progs")
def _progs(self):
    return self.default_progs(extra = [
        "usr/share/aclocal/wayland-scanner.m4",
        "usr/share/wayland/wayland-scanner.mk",
    ])

@subpackage("wayland-devel")
def _devel(self):
    self.depends += [
        f"wayland-progs={pkgver}-r{pkgrel}",
        "libffi-devel"
    ]
    return self.default_devel(extra = ["usr/share/wayland"])
