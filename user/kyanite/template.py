pkgname = "kyanite"
pkgver = "0.0.1"
pkgrel = 0
build_style = "cargo"
configure_args = [
    "-Dbugreport_url=https://github.com/chimera-linux/cports/issues",
]
hostmakedepends = ["blueprint-compiler"]
makedepends = [
    "cargo",
    "gtk4-devel",
    "gtksourceview-devel",
    "libadwaita-devel",
    "libpanel-devel",
    "pkgconf",
    "vte-gtk4-devel",
]
pkgdesc = "Kyanite text editor"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/pastthepixels/kyanite"
source = "https://codeberg.org/pastthepixels/kyanite/archive/8e27198895ca5b7574fdf5176267c87c1cc1849e.tar.gz"
sha256 = "b15561466a1cda0df03ee281fe5efdf9015a742986889917bd52f4d0a9519b1a"
hardening = [
    "format",
    "int",
    "pie",
    "scp",
    "ssp",
    "var-init",
    "!bti",
    "!cet",
    "!cfi",
    "!pac",
    "!sst",
    "!vis",
]
# project doesn't have linting or tests
options = ["!check"]


def install(self):
    self.cargo.install(wrksrc="./")
    self.install_files(
        "resources/icons/hicolor/",
        "usr/share/icons/",
    )
    self.install_file(
        "resources/metadata/ca.potatoe.Kyanite.desktop",
        "usr/share/applications",
        mode=0o755,
    )
