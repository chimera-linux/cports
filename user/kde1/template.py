pkgname = "kde1"
pkgver = "1.1.2"
pkgrel = 0
build_style = "meta"
depends = [
    f"kde1-kdebase~{pkgver}",
    f"kde1-kdeutils~{pkgver}",
]
pkgdesc = "KDE 1.x historical version"
license = "custom:meta"
url = "https://kde.org"


@subpackage("kde1-apps")
def _(self):
    self.subdesc = "apps"
    self.install_if = [self.parent]
    self.depends = [
        f"kde1-kdegames~{pkgver}",
        f"kde1-kdegraphics~{pkgver}",
        f"kde1-kdemultimedia~{pkgver}",
        f"kde1-kdenetwork~{pkgver}",
        f"kde1-kdetoys~{pkgver}",
    ]
    return []
