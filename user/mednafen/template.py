pkgname = "mednafen"
pkgver = "1.32.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-external-libzstd",
    "--with-external-lzo",
]
hostmakedepends = ["automake", "gettext-devel", "pkgconf"]
makedepends = [
    "alsa-lib-devel",
    "flac-devel",
    "glu-devel",
    "lzo-devel",
    "sdl2-compat-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Multi-system emulator"
license = "GPL-2.0-or-later"
url = "https://mednafen.github.io"
source = f"https://mednafen.github.io/releases/files/mednafen-{pkgver}.tar.xz"
sha256 = "de7eb94ab66212ae7758376524368a8ab208234b33796625ca630547dbc83832"
_cfl = ["-DMDFN_DISABLE_PICPIE_ERRWARN", "-fno-strict-aliasing"]
tool_flags = {"CFLAGS": [*_cfl], "CXXFLAGS": [*_cfl]}
# uses -fwrapv
hardening = ["!int"]

if self.profile.arch in ["ppc64", "ppc64le"]:
    configure_args += ["--enable-altivec"]
