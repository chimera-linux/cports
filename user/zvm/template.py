pkgname = "zvm"
pkgver = "0.8.20"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dfeadf7a54bb14e2cc1819dc1e3b533e34dbe01b0747be55ed0c8615fa767616"
# generates completions with host binary
options = ["!cross"]


# add fish completions after https://github.com/tristanisham/zvm/issues/161 gets fixed
def post_build(self):
    for shell in ["bash", "zsh"]:
        with open(self.cwd / f"zvm.{shell}", "w") as f:
            self.do(f"{self.make_dir}/zvm", "completion", shell, stdout=f)


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "zsh"]:
        self.install_completion(f"zvm.{shell}", shell)
