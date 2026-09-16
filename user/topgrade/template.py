pkgname = "topgrade"
pkgver = "17.8.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Multiple package-manager system updater"
license = "GPL-3.0-or-later"
url = "https://github.com/topgrade-rs/topgrade"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e723b723db7ef3179417e3529bd67a637a3ceafed8f63ee81202cfae9200ad9b"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    from cbuild.util import cargo

    for shell in ["bash", "fish", "zsh"]:
        with open(f"{self.cwd}/topgrade.{shell}", "w") as o:
            self.do(
                cargo.target_path(self, "topgrade"),
                "--gen-completion",
                shell,
                stdout=o,
            )
    with open(f"{self.cwd}/topgrade.1", "w") as o:
        self.do(
            cargo.target_path("topgrade"),
            "--gen-manpage",
            stdout=o,
        )


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "topgrade"))
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"topgrade.{shell}", shell)
    self.install_man("topgrade.1")
    self.install_file(
        "config.example.toml", "usr/share/examples/topgrade/config.toml"
    )
