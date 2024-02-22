pkgname = "yq"
pkgver = "4.41.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["bash", "tzdata"]
pkgdesc = "Command-line YAML processor"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/mikefarah/yq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "25d61e72887f57510f88d1a30d515c7e2d79e7c6dce5c96aea7c069fcbc089e7"
# generates completions with host binary
options = ["!cross"]


def do_check(self):
    self.cp("build/yq", "yq")
    self.do("scripts/acceptance.sh")


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.do(
            "sh",
            "-c",
            f"{self.chroot_cwd}/build/yq shell-completion {shell} > yq.{shell}",
        )
        self.install_completion(f"yq.{shell}", shell)
