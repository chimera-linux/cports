pkgname = "wayland"
pkgver = "1.23.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocumentation=false"]
hostmakedepends = ["meson", "pkgconf", "flex"]
makedepends = [
    "flex-devel-static",
    "libexpat-devel",
    "libffi8-devel",
    "libxml2-devel",
]
pkgdesc = "Wayland compositor infrastructure"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = (
    f"https://gitlab.freedesktop.org/wayland/wayland/-/archive/{pkgver}.tar.gz"
)
sha256 = "a7e4678a71cfdbf095673c894362accaebd0c4ba0618b5f4f6ce04acc13275b0"

if self.profile().cross:
    hostmakedepends += ["wayland-progs"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("wayland-progs")
def _(self):
    return self.default_progs(
        extra=[
            "usr/share/aclocal/wayland-scanner.m4",
            "usr/share/wayland/wayland-scanner.mk",
            "usr/lib/pkgconfig/wayland-scanner.pc",
        ]
    )


@subpackage("wayland-devel")
def _(self):
    self.depends += [self.with_pkgver("wayland-progs"), "libffi8-devel"]
    return self.default_devel(extra=["usr/share/wayland"])
