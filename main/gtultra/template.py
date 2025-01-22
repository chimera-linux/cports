pkgname = "gtultra"
pkgver = "1.5.5"
pkgrel = 0
build_style = "makefile"
make_dir = "src"
make_use_env = True
hostmakedepends = ["pkgconf", "imagemagick"]
makedepends = ["sdl2-compat-devel", "alsa-lib-devel"]
pkgdesc = "C64 music editor"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://github.com/jpage8580/GTUltra"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eeec007e689d8934a466b33546830e4751445cec2d857d81581b3aa8d76b3294"
# no tests
options = ["!check"]


def install(self):
    self.install_bin("linux/*", glob=True)
    self.install_file("GTUltra.pdf", "usr/share/doc/gtultra")
    self.install_file(
        "readme - OriginalGT2 Documentation.txt", "usr/share/doc/gtultra"
    )
    self.install_files("examples", "usr/share/doc/gtultra")
    self.install_file(
        self.files_path / "gtultra.desktop", "usr/share/applications"
    )
    self.do("convert", "-quality", "95", "src/goattrk2.bmp", "gtultra.png")
    self.install_file("gtultra.png", "usr/share/icons/hicolor/32x32/apps")
