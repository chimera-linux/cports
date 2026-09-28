pkgname = "classicube"
pkgver = "1.3.8"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "BUILD_SDL3=1",
    "RELEASE=1",
    "CFLAGS=-DDEFAULT_WIN_BACKEND=CC_WIN_BACKEND_SDL3",
]
hostmakedepends = ["dos2unix"]
makedepends = [
    "mesa-devel",
    "openal-soft-devel",
    "sdl3-devel",
]
pkgdesc = "Sandbox building-block game"
license = "BSD-3-Clause AND CC0-1.0 AND MIT AND FTL"
url = "https://www.classicube.net"
source = f"https://github.com/ClassiCube/ClassiCube/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "35293acf1e63baeca832dec2512283f2975c79ddf80cc855a12c10464723a6c4"
hardening = ["!int"]
# Makefile has no check target
options = ["!check"]


def post_extract(self):
    # windows software lol
    self.do("dos2unix", "src/Logger.c")


def install(self):
    self.install_bin(self.files_path / "ClassiCube")
    self.install_file("ClassiCube", "usr/lib", mode=0o755)
    self.install_file("misc/CCicon.png", "usr/share/icons/hicolor/256x256/apps")
    self.do("sh", "misc/linux/install-desktop-entry.sh", self.chroot_destdir)
    self.install_license("license.txt")
