pkgname = "micro"
pkgver = "2.0.14"
pkgrel = 11
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
sha256 = "40177579beb3846461036387b649c629395584a4bbe970f61ba7591bd9c0185a"


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
