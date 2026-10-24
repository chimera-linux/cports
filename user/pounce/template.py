pkgname = "pounce"
pkgver = "3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-notify"]
configure_gen = []
make_dir = "."
make_build_target = "all"
hostmakedepends = ["autoconf", "pkgconf"]
makedepends = ["libretls-devel"]
pkgdesc = "TLS-only multi-client IRC bouncer"
license = "GPL-3.0-or-later"
url = "https://git.causal.agency/pounce"
source = f"{url}/snapshot/pounce-{pkgver}.tar.gz"
sha256 = "5aeebf6dd73a61dbd44b94d417f0e4e5cd30c90561ba5550ac6ea61bab391ac4"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("QUIRKS.7", name="pounce-quirks")
    self.install_man("README.7", name="pounce-readme")
