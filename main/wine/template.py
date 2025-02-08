pkgname = "wine"
pkgver = "10.1"
pkgrel = 0
archs = ["x86_64"]
build_style = "gnu_configure"
configure_args = [
    "--disable-tests",
    "--enable-archs=x86_64,i386",
    "--enable-win64",
]
make_install_args = [
    "STRIP=true",
    "STRIPPROG=true",
]
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "bison",
    "cups-devel",
    "dbus-devel",
    "ffmpeg-devel",
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
    "ocl-icd-devel",
    "pcsc-lite-devel",
    "samba-devel",
    "sane-backends-devel",
    "sdl2-compat-devel",
    "udisks-devel",
    "v4l-utils-devel",
    "vulkan-loader-devel",
    "wayland-devel",
]
# not traced but needed
depends = ["libxrandr"]
pkgdesc = "Compatibility layer for running Windows programs on Linux"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.winehq.org"
# the url is .0 for .0 and .x for >0
source = f"https://dl.winehq.org/wine/source/10.x/wine-{pkgver}.tar.xz"
sha256 = "63471e37b1a515795ff3368d26a039261660e1377cb427d1b61b3a7b76091663"
# FIXME: int breaks wine
# trivial-auto-var-init relies on memset() symbol existing during link for vars
# which isn't the case for loader/preloader.o:(map_so_lib)
hardening = ["!int", "!var-init"]
# lto: relocation R_X86_64_32 out of range,
# for 32-bit component
# check: tests hard to run, etc, meh
options = ["!lto", "!check"]


def post_install(self):
    # when building 64+32 compat, only bare name is emitted, add *64 names for compat
    self.install_link("usr/bin/wine64", "wine")
    self.install_link("usr/bin/wine64-preloader", "wine-preloader")

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
        self.uninstall(f"usr/bin/{link}")
        self.install_link(f"usr/bin/{link}", "wineapploader")


@subpackage("wine-devel")
def _(self):
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
