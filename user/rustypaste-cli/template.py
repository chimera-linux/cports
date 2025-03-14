pkgname = "rustypaste-cli"
pkgver = "0.9.3"
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
sha256 = "4e4083cb537085a0e36bac6dd945883fc3cccd7c9a86496468687b406768967a"
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
