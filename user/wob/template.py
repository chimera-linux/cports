pkgname = "wob"
pkgver = "0.16"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dseccomp=enabled"]
hostmakedepends = ["meson", "pkgconf", "scdoc", "wayland-progs"]
makedepends = [
    "inih-devel",
    "libffi8-devel",
    "libseccomp-devel",
    "linux-headers",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Wayland Overlay Bar"
license = "ISC"
url = "https://github.com/francma/wob"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "8a5850beec72b5b19be631a6eb21315a20082bf9135447080f9e9045f143938b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")

    # TODO: dinit service?
    self.uninstall("usr/lib/systemd")
