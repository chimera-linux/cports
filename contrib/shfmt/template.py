pkgname = "shfmt"
pkgver = "3.7.0"
pkgrel = 0
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
sha256 = "89eafc8790df93305dfa42233e262fb25e1c96726a3db420a7555abadf3111ed"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")
    with open(self.cwd / "cmd/shfmt/shfmt.1.scd", "rb") as i:
        with open(self.cwd / "cmd/shfmt/shfmt.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)
            self.install_man(self.cwd / "cmd/shfmt/shfmt.1")
