pkgname = "senpai"
pkgver = "0.5.0"
pkgrel = 1
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X git.sr.ht/~delthas/senpai.version={pkgver}",
    "./cmd/senpai",
]
hostmakedepends = ["go", "scdoc"]
pkgdesc = "IRC client that works best with bouncers"
license = "ISC"
url = "https://git.sr.ht/~delthas/senpai"
source = f"https://git.sr.ht/~delthas/senpai/archive/v{pkgver}.tar.gz"
sha256 = "1793259dca5321f1365cae9d24316d5d4cd01df648d895eaa03eacb49f433db8"


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
