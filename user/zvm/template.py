pkgname = "zvm"
pkgver = "0.9.4"
pkgrel = 0
build_style = "go"
prepare_after_patch = True
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "90be104398c71959939decd4a924af87a53f27577aff069fe68eb4f090b4d18b"
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
