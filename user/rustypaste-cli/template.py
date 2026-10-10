pkgname = "rustypaste-cli"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=use-native-certs",
]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CLI client for rustypaste"
license = "MIT"
url = "https://github.com/orhun/rustypaste-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cfa4fa94d950c59eb0474e2387e0171d77fba3abfbecef4ffbf520dbb897de44"
# no tests defined
options = ["!check"]


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


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "rpaste"))
    self.install_license("LICENSE")
    self.install_man("man/rpaste.1")
