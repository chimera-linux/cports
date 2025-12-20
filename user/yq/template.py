pkgname = "yq"
pkgver = "4.50.1"
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
    "ec55f107fbfe1d8226c1d4d74def734672f9aa58165029819ddfb771339e53a1",
    "de17f76a2488e5b0351a4adb6eccd4abdc561b8bfa25f993c8ac74c69c8124d1",
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
