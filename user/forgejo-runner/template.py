pkgname = "forgejo-runner"
pkgver = "12.7.3"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Task runner for Forgejo"
license = "GPL-3.0-only"
url = "https://code.forgejo.org/forgejo/runner"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a9a9b37adb6aa44707be90d3003870f5940424b54b0ad39a808a8e60dbfd649a"
# check: needs network access
options = ["!check"]


def install(self):
    self.install_bin("build/runner", name="forgejo-runner")


def post_install(self):
    self.install_license("LICENSE")
