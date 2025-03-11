pkgname = "shfmt"
pkgver = "3.11.0"
pkgrel = 1
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
sha256 = "69aebb0dd4bf5e62842c186ad38b76f6ec2e781188cd71cea33cb4e729086e94"


def post_install(self):
    self.install_license("LICENSE")
    with open(self.cwd / "cmd/shfmt/shfmt.1.scd", "rb") as i:
        with open(self.cwd / "cmd/shfmt/shfmt.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)
            self.install_man(self.cwd / "cmd/shfmt/shfmt.1")
