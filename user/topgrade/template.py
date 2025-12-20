pkgname = "topgrade"
pkgver = "16.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Multiple package-manager system updater"
license = "GPL-3.0-or-later"
url = "https://github.com/topgrade-rs/topgrade"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "351a1f1a1676662aa00ad6440e7b493ae40fd40dd609cbe8b3920df981835aae"
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
    with open(f"{self.cwd}/topgrade.1", "w") as o:
        self.do(
            f"target/{self.profile().triplet}/release/topgrade",
            "--gen-manpage",
            stdout=o,
        )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/topgrade")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"topgrade.{shell}", shell)
    self.install_man("topgrade.1")
    self.install_file(
        "config.example.toml", "usr/share/examples/topgrade/config.toml"
    )
