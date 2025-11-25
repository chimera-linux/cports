pkgname = "yq"
pkgver = "4.49.2"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["bash", "tzdb"]
pkgdesc = "Command-line YAML processor"
license = "MIT"
url = "https://github.com/mikefarah/yq"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    f"{url}/releases/download/v{pkgver}/yq_man_page_only.tar.gz",
]
source_paths = [".", "manpage"]
sha256 = [
    "648d96cc490a4e08edb6bf8ff9498360b405263e202663cd9c92322b3aa557ef",
    "74f01170c0d866cf787660d3ba2be16d47c447889ddc558958789a02c99d2623",
]
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
    self.install_man("manpage/yq.1")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"yq.{shell}", shell)
