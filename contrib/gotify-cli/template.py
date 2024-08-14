pkgname = "gotify-cli"
pkgver = "2.3.2"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X main.Version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Command line interface for pushing messages to a gotify server"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://gotify.net"
source = f"https://github.com/gotify/cli/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e3b798d89138fdbc355a66d0fc2ca96676591366460f72c8f38b81365bebe5ba"


def install(self):
    self.install_bin("build/cli", name="gotify")
    self.install_license("LICENSE")
