pkgname = "elfutils"
pkgver = "0.191"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-nls",
    "--disable-werror",
    "--enable-deterministic-archives",
    "--with-zstd",
    "--program-prefix=eu-",
]
# autoreconf generates junk configure
configure_gen = []
make_cmd = "gmake"
hostmakedepends = [
    "bison",
    "flex",
    "gmake",
    "pkgconf",
]
makedepends = [
    "argp-standalone",
    "bzip2-devel",
    "libarchive-devel",
    "libcurl-devel",
    "libmicrohttpd-devel",
    "linux-headers",
    "musl-bsd-headers",
    "musl-fts-devel",
    "musl-obstack-devel",
    "sqlite-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["bash"]
# transitional
provides = [f"elftoolchain={pkgver}-r{pkgrel}"]
pkgdesc = "Utilities and libraries to handle ELF files and DWARF data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later AND (GPL-2.0-or-later OR LGPL-3.0-or-later)"
url = "https://sourceware.org/elfutils"
source = (
    f"https://sourceware.org/elfutils/ftp/{pkgver}/elfutils-{pkgver}.tar.bz2"
)
sha256 = "df76db71366d1d708365fc7a6c60ca48398f14367eb2b8954efc8897147ad871"
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE", "-Wno-unaligned-access"],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152"],
}


def post_build(self):
    self.ln_s("eustack", "build/src/stack")


def post_install(self):
    self.rename("usr/bin/eu-eustack", "eu-stack")


@subpackage("debuginfod")
def _dinfod(self):
    self.pkgdesc = f"{pkgdesc} (debuginfod)"

    return [
        "usr/bin/debuginfod*",
        "usr/share/man/man[18]/debuginfod*",
    ]


@subpackage("debuginfod-libs")
def _dinfod_libs(self):
    self.pkgdesc = f"{pkgdesc} (debuginfod library)"

    return [
        "etc/profile.d",
        "usr/lib/libdebuginfod.so.*",
        "usr/lib/libdebuginfod-*.so",
    ]


@subpackage("elfutils-libs")
def _libs(self):
    # since the resolved (after symlinks) filename of the .so is without
    # a suffix, the automatic virtual version would be 0, which would
    # prevent upgrades from elftoolchain (which had 1)
    pv = pkgver[2:]
    self.provides = [
        f"libelf={pkgver}-r{pkgrel}",  # transitional
        f"so:libasm.so.1={pv}",  # allow for upgrade
        f"so:libdw.so.1={pv}",
        f"so:libelf.so.1={pv}",
    ]

    return self.default_libs(extra=[f"usr/lib/*-{pkgver}.so"])


@subpackage("elfutils-devel")
def _devel(self):
    # transitional
    self.provides = [f"elftoolchain-devel={pkgver}-r{pkgrel}"]

    return self.default_devel()
