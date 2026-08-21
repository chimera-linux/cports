pkgname = "zvm"
pkgver = "0.8.29"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d41875911b44bf0faf01322b6ec46958d73a80e49a8d50db4380c1f064ddc6cd"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"zvm.{shell}", "w") as f:
            self.do(f"{self.make_dir}/zvm", "completion", shell, stdout=f)


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"zvm.{shell}", shell)
