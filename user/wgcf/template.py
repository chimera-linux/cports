pkgname = "wgcf"
pkgver = "2.2.29"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Unofficial CLI for Cloudflare Warp"
license = "MIT"
url = "https://github.com/ViRb3/wgcf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "25bd436c3d0919c8e76a2e31806520c401c9561663946951746d4027a7fab96a"
# cross: generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"wgcf.{shell}", "w") as f:
            self.do(f"{self.make_dir}/wgcf", "completion", shell, stdout=f)


def post_install(self):
    self.install_license("LICENSE")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"wgcf.{shell}", shell)
