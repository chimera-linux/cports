pkgname = "schismtracker"
pkgver = "20240909"
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
sha256 = "3e29fb646e08ae210f027d1c8aaed4b6a0514b731202cb437a37b9685d40d6cd"
patch_style = "patch"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE", f'-DVERSION2="{pkgver}"']}
