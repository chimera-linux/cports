pkgname = "yq"
pkgver = "4.45.1"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["bash", "tzdb"]
pkgdesc = "Command-line YAML processor"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/mikefarah/yq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "074a21a002c32a1db3850064ad1fc420083d037951c8102adecfea6c5fd96427"
# generates completions with host binary
options = ["!cross"]


def check(self):
    self.cp("build/yq", "yq")
    self.do("scripts/acceptance.sh")


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"yq.{shell}", "w") as outf:
            self.do("build/yq", "shell-completion", shell, stdout=outf)


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"yq.{shell}", shell)
