pkgname = "schismtracker"
pkgver = "20240609"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl-devel", "flac-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "83d73236c3d9d30353371bb38380010bed2d0fec15adb77fe1e04e3394535350"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
