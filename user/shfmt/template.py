pkgname = "shfmt"
pkgver = "3.13.0"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/shfmt"]
make_check_args = [*make_build_args]
hostmakedepends = ["go", "scdoc"]
pkgdesc = "Shell language formatter"
license = "BSD-3-Clause"
url = "https://github.com/mvdan/sh"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "efef583999befd358fae57858affa4eb9dc8a415f39f69d0ebab3a9f473d7dd3"


def post_install(self):
    self.install_license("LICENSE")
    with open(self.cwd / "cmd/shfmt/shfmt.1.scd", "rb") as i:
        with open(self.cwd / "cmd/shfmt/shfmt.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)
            self.install_man(self.cwd / "cmd/shfmt/shfmt.1")
