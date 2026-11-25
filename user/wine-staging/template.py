# keep in sync with main/wine
pkgname = "wine-staging"
pkgver = "11.22"
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
    "libatomic-chimera-devel-static",
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
    "llvm-runtimes-devel-static",
    "mesa-devel",
    "musl-devel-static",
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
    "f172e9c1be73e862057deae1f0e03ce95919986c5df8a18e1c0829c34863c9ee",
    "9c7dd979f23c551fa15caa16ba1ea039ab74c2ee5b17fdd471b5115f74a6ceb1",
]
# FIXME: int breaks wine
# trivial-auto-var-init relies on memset() symbol existing during link for vars
# which isn't the case for loader/preloader.o:(map_so_lib)
hardening = ["!int", "!var-init"]
# lto: relocation R_X86_64_32 out of range,
# for 32-bit component
# check: tests hard to run, etc, meh
options = ["!lto", "!check"]

match self.profile.arch:
    case "x86_64":
        configure_args += ["--enable-archs=x86_64,i386"]


def post_patch(self):
    self.do("./staging/staging/patchinstall.py", "--all", "DESTDIR=.")


def post_install(self):
    self.install_link("usr/bin/wine64", "wine")


@split("devel")
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
