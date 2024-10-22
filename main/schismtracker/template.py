pkgname = "schismtracker"
pkgver = "20241021"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "flac-devel",
    "sdl-devel",
    "utf8proc-devel",
]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9615aeb37a29867306b92008c4579be185871ac0156009ce64be406b777b8f5d"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE", f'-DVERSION2="{pkgver}"']}
