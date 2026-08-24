pkgname = "classicube"
pkgver = "1.3.8"
pkgrel = 0
build_style = "makefile"
make_build_args = ["CFLAGS=-DDEFAULT_WIN_BACKEND=CC_WIN_BACKEND_SDL3"]
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
# FIXME int: crashes at runtime
hardening = ["!int"]
# Makefile has no check target, FIXME lintpixmaps
options = ["!check", "!lintpixmaps"]


def install(self):
    self.install_bin("ClassiCube")
    # Avoid having to run "misc/linux/install-desktop-entry.sh"
    self.install_file(
        self.files_path / "ClassiCube.desktop", "usr/share/applications"
    )
    self.install_file(
        "misc/CCicon.png", "usr/share/pixmaps", name="ClassiCube.png"
    )
    self.install_license("license.txt")
