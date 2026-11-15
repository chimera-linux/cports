pkgname = "ov"
pkgver = "0.55.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal pager"
license = "MIT"
url = "https://noborus.github.io/ov"
source = f"https://github.com/noborus/ov/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a715b1ef3e8a4d4525155a4d30458d44b2aab2c9741fe89dea8bfd3640691bb5"
# cross: generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"ov.{shell}", "w") as outf:
            self.do(
                "build/ov",
                "--completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"ov.{shell}", shell)
