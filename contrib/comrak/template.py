pkgname = "comrak"
pkgver = "0.22.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["oniguruma-devel"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "BSD-2-Clause"
url = "https://hrzn.ee/kivikakk/comrak"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "532d855e8101e064c8dd26e74718f4520e400e9619bb2db129dc7c174bd59df6"


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("COPYING")
