pkgname = "shfmt"
pkgver = "3.8.0"
pkgrel = 4
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X main.version={pkgver}",
    "./cmd/shfmt",
]
make_check_args = ["./cmd/shfmt/..."]
hostmakedepends = ["go", "scdoc"]
pkgdesc = "Shell language formatter"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/mvdan/sh"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d8f28156a6ebfd36b68f5682b34ec7824bf61c3f3a38be64ad22e2fc2620bf44"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")
    with open(self.cwd / "cmd/shfmt/shfmt.1.scd", "rb") as i:
        with open(self.cwd / "cmd/shfmt/shfmt.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)
            self.install_man(self.cwd / "cmd/shfmt/shfmt.1")
