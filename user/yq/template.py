pkgname = "yq"
pkgver = "4.54.3"
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
    "93143d49b2a3bd6cb723477f585366b29f70c636af4653191d61b49b0c47de7f",
    "23f2af15723d51db671a647f17dc386678d9ca85bc314025db466b102d47c1f3",
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
