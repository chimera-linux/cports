pkgname = "senpai"
pkgver = "0.3.0"
pkgrel = 11
build_style = "go"
make_build_args = ["./cmd/senpai"]
hostmakedepends = ["go", "scdoc"]
pkgdesc = "IRC client that works best with bouncers"
maintainer = "triallax <triallax@tutanota.com>"
license = "ISC"
url = "https://git.sr.ht/~delthas/senpai"
source = f"https://git.sr.ht/~delthas/senpai/archive/v{pkgver}.tar.gz"
sha256 = "c02f63a7d76ae13ed888fc0de17fa9fd5117dcb3c9edc5670341bf2bf3b88718"


def post_build(self):
    self.do("make", "doc")


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/senpai.1")
    self.install_man("doc/senpai.5")
