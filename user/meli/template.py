pkgname = "meli"
pkgver = "0.8.13"
pkgrel = 0
build_wrksrc = "meli"
build_style = "cargo"
configure_args = ["--bin meli"]
hostmakedepends = ["cargo-auditable", "pkgconf", "mandoc"]
makedepends = ["openssl3-devel", "sqlite-devel"]
depends = ["gpgme-devel", "notmuch-devel"]
pkgdesc = "Terminal e-mail client"
license = "EUPL-1.2 OR GPL-3.0-or-later"
url = "https://meli-email.org"
source = f"https://git.meli-email.org/meli/meli/archive/v{pkgver}.tar.gz"
sha256 = "b1414defb7973a96ed0510b5cb888aa8671fe4f3f832c5baa0c79dcd61ba2edf"

def post_install(self):
    self.install_man("docs/meli.1")
    self.install_man("docs/meli.7")
    self.install_man("docs/meli.conf.5")
    self.install_man("docs/meli.conf.examples.5")
    self.install_man("docs/meli-themes.5")

    self.install_license("../COPYING")
