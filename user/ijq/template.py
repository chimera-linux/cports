pkgname = "ijq"
pkgver = "1.1.2"
pkgrel = 13
build_style = "go"
make_build_args = ["-ldflags", f"-X main.Version={pkgver}"]
hostmakedepends = ["go", "scdoc"]
depends = ["jq"]
pkgdesc = "Interactive jq repl to preview filters"
license = "GPL-3.0-or-later"
url = "https://git.sr.ht/~gpanders/ijq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "dd5055e7a740c54a32043b744f061b1a00a4d2f97f6c6214c2109fd22491b9f3"


def post_build(self):
    self.do("make", "docs")


def post_install(self):
    self.install_man("ijq.1")
