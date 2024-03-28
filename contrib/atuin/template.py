pkgname = "atuin"
pkgver = "18.1.0"
pkgrel = 0
build_wrksrc = "atuin"
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["sqlite-devel"]
pkgdesc = "Sync, search and backup tool for shell history"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/atuinsh/atuin"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "17712bed6528a7f82cc1dffd56b7effe28270ee2f99247908d7a6adff9474338"
# A bunch of failures yet to be investigated
# generates completions using host binary
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"atuin.{shell}", "w") as outf:
            self.do(
                f"../target/{self.profile().triplet}/release/atuin",
                "gen-completion",
                "--shell",
                shell,
                stdout=outf,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"atuin.{shell}", shell)
    self.install_license("LICENSE")
