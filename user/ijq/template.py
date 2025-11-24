pkgname = "ijq"
pkgver = "1.2.0"
pkgrel = 1
build_style = "go"
make_build_args = ["-ldflags", f"-X main.Version={pkgver}"]
hostmakedepends = ["go", "scdoc"]
depends = ["jq"]
pkgdesc = "Interactive jq repl to preview filters"
license = "GPL-3.0-or-later"
url = "https://git.sr.ht/~gpanders/ijq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "11ac7f233bac6dd8fa97399c90bcf4ffb311367eb31a95ddcf5f36708561a0f0"


def post_build(self):
    self.do("make", "docs")


def post_install(self):
    self.install_man("ijq.1")
