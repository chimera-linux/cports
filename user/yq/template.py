pkgname = "yq"
pkgver = "4.54.1"
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
    "0cec36e7035dd56c508bda56245cbd71e4495d2317bc2528165c4162bce79335",
    "2f9db96faeb11a82fa80fe5af35d955f306b04e4d530e25f85b3574b41107414",
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
