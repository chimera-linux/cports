pkgname = "schismtracker"
pkgver = "20260524"
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
sha256 = "1e567e7ce5d9c68aac7b348e03b4cdb652d23fc4652b0089b83238e62d8925de"
tool_flags = {
    "CFLAGS": [
        f'-DVERSION2="{pkgver}"',
        # crashes when parsing config otherwise
        "-U_FORTIFY_SOURCE",
    ],
}


def post_install(self):
    self.rename(
        "usr/share/pixmaps/schism-icon-128.png",
        "usr/share/icons/hicolor/128x128/apps",
        relative=False,
        keep_name=True,
    )
