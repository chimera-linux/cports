pkgname = "comrak"
pkgver = "0.23.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["oniguruma-devel"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "BSD-2-Clause"
url = "https://hrzn.ee/kivikakk/comrak"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "2090b91c8366f50071694823063f1944964def187c0c1ad6ea06a306b1db972a"


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("COPYING")
