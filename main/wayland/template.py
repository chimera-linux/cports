pkgname = "wayland"
pkgver = "1.26.0"
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
sha256 = "5d92753c046c6dbd528a6f47edbab599a017d415aed8088875d8c36f39189b60"

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
