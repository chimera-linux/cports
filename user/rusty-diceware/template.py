pkgname = "rusty-diceware"
pkgver = "0.5.8"
pkgrel = 1
build_style = "cargo"
# we patch lockfile
prepare_after_patch = True
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Word list based passphrase generator"
license = "AGPL-3.0-only"
url = "https://gitlab.com/yuvallanger/rusty-diceware"
source = f"{url}/-/archive/diceware-v{pkgver}/rusty-diceware-diceware-v{pkgver}.tar.gz"
sha256 = "a3301f585149af8818d10972238656b9586a3fd78a6842150aec6d0ae8e4dbe8"


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


def post_install(self):
    self.install_license("LICENSE")
