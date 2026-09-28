pkgname = "shfmt"
pkgver = "3.14.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/shfmt"]
make_check_args = [*make_build_args]
hostmakedepends = ["go", "scdoc"]
pkgdesc = "Shell language formatter"
license = "BSD-3-Clause"
url = "https://github.com/mvdan/sh"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ec4bdb88ab6c95686be3a4eeb4ad77d2b49d33d2ed7b0a65035cd52d2d87c443"


def post_install(self):
    self.install_license("LICENSE")
    with open(self.cwd / "cmd/shfmt/shfmt.1.scd", "rb") as i:
        with open(self.cwd / "cmd/shfmt/shfmt.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)
            self.install_man(self.cwd / "cmd/shfmt/shfmt.1")
