pkgname = "wine"
pkgver = "8.15"
pkgrel = 0
archs = ["x86_64"]
build_style = "gnu_configure"
configure_args = [
    "--disable-tests",
    "--enable-win64",
    "--enable-archs=x86_64,i386",
]
make_cmd = "gmake"
make_install_args = [
    "STRIP=true",
    "STRIPPROG=true",
]
hostmakedepends = [
    "autoconf",
    "automake",
    "gmake",
    "pkgconf",
]
makedepends = [
    "bison",
    "cups-devel",
    "dbus-devel",
    "flex",
    "fontconfig-devel",
    "freetype-devel",
    "gettext",
    "gnutls-devel",
    "gst-plugins-base-devel",
    "libgphoto2-devel",
    "libpcap-devel",
    "libpulse-devel",
    "libusb-devel",
    "libxcomposite-devel",
    "libxcursor-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "mesa-devel",
    "ncurses-devel",
    "pcsc-lite-devel",
    "samba-devel",
    "sane-backends-devel",
    "sdl-devel",
    "udisks-devel",
    "v4l-utils-devel",
    "vulkan-loader",
    "wayland-devel",
]
# not traced but needed
depends = ["libxrandr"]
pkgdesc = "Compatibility layer for running Windows programs on Linux"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://www.winehq.org"
# the url is .0 for .0 and .x for >0
source = f"https://dl.winehq.org/wine/source/8.x/wine-{pkgver}.tar.xz"
sha256 = "ed8fae61784bca6475accc78eff26a9ec6b08001a7ae1698d52e25f9c2d422da"
# FIXME: int breaks wine
hardening = ["!int"]
# lto: relocation R_X86_64_32 out of range,
# for 32-bit component
# check: tests hard to run, etc, meh
options = ["!lto", "!check"]


def post_install(self):
    # when building 64+32 compat, only bare name is emitted, add *64 names for compat
    self.install_link("wine", "usr/bin/wine64")
    self.install_link("wine-preloader", "usr/bin/wine64-preloader")

    # all of these are the same wineapploader shell script that uses $0,
    # so just create links to it
    self.install_bin("build/tools/wineapploader")
    for link in [
        "msidb",
        "msiexec",
        "notepad",
        "regedit",
        "regsvr32",
        "wineboot",
        "winecfg",
        "wineconsole",
        "winefile",
        "winemine",
        "winepath",
    ]:
        self.rm(self.destdir / f"usr/bin/{link}")
        self.install_link("wineapploader", f"usr/bin/{link}")


@subpackage("wine-devel")
def _devel(self):
    # llvm-strip/objcopy cannot handle windows .a's
    self.nostrip_files = [
        "usr/lib/wine/i386-windows/*.a",
        "usr/lib/wine/x86_64-windows/*.a",
    ]
    return self.default_devel(
        extra=[
            "usr/bin/function_grep.pl",
            "usr/bin/widl",
            "usr/bin/winebuild",
            "usr/bin/winecpp",
            "usr/bin/winedbg",
            "usr/bin/winedump",
            "usr/bin/wineg++",
            "usr/bin/winegcc",
            "usr/bin/winemaker",
            "usr/bin/wmc",
            "usr/bin/wrc",
            "usr/lib/wine/i386-windows/*.a",
            "usr/lib/wine/x86_64-unix/*.a",
            "usr/lib/wine/x86_64-windows/*.a",
        ]
    )
