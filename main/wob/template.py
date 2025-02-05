pkgname = "wob"
pkgver = "0.15.1"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "ISC"
url = "https://github.com/francma/wob"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "094f666e799a7fa0914192d041032f4e9a28a87486d024db80ade010988b218a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
