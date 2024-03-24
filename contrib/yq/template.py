pkgname = "yq"
pkgver = "4.43.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["bash", "tzdata"]
pkgdesc = "Command-line YAML processor"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/mikefarah/yq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e5581d28bae2bcdf70501dfd251233c592eb3e39a210956ee74965b784435d63"
# generates completions with host binary
options = ["!cross"]


def do_check(self):
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
