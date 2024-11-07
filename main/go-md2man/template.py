pkgname = "go-md2man"
pkgver = "2.0.5"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Markdown to manpage converter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/cpuguy83/go-md2man"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6bb799e8fff06d82ca4617190157338d336e2361aa6c5b1786f763a684ffc3f2"


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
