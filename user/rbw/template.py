pkgname = "rbw"
pkgver = "1.14.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Unofficial Bitwarden CLI"
license = "MIT"
url = "https://github.com/doy/rbw"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e754da1cca32593e8af6b5d24d7a1eb82bf00e9811a8e42fd7293a6e36724f1d"


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
