pkgname = "go-md2man"
pkgver = "2.0.3"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Markdown to manpage converter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/cpuguy83/go-md2man"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "7ca3a04bb4ab83387538235decc42a535097a05d2fb9f2266d0c47b33119501f"
# objcopy fails on ppc
options = ["!debug"]


def post_extract(self):
    # delete stray incomplete vendor dir
    self.rm("vendor/", recursive=True)


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
