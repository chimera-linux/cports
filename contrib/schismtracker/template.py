pkgname = "schismtracker"
pkgver = "20231029"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
makedepends = ["sdl-devel", "flac-devel", "libxv-devel"]
pkgdesc = "Reimplementation of Impulse Tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/releases/download/{pkgver}/schismtracker-{pkgver}.source.tar.gz"
sha256 = "bef92f12f32937c2aa450462b694a8871b94a0199fb8679371c4672526297b7e"
tool_flags = {"CFLAGS": [f'-DVERSION2="{pkgver}"']}
