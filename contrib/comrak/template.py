pkgname = "comrak"
pkgver = "0.21.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["oniguruma-devel"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "BSD-2-Clause"
url = "https://hrzn.ee/kivikakk/comrak"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "4d490100259d45331724a132cebff90bbc6c4729397a10465e8a7216673e1a8e"


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("COPYING")
