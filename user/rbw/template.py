pkgname = "rbw"
pkgver = "1.14.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Unofficial Bitwarden CLI"
license = "MIT"
url = "https://github.com/doy/rbw"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c551ec4665d26f6282ba6a5f46c71df79304f8c618a836c653f0289ff3ebb94e"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"rbw.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/rbw",
                "gen-completions",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"rbw.{shell}", shell)
