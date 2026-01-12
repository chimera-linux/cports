pkgname = "micro"
pkgver = "2.0.15"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/zyedidia/micro/v2/internal/util.Version={pkgver}",
    "./cmd/micro",
]
hostmakedepends = ["go"]
pkgdesc = "Terminal-based text editor"
license = "MIT"
url = "https://micro-editor.github.io"
source = f"https://github.com/zyedidia/micro/archive/v{pkgver}.tar.gz"
sha256 = "612c775321c268c8f9e1767505ff378bca9b9ab66f5c41b69ecb2464ecf15084"


def pre_build(self):
    from cbuild.util import golang

    self.do("go", "generate", "./runtime", env=golang.get_go_env(self))


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
