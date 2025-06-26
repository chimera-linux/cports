pkgname = "rbw"
pkgver = "1.13.2"
pkgrel = 2
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Unofficial Bitwarden CLI"
license = "MIT"
url = "https://github.com/doy/rbw"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "afe8887b64c4da6e5f33535d02ad4e1fe75c536a55d63291622b4b339522d138"
# generates completions using binary
options = ["!cross"]


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
    self.install_service("^/rbw.user")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"rbw.{shell}", shell)
