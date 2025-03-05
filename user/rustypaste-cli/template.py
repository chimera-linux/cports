pkgname = "rustypaste-cli"
pkgver = "0.9.2"
pkgrel = 1
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
sha256 = "747c4690631082e3cfbdf7bf4656ac9a76db4ea6bb3f067f24a982ea00f16cc2"
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
    self.install_bin(f"target/{self.profile().triplet}/release/rpaste")
    self.install_license("LICENSE")
    self.install_man("man/rpaste.1")
