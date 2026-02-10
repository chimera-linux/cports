pkgname = "go-md2man"
pkgver = "2.0.7"
pkgrel = 6
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Markdown to manpage converter"
license = "MIT"
url = "https://github.com/cpuguy83/go-md2man"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "ca3a5b57e2c01759f5a00ad2a578d034c5370fae9aa7a6c3af5648b2fc802a92"


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
