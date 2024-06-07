pkgname = "syntax-highlighting"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "perl",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Syntax highlighting engine for structured text and code"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://api.kde.org/frameworks/syntax-highlighting/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/syntax-highlighting-{pkgver}.tar.xz"
sha256 = "38300a35c969bef5fa36b437d54342da0a0c805282a657519bd4e2f7b42df984"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("syntax-highlighting-devel")
def _devel(self):
    return self.default_devel()
