pkgname = "wayland"
pkgver = "1.22.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Ddocumentation=false"]
hostmakedepends = ["meson", "pkgconf", "flex"]
makedepends = [
    "libexpat-devel",
    "libffi-devel",
    "libfl-devel-static",
    "libxml2-devel",
]
pkgdesc = "Wayland compositor infrastructure"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland/-/releases/{pkgver}/downloads/{pkgname}-{pkgver}.tar.xz"
sha256 = "1540af1ea698a471c2d8e9d288332c7e0fd360c8f1d12936ebb7e7cbc2425842"

if self.profile().cross:
    hostmakedepends += ["wayland-progs"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("wayland-progs")
def _progs(self):
    return self.default_progs(
        extra=[
            "usr/share/aclocal/wayland-scanner.m4",
            "usr/share/wayland/wayland-scanner.mk",
            "usr/lib/pkgconfig/wayland-scanner.pc",
        ]
    )


@subpackage("wayland-devel")
def _devel(self):
    self.depends += [f"wayland-progs={pkgver}-r{pkgrel}", "libffi-devel"]
    return self.default_devel(extra=["usr/share/wayland"])
