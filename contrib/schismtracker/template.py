pkgname = "schismtracker"
pkgver = "20240614"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl-devel", "flac-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "91200e61f7b5a5c1193ca491e2ea9cd5fd74f2462e5af88a7e8d9e7c115481ac"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
