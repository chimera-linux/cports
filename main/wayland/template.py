pkgname = "wayland"
pkgver = "1.24.0"
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
license = "MIT"
url = "https://wayland.freedesktop.org"
source = (
    f"https://gitlab.freedesktop.org/wayland/wayland/-/archive/{pkgver}.tar.gz"
)
sha256 = "82eab21b355ba2b0b5c2b7e6bfa7335ef9eaf52e874d4e4884e5ba18423b0d3b"

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
