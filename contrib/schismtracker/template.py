pkgname = "schismtracker"
pkgver = "20240809"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl-devel", "flac-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4dafacc4db2516629d377097573a3cad9ee41de44b2f3c956b360779440168e0"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE", f'-DVERSION2="{pkgver}"']}
