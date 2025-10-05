pkgname = "dive"
pkgver = "0.13.1"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Docker image and layer explorer"
license = "MIT"
url = "https://github.com/wagoodman/dive"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2a9666e9c3fddd5e2e5bad81dccda520b8102e7cea34e2888f264b4eb0506852"
# generates completions using binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"dive.{shell}", "w") as f:
            self.do("./build/dive", "completion", shell, stdout=f)


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"dive.{shell}", shell)
