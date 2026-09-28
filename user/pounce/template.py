pkgname = "pounce"
pkgver = "3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-notify",
    "--enable-palaver",
]
configure_gen = []
make_dir = "."
make_build_target = "all"
hostmakedepends = ["autoconf", "pkgconf"]
makedepends = ["curl-devel", "libretls-devel", "sqlite-devel"]
pkgdesc = "TLS-only multi-client IRC bouncer"
license = "GPL-3.0-or-later"
url = "https://git.causal.agency/pounce"
source = f"{url}/snapshot/pounce-{pkgver}.tar.gz"
sha256 = "97f245556b1cc940553fca18f4d7d82692e6c11a30f612415e5e391e5d96604e"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("QUIRKS.7", name="pounce-quirks")
    self.install_man("README.7", name="pounce-readme")
