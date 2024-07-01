pkgname = "schismtracker"
pkgver = "20240630"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl-devel", "flac-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "55822248685eb6f3d99f95536a93969198eae92dda41cbde7f39fa1384bc758a"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE", f'-DVERSION2="{pkgver}"']}
