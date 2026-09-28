pkgname = "zvm"
pkgver = "0.9.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "49769334b7a1dfa3065306d8037b2a7baa9993207af60ee8e39015ece4b1c94f"
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
