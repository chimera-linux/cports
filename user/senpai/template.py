pkgname = "senpai"
pkgver = "0.4.0"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/senpai"]
hostmakedepends = ["go", "scdoc"]
pkgdesc = "IRC client that works best with bouncers"
license = "ISC"
url = "https://git.sr.ht/~delthas/senpai"
source = f"https://git.sr.ht/~delthas/senpai/archive/v{pkgver}.tar.gz"
sha256 = "ff5697bc09a133b73a93db17302309b81d6d11281ea85d80157f1977e8b1a1e2"


def post_build(self):
    self.do("make", "doc")


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/senpai.1")
    self.install_man("doc/senpai.5")
    self.install_file("contrib/senpai.desktop", "usr/share/applications")
