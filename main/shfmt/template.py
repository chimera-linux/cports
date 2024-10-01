pkgname = "shfmt"
pkgver = "3.9.0"
pkgrel = 2
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
sha256 = "d8bd0b83cd41bb65420395d6efb7d2c4bfcd535fbf3d702325d150e5ee2d1809"


def post_install(self):
    self.install_license("LICENSE")
    with open(self.cwd / "cmd/shfmt/shfmt.1.scd", "rb") as i:
        with open(self.cwd / "cmd/shfmt/shfmt.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)
            self.install_man(self.cwd / "cmd/shfmt/shfmt.1")
