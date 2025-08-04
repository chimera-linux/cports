pkgname = "7zip"
pkgver = "25.01"
pkgrel = 0
# Alone2: CLI with all format support
build_wrksrc = "CPP/7zip/Bundles/Alone2"
build_style = "makefile"
make_build_args = [
    # silence garbage Werror+Weverything
    "CFLAGS_WARN_WALL=",
    "CFLAGS_WARN=",
]
make_use_env = True
pkgdesc = "File archiver with a high compression ratio"
license = "LGPL-2.0-only AND BSD-3-Clause AND custom:unrar"
url = "https://7-zip.org"
source = f"https://7-zip.org/a/7z{pkgver.replace('.', '')}-src.tar.xz"
sha256 = "ed087f83ee789c1ea5f39c464c55a5c9d4008deb0efe900814f2df262b82c36e"
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
    self.install_license("../../../../DOC/unRarLicense.txt")
    self.install_bin("b/c/7zz")
    self.install_link("usr/bin/7z", "7zz")
