pkgname = "kitty"
pkgver = "0.35.1"
pkgrel = 1
hostmakedepends = [
    "go",
    "pkgconf",
    "python-setuptools",
    "wayland-progs",
    "wayland-protocols",
]
makedepends = [
    "dbus-devel",
    "fontconfig-devel",
    "freetype-devel",
    "gettext-devel",
    "harfbuzz-devel",
    "lcms2-devel",
    "libcanberra-devel",
    "libpng-devel",
    "libxcb-devel",
    "libxcursor-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "openssl-devel",
    "python-devel",
    "xxhash-devel",
]
depends = [
    f"kitty-kitten={pkgver}-r{pkgrel}",
    f"kitty-terminfo={pkgver}-r{pkgrel}",
]
pkgdesc = "Accelerated terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://sw.kovidgoyal.net/kitty"
source = f"https://github.com/kovidgoyal/kitty/releases/download/v{pkgver}/kitty-{pkgver}.tar.xz"
sha256 = "a9a4a5b06040b72f11f5f1c7bafe0f78b1e6a50dffb1903830f492aee42a63e4"
# nah
options = ["!cross"]

tool_flags = {
    # musl/posix ioctl int argument crap
    # sketchy simd garbage
    "CFLAGS": ["-Wno-error=overflow", "-DKITTY_NO_SIMD"],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152"],
}


def do_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def do_build(self):
    from cbuild.util import golang

    self.do(
        "python3",
        "setup.py",
        "linux-package",
        "--ignore-compiler-warnings",
        "--update-check-interval=0",
        "--verbose",
        env=golang.get_go_env(self),
    )


def do_install(self):
    # nuke pointless optimized pycache
    for f in (self.cwd / "linux-package").rglob("*.opt-*.pyc"):
        f.unlink()
    # install the rest as is
    self.install_files("linux-package", "", name="usr")


@subpackage("kitty-terminfo")
def _terminfo(self):
    self.pkgdesc = f"{pkgdesc} (terminfo data)"

    return ["usr/share/terminfo"]


@subpackage("kitty-kitten")
def _kitten(self):
    self.pkgdesc = f"{pkgdesc} (kitten client)"

    return ["usr/bin/kitten", "usr/share/man/man1/kitten*.1"]
