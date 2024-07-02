pkgname = "chathistorysync"
pkgver = "0.2.0"
pkgrel = 2
build_style = "go"
hostmakedepends = [
    "go",
    "scdoc",
]
pkgdesc = "Synchronization tool for IRC chat history"
maintainer = "psykose <alice@ayaya.dev>"
license = "AGPL-3.0-only"
url = "https://git.sr.ht/~emersion/chathistorysync"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "97d428a7ce46caabdfcf13e1863eeaa534b7c8247d8bd9f8cbcc64c20e5cf86a"
# no tests
options = ["!check"]


def post_build(self):
    with open(self.cwd / "chathistorysync.1.scd", "rb") as i:
        with open(self.cwd / "chathistorysync.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("chathistorysync.1")
