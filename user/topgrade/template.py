pkgname = "topgrade"
pkgver = "16.0.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Multiple package-manager system updater"
license = "GPL-3.0-or-later"
url = "https://github.com/topgrade-rs/topgrade"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "62cfb4eacfe96ba74d510159812fb87076a31c595efd43eb44cb610ca11f5c9d"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(f"{self.cwd}/topgrade.{shell}", "w") as o:
            self.do(
                f"target/{self.profile().triplet}/release/topgrade",
                "--gen-completion",
                shell,
                stdout=o,
            )
    with open(f"{self.cwd}/topgrade.8", "w") as o:
        self.do(
            f"target/{self.profile().triplet}/release/topgrade",
            "--gen-manpage",
            stdout=o,
        )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/topgrade")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"topgrade.{shell}", shell)
    self.install_man("topgrade.8")
    self.install_file(
        "config.example.toml", "usr/share/examples/topgrade/config.toml"
    )
