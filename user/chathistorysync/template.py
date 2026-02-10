pkgname = "chathistorysync"
pkgver = "0.2.1"
pkgrel = 16
build_style = "go"
hostmakedepends = [
    "go",
    "scdoc",
]
pkgdesc = "Synchronization tool for IRC chat history"
license = "AGPL-3.0-only"
url = "https://git.sr.ht/~emersion/chathistorysync"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "dc1fdbd1910b356d239afc2cffdd181faa47b8a82cf3251281c99cd3d612b4cf"
# no tests
options = ["!check"]


def post_build(self):
    with open(self.cwd / "chathistorysync.1.scd", "rb") as i:
        with open(self.cwd / "chathistorysync.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("chathistorysync.1")
