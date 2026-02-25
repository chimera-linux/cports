pkgname = "rbw"
pkgver = "1.15.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Unofficial Bitwarden CLI"
license = "MIT"
url = "https://github.com/doy/rbw"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "660cfa4c727711665bef060046c28dd3924ca1e490fdc058d90d35372b2d2cf6"


def post_build(self):
    for shell in ["bash", "fish", "nushell", "zsh"]:
        with open(self.cwd / f"rbw.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/rbw",
                "gen-completions",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "nushell", "zsh"]:
        self.install_completion(f"rbw.{shell}", shell)
