pkgname = "wgcf"
pkgver = "2.2.23"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Unofficial CLI for Cloudflare Warp"
maintainer = "cassiofb-dev <contact@cassiofernando.com>"
license = "MIT"
url = "https://github.com/ViRb3/wgcf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "01851eee54954174bc7a0b6528252f5aee0d7996d48094f266011db3f20b1554"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"wgcf.{shell}", "w") as f:
            self.do(f"{self.make_dir}/wgcf", "completion", shell, stdout=f)


def post_install(self):
    self.install_license("LICENSE")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"wgcf.{shell}", shell)
