pkgname = "topgrade"
pkgver = "15.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Multiple package-manager system updater"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/topgrade-rs/topgrade"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "53c6521041a6ffddf1ccb13f404f131919a2ef48deb3974fc71dc3be08db6cd0"
_supported_shells = ["bash", "fish", "zsh"]
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in _supported_shells:
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
    for shell in _supported_shells:
        self.install_completion(f"topgrade.{shell}", shell)
    self.install_man("topgrade.8")
    self.install_file(
        "config.example.toml", "usr/share/examples/topgrade/config.toml"
    )
