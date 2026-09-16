pkgname = "magic-wormhole.rs"
pkgver = "0.8.1"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Magic Wormhole CLI client"
license = "EUPL-1.2"
url = "https://github.com/magic-wormhole/magic-wormhole.rs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "90e8b1d7270a4c251f78376e10948c994df1a559152eca7eedd4aecbf70b70d9"
# generates completions with host bin
options = ["!check", "!cross"]


def post_build(self):
    from cbuild.util import cargo

    for shell in ["bash", "fish", "zsh"]:
        with open(f"{self.cwd}/wormhole-rs.{shell}", "w") as o:
            self.do(
                cargo.target_path(self, "wormhole-rs"),
                "completion",
                shell,
                stdout=o,
            )


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "wormhole-rs"))
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"wormhole-rs.{shell}", shell, "wormhole-rs")
    self.install_man("wormhole.1", name="wormhole-rs")
    self.install_license("LICENSE")
