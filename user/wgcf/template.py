pkgname = "wgcf"
pkgver = "2.2.30"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Unofficial CLI for Cloudflare Warp"
license = "MIT"
url = "https://github.com/ViRb3/wgcf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "91dae7e063476486643bc20005fa764380e2a3b38f42002b4c5e17da637bafba"
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
