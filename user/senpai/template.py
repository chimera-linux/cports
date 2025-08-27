pkgname = "senpai"
pkgver = "0.4.1"
pkgrel = 4
build_style = "go"
make_build_args = ["./cmd/senpai"]
hostmakedepends = ["go", "scdoc"]
pkgdesc = "IRC client that works best with bouncers"
license = "ISC"
url = "https://git.sr.ht/~delthas/senpai"
source = f"https://git.sr.ht/~delthas/senpai/archive/v{pkgver}.tar.gz"
sha256 = "ab786b7b3cffce69d080c3b58061e14792d9065ba8831f745838c850acfeab24"


def post_build(self):
    self.do("make", "doc")


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/senpai.1")
    self.install_man("doc/senpai.5")
    self.install_file("contrib/senpai.desktop", "usr/share/applications")
    self.install_file(
        "res/icon.48.png",
        "usr/share/icons/hicolor/48x48/apps",
        name="senpai.png",
    )
    self.install_file(
        "res/icon.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="senpai.svg",
    )
