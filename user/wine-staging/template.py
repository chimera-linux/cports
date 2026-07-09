# keep in sync with main/wine
pkgname = "wine-staging"
pkgver = "11.12"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "gnu_configure"
configure_args = [
    "--disable-tests",
    "--enable-tools",
    "--enable-win64",
]
make_install_args = [
    "STRIP=true",
    "STRIPPROG=true",
]
hostmakedepends = [
    "automake",
    "bash",
    "git",
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
    "linux-headers",
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
# low priority provider so it can seamlessly replace wine
# (for quality of life when you have e.g. winetricks installed)
provides = ["wine=0"]
pkgdesc = "Compatibility layer for running Windows programs on Linux"
subdesc = "staging patchset"
license = "LGPL-2.1-or-later"
url = "https://www.winehq.org"
# the url is .0 for .0 and .x for >0
source = [
    f"https://dl.winehq.org/wine/source/11.x/wine-{pkgver}.tar.xz",
    f"https://github.com/wine-staging/wine-staging/archive/refs/tags/v{pkgver}.tar.gz",
]
source_paths = [".", "staging"]
sha256 = [
    "d3bc091192d985846c9f20065cc81f21331f01e22b736b131e3449e1306671bc",
    "9d72a105560a6e05fb37edf03e7521b2e3eafb49acd0ce5e344ef1bca5ff2730",
]
# FIXME: int breaks wine
# trivial-auto-var-init relies on memset() symbol existing during link for vars
# which isn't the case for loader/preloader.o:(map_so_lib)
hardening = ["!int", "!var-init"]
# lto: relocation R_X86_64_32 out of range,
# for 32-bit component
# check: tests hard to run, etc, meh
options = ["!lto", "!check"]

match self.profile().arch:
    case "x86_64":
        configure_args += ["--enable-archs=x86_64,i386"]


def post_patch(self):
    self.do("./staging/staging/patchinstall.py", "--all", "DESTDIR=.")


def post_install(self):
    self.install_link("usr/bin/wine64", "wine")


@subpackage("wine-staging-devel")
def _(self):
    # ditto
    self.provides = ["wine-devel=0"]
    # llvm-strip/objcopy cannot handle windows .a's
    self.nostrip_files = [
        "usr/lib/wine/*-*/*.a",
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
            "usr/lib/wine/*-*/*.a",
        ]
    )
