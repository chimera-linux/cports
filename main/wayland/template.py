pkgname = "wayland"
pkgver = "1.23.0"
pkgrel = 0
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
sha256 = "05b3e1574d3e67626b5974f862f36b5b427c7ceeb965cb36a4e6c2d342e45ab2"

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
