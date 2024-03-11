pkgname = "goattracker"
pkgver = "2.76"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_dir = "src"
make_use_env = True
hostmakedepends = ["gmake", "imagemagick"]
makedepends = ["sdl12-compat-devel"]
pkgdesc = "C64 music editor"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/p/goattracker2"
source = f"$(SOURCEFORGE_SITE)/goattracker2/GoatTracker%202/{pkgver}/GoatTracker_{pkgver}.zip"
sha256 = "c1b6b159ec0d37ae68599ac83be8934a71cd543e480eb5225f844b62151cea34"
# no tests
options = ["!check"]


def do_install(self):
    self.install_bin("linux/goattrk2", name="goattracker")
    self.install_bin("linux/gt2reloc")
    self.install_bin("linux/ins2snd2")
    self.install_bin("linux/mod2sng")
    self.install_bin("linux/sngspli2")
    self.install_man("linux/goattracker.1")
    self.install_file("goat_tracker_commands.pdf", "usr/share/doc/goattracker")
    self.install_file("readme.txt", "usr/share/doc/goattracker")
    self.install_file(
        "examples/*.sng", "usr/share/doc/goattracker/examples", glob=True
    )
    self.install_file(
        self.files_path / "goattracker.desktop", "usr/share/applications"
    )
    self.do("convert", "-quality", "95", "src/goattrk2.bmp", "goattracker.png")
    self.install_file("goattracker.png", "usr/share/icons/hicolor/32x32/apps")
