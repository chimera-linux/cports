pkgname = "kde1-kdebase"
pkgver = "1.1.2"
pkgrel = 4
_gitrev = "4987e047002f9b8364c16fa0e6650717c24bcc7e"
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "elogind-devel",
    "kde1-kdelibs-devel",
    "libjpeg-turbo-devel",
    "libpulse-devel",
    "libxau-devel",
    "libxdmcp-devel",
    "libxpm-devel",
    "libxscrnsaver-devel",
    "libxt-devel",
    "linux-pam-devel",
    "mesa-devel",
    "ncurses-devel",
    "openssl3-devel",
    "qt1-devel",
]
# for konsole
depends = ["font-misc-misc"]
pkgdesc = "KDE1 base applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/KDE/kde1-kdebase"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "480b847c73cf00bed6c8f6095e73bf61e41e6ae38d9fb0e1d97d3b149521107d"
hardening = ["!int", "!format"]
options = ["!lto"]

tool_flags = {
    "CFLAGS": [
        "-Wno-deprecated-non-prototype",
    ],
    "CXXFLAGS": [
        "-std=gnu++98",
        "-Wno-format-security",
        "-Wno-c++11-extensions",
        "-Wno-c++11-compat-deprecated-writable-strings",
    ],
}


# conflicts with kde6
def post_install(self):
    self.uninstall("usr/cgi-bin")
    self.rename("usr/bin/kstart", "kstart1")
    for f in (self.destdir / "usr/share/locale").rglob("kstart.mo"):
        f.rename(f.with_name("kstart1.mo"))
