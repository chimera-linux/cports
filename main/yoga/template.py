pkgname = "yoga"
pkgver = "3.2.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["gtest-devel"]
pkgdesc = "Embeddable ayout engine"
license = "MIT"
url = "https://www.yogalayout.dev"
source = f"https://github.com/react/yoga/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "86b399ac31fd820d8ffa823c3fae31bb690b6fc45301b2a8a966c09b5a088b55"


def check(self):
    self.do("tests/yogatests", wrksrc=self.make_dir)


def post_install(self):
    self.install_license("LICENSE")


@subpackage("yoga-devel")
def _(self):
    self.depends = [self.parent]

    return self.default_devel()
