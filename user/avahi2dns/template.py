pkgname = "avahi2dns"
pkgver = "0.2.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["avahi", "dinit-chimera", "dinit-dbus"]
depends = ["avahi"]
pkgdesc = "DNS server that interfaces with Avahi"
license = "MIT"
url = "https://github.com/LouisBrunner/avahi2dns"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6ccdaad8dfaa74e186b1592f3620af1b255fae719f70cfa3edfca1a1f66faeb1"


def pre_build(self):
    from cbuild.util import golang

    self.do("go", "generate", ".", env=golang.get_go_env(self))


def post_install(self):
    self.install_service(self.files_path / "avahi2dns")
    self.install_license("LICENSE")
