pkgname = "vgrep"
pkgver = "2.8.0"
pkgrel = 9
build_style = "go"
make_build_args = [f"-ldflags=-X main.version={pkgver}"]
hostmakedepends = ["go", "go-md2man"]
pkgdesc = "Pager for grep output"
license = "GPL-3.0-or-later"
url = "https://github.com/vrothberg/vgrep"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "325b28bd5e8da316e319361f2dd8e3cc74fcd55724fc8ad4b2a73c21b2903bd8"


def post_build(self):
    self.do("go-md2man", "-in", "docs/vgrep.1.md", "-out", "docs/vgrep.1")


def post_install(self):
    self.install_man("docs/vgrep.1")
