pkgname = "yq"
pkgver = "4.40.7"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["bash", "tzdata"]
pkgdesc = "Command-line YAML processor"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/mikefarah/yq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "c38024d40ee37d26caba1824965d9ea1d65468f48b2bacd45647ff4f547fa59f"


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
        self.install_completion(f"yq.{shell}", shell=shell)
