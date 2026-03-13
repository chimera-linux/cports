pkgname = "forgejo-runner"
pkgver = "12.7.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "File transfer tool"
license = "MIT"
url = "https://code.forgejo.org/forgejo/runner"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "509e846afd76e84bc5994b244e2ce0b986b4a9e99a8e80d5f31e691ce2efb6f4"
# check: needs network access
options = ["!check"]


def install(self):
    self.install_bin("build/runner", name="forgejo-runner")


def post_install(self):
    self.install_license("LICENSE")
