pkgname = "egl-gbm"
pkgver = "1.1.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["cmake", "meson", "pkgconf"]
makedepends = [
    "eglexternalplatform",
    "libdrm-devel",
    "libgbm-devel",
    "libglvnd-devel",
]
pkgdesc = "GBM EGL external platform library"
maintainer = "mizz1e <158266562+mizz1e@users.noreply.github.com>"
license = "MIT"
url = "https://github.com/NVIDIA/egl-gbm"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "40c8a1a3df0639ea83031a92e9adcbef92ed696445307aa23cfc5895e63d11f0"


def post_install(self):
    self.install_license("COPYING")
