pkgname = "chrpath"
pkgver = "0.16"
pkgrel = 1
build_style = "configure"
configure_args = ["--prefix=/usr"]
pkgdesc = "Chrpath can modify the rpath and runpath of ELF executables"
license = "GPL-2.0-or-later"
url = "https://directory.fsf.org/wiki/Chrpath"
source = [
    f"https://alioth-archive.debian.org/releases/{pkgname}/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.gz",
]
sha256 = [
        "bb0d4c54bac2990e1bdf8132f2c9477ae752859d523e141e72b3b11a12c26e7b",
        ]

def post_install(self):
    self.install_license("COPYING")

    self.uninstall(f"usr/doc/{pkgname}-{pkgver}/*", glob=True)
