pkgname = "go-md2man"
pkgver = "2.0.6"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Markdown to manpage converter"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/cpuguy83/go-md2man"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "5fa29154237bc840a10a06231c066f9ddbe06bb31d1c3372eab12e1ed977271f"


def post_build(self):
    self.do(
        f"{self.make_dir}/go-md2man",
        "-in",
        "go-md2man.1.md",
        "-out",
        "go-md2man.1",
    )


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_man("go-md2man.1")
