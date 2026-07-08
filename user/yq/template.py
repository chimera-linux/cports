pkgname = "yq"
pkgver = "4.53.3"
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
    "fadf86d0ae3988bb40fa8aad424d0c71658493f6377285e711c7e7e313b3b238",
    "4c43e5b95084e0da8b11294b903f6c1164a65f7580794b4d48a2e6653379034e",
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
