pkgname = "yq"
pkgver = "4.44.5"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["bash", "tzdata"]
pkgdesc = "Command-line YAML processor"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/mikefarah/yq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1505367f4a6c0c4f3b91c6197ffed4112d29ef97c48d0b5e66530cfa851d3f0e"
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
