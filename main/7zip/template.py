pkgname = "7zip"
pkgver = "24.08"
pkgrel = 1
# Alone2: CLI with all format support
build_wrksrc = "CPP/7zip/Bundles/Alone2"
build_style = "makefile"
make_build_args = [
    # nonfree rar sdk; uncompressed rar technically still supported
    "DISABLE_RAR_COMPRESS=1",
    # silence garbage Werror+Weverything
    "CFLAGS_WARN_WALL=",
    "CFLAGS_WARN=",
]
make_use_env = True
pkgdesc = "File archiver with a high compression ratio"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.0-only AND BSD-3-Clause"
url = "https://7-zip.org"
source = f"https://7-zip.org/a/7z{pkgver.replace('.', '')}-src.tar.xz"
sha256 = "aa04aac906a04df59e7301f4c69e9f48808e6c8ecae4eb697703a47bfb0ac042"
hardening = ["vis", "!cfi"]


match self.profile().arch:
    # TODO: there is an aarch64 file too
    # TODO: yoink the aur meson.build and just replace the whole build system, this is way too cursed
    case "x86_64":
        hostmakedepends = ["uasm"]
        # this makes unpacking a 7z up to 3-4x faster
        make_build_args += [
            "IS_X64=1",
            "MY_ASM=uasm",
            "USE_ASM=1",
        ]


def init_build(self):
    self.make_build_args += [
        "-f",
        # cwd is build type (alone2), -f .mak is toolchain type for some flags
        "../../cmpl_clang.mak",
        f"CC={self.get_tool('CC')}",
        f"CXX={self.get_tool('CXX')}",
    ]


def check(self):
    # no actual tests, so just compress+decompress something as useful sanity

    self.do(
        # b/c is toolchain clang; b/g is gcc
        self.chroot_cwd / "b/c/7zz",
        "a",
        "-y",
        "xxx.7z",
        # XXX: this is self.sources_path but chroot
        self.chroot_srcdir / "Asm",
        self.chroot_srcdir / "C",
    )

    self.do(
        self.chroot_cwd / "b/c/7zz",
        "x",
        "-y",
        "-o/tmp",
        "xxx.7z",
    )


def install(self):
    self.install_license("../../../../DOC/License.txt")
    self.install_bin("b/c/7zz")
    self.install_link("usr/bin/7z", "7zz")
