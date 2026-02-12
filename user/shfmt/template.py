pkgname = "shfmt"
pkgver = "3.12.0"
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
license = "BSD-3-Clause"
url = "https://github.com/mvdan/sh"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ac15f42feeba55af29bd07698a881deebed1cd07e937effe140d9300e79d5ceb"


def post_install(self):
    self.install_license("LICENSE")
    with open(self.cwd / "cmd/shfmt/shfmt.1.scd", "rb") as i:
        with open(self.cwd / "cmd/shfmt/shfmt.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)
            self.install_man(self.cwd / "cmd/shfmt/shfmt.1")
