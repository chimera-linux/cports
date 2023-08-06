pkgname = "go-md2man"
pkgver = "2.0.2"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Markdown to manpage converter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/cpuguy83/go-md2man"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2f52e37101ea2734b02f2b54a53c74305b95b3a9a27792fdac962b5354aa3e4a"
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
