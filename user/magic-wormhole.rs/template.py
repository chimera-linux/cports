pkgname = "magic-wormhole.rs"
pkgver = "0.7.4"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Magic Wormhole CLI client"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "EUPL-1.2"
url = "https://github.com/magic-wormhole/magic-wormhole.rs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3ddc40c82faa381e96ffdc54757625a4707c1bd111d67ab2ec733a5bb666a43c"
# generates completions with host bin
options = ["!check", "!cross"]


def post_extract(self):
    self.rm(".cargo/config")


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
