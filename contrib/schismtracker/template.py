pkgname = "schismtracker"
pkgver = "20240523"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl-devel", "flac-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "956e844c0da6ff57a97ee27a173cb07c9c9c550f24bce23a3525f37936ee4fb2"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
