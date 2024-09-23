pkgname = "wine"
pkgver = "9.18"
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
    "sdl-devel",
    "udisks-devel",
    "v4l-utils-devel",
    "vulkan-loader-devel",
    "wayland-devel",
]
# not traced but needed
depends = ["libxrandr"]
pkgdesc = "Compatibility layer for running Windows programs on Linux"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://www.winehq.org"
# the url is .0 for .0 and .x for >0
source = f"https://dl.winehq.org/wine/source/9.x/wine-{pkgver}.tar.xz"
sha256 = "6526f5211c085453bcb642946eb2ce8d1d42a8a4a68168bf2a0d73f32612dd1c"
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
            "cmd:function_grep.pl",
            "cmd:widl",
            "cmd:winebuild",
            "cmd:winecpp",
            "cmd:winedbg",
            "cmd:winedump",
            "cmd:wineg++",
            "cmd:winegcc",
            "cmd:winemaker",
            "cmd:wmc",
            "cmd:wrc",
            "usr/lib/wine/i386-windows/*.a",
            "usr/lib/wine/x86_64-unix/*.a",
            "usr/lib/wine/x86_64-windows/*.a",
        ]
    )
