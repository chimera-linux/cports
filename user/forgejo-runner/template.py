pkgname = "forgejo-runner"
pkgver = "12.7.2"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Task runner for Forgejo"
license = "GPL-3.0-only"
url = "https://code.forgejo.org/forgejo/runner"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8085a66ad64cdd19c35af82d4f59b033dbf3f4b1302b6d2ec785a3059520d799"
# check: needs network access
options = ["!check"]


def install(self):
    self.install_bin("build/runner", name="forgejo-runner")


def post_install(self):
    self.install_license("LICENSE")
