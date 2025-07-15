pkgname = "wlrctl"
pkgver = "0.2.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["wlroots0.19-devel"]
pkgdesc = "CLI utility for managing wlroots compositors"
license = "MIT"
url = "https://git.sr.ht/~brocellous/wlrctl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b5b3836091c41de09a832df1e5eb4747841d7ae670367e413487d5be7a5f2849"


def post_install(self):
    self.install_license("LICENSE")
