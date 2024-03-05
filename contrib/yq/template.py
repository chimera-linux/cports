pkgname = "yq"
pkgver = "4.42.1"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["bash", "tzdata"]
pkgdesc = "Command-line YAML processor"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/mikefarah/yq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "be31e5e828a0251721ea71964596832d4a40cbc21c8a8392a804bc8d1c55dd62"
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
