pkgname = "magic-wormhole.rs"
pkgver = "0.7.1"
pkgrel = 1
build_style = "cargo"
make_build_args = ["--bins"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Magic Wormhole CLI client"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "EUPL-1.2"
url = "https://github.com/magic-wormhole/magic-wormhole.rs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c6e2acd3cccd982f449d26184d714d4cf813f51b8b75b3e36ecbb78565b3f4e8"
# generates completions with host bin
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(f"{self.cwd}/wormhole-rs.{shell}", "w") as o:
            self.do(
                f"target/{self.profile().triplet}/release/wormhole-rs",
                "completion",
                shell,
                stdout=o,
            )


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/wormhole-rs",
    )
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"wormhole-rs.{shell}", shell, "wormhole-rs")
    self.install_man("wormhole.1", name="wormhole-rs")
    self.install_license("LICENSE")
