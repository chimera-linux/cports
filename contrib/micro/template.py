pkgname = "micro"
pkgver = "2.0.13"
pkgrel = 2
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/zyedidia/micro/v2/internal/util.Version={pkgver}",
    "./cmd/micro",
]
hostmakedepends = ["go"]
pkgdesc = "Terminal-based text editor"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "MIT"
url = "https://micro-editor.github.io"
source = f"https://github.com/zyedidia/micro/archive/v{pkgver}.tar.gz"
sha256 = "a96fff974ed6bd9a1dd58a33e54ff23b78783bbb3571b86d5c37d787b1e0e4be"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("assets/packaging/micro.1")
    self.install_file(
        "assets/packaging/micro.desktop", "usr/share/applications"
    )
    self.install_file(
        "assets/micro-logo-mark.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="micro.svg",
    )
