pkgname = "schismtracker"
pkgver = "20250415"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-flac-linking",
    "--enable-sdl3-linking",
]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "flac-devel",
    "sdl3-devel",
    "utf8proc-devel",
]
pkgdesc = "Reimplementation of Impulse Tracker"
license = "GPL-2.0-or-later"
url = "https://schismtracker.org"
source = f"https://github.com/schismtracker/schismtracker/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ba9b8e4381e9f3a3110ae7bb4e7794ac2399e88bb26a50c86a6f45beed57c5f3"
tool_flags = {
    "CFLAGS": [
        f'-DVERSION2="{pkgver}"',
        # crashes when parsing config otherwise
        "-U_FORTIFY_SOURCE",
    ],
}
# FIXME lintpixmaps
options = ["!lintpixmaps"]
