pkgname = "go-md2man"
pkgver = "2.0.4"
pkgrel = 3
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Markdown to manpage converter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/cpuguy83/go-md2man"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b0a4c7c077ede56967deef6ab7e7696c0f46124b0b3360fd05564ec5a536f11f"
# objcopy fails on ppc
options = ["!debug"]


def post_build(self):
    self.do(
        self.chroot_cwd / self.make_dir / "go-md2man",
        "-in",
        "go-md2man.1.md",
        "-out",
        "go-md2man.1",
    )


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_man("go-md2man.1")
