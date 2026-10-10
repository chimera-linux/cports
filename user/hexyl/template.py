pkgname = "hexyl"
pkgver = "0.17.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
pkgdesc = "Color-coded hex viewer CLI"
license = "Apache-2.0 OR MIT"
url = "https://github.com/sharkdp/hexyl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "72fa17397ad187eec6b295d02c7caabbb209a6e0d5706187b8a599bd5df8615e"


def post_build(self):
    from cbuild.util import cargo

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"hexyl.{shell}", "w") as f:
            self.do(
                cargo.target_path(self, "hexyl"),
                "--completion",
                shell,
                stdout=f,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"hexyl.{shell}", shell)
    self.install_license("LICENSE-MIT")
