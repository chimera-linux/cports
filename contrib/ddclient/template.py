pkgname = "ddclient"
pkgver = "3.11.2"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "curl",
]
depends = [
    "curl",
    "perl",
]
pkgdesc = "Client used to update dynamic DNS entries"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "GPL-2.0-or-later"
url = "https://ddclient.net"
source = (
    f"https://github.com/ddclient/ddclient/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "243cd832abd3cdd2b49903e1b5ed7f450e2d9c4c0eaf8ce4fe692c244d3afd77"


def post_install(self):
    self.install_service(self.files_path / "ddclient")
