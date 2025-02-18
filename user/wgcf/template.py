pkgname = "wgcf"
pkgver = "2.2.25"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Unofficial CLI for Cloudflare Warp"
maintainer = "cassiofb-dev <contact@cassiofernando.com>"
license = "MIT"
url = "https://github.com/ViRb3/wgcf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1f994953aa4e9d6718dd7629957db9ee82f766e22975808cded1dcaf722734d8"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"wgcf.{shell}", "w") as f:
            self.do(f"{self.make_dir}/wgcf", "completion", shell, stdout=f)


def post_install(self):
    self.install_license("LICENSE")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"wgcf.{shell}", shell)
