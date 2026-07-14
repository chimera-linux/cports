pkgname = "zvm"
pkgver = "0.8.27"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1bc95c6da1c7855f62392416c4c7d61825806654db987c71c1d79515f395c3df"
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
