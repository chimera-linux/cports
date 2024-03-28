pkgname = "rusty-diceware"
pkgver = "0.5.8"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
pkgdesc = "Word list based passphrase generator"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "AGPL-3.0-only"
url = "https://gitlab.com/yuvallanger/rusty-diceware"
source = f"{url}/-/archive/diceware-v{pkgver}/rusty-diceware-diceware-v{pkgver}.tar.gz"
sha256 = "a3301f585149af8818d10972238656b9586a3fd78a6842150aec6d0ae8e4dbe8"


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENSE")
