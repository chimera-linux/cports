pkgname = "cmake"
pkgver = "3.28.0"
_actualver = "3.27.9"
pkgrel = 1
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--mandir=/share/man",
    "--docdir=/share/doc/cmake",
    "--generator=Ninja",
    "--system-libarchive",
    "--system-zlib",
    "--system-bzip2",
    "--system-liblzma",
    "--system-zstd",
    f"--parallel={self.conf_jobs}",
]
make_cmd = "ninja"
hostmakedepends = ["ninja"]
makedepends = [
    "libarchive-devel",
    "linux-headers",
    "ncurses-devel",
]
pkgdesc = "Cross-platform, open source build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://cmake.org"
source = f"https://www.cmake.org/files/v{_actualver[:-2]}/{pkgname}-{_actualver}.tar.gz"
sha256 = "609a9b98572a6a5ea477f912cffb973109ed4d0a6a6b3f9e2353d2cdc048708e"
# prevent cmake self-bootstrap false positive nonsense
tool_flags = {
    "CXXFLAGS": ["-Wno-unused-command-line-argument"],
}
hardening = ["vis"]
# checkdepends are missing
options = ["!check"]

# need to use bundled jsoncpp (i.e. --system-jsoncpp is not possible) as
# the two build systems that offers are meson and cmake - cmake cannot be
# used for obvious reasons, meson can't either as during stage 2 at the
# point cmake is built, meson is not yet available, but no big deal
if self.stage >= 2:
    # librash does not like cfi, so only set it when using system's
    hardening += ["cfi"]
    makedepends += [
        "libcurl-devel",
        "nghttp2-devel",
        "libexpat-devel",
        "libuv-devel",
        "rhash-devel",
    ]
    configure_args += [
        "--bootstrap-system-librhash",
        "--bootstrap-system-libuv",
        "--system-curl",
        "--system-nghttp2",
        "--system-expat",
        "--system-libuv",
        "--system-librhash",
        "--",
        # need these for correct linking
        "-DCMAKE_AR=/usr/bin/llvm-ar",
        "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
        "-DCMAKE_NM=/usr/bin/llvm-nm",
    ]


def post_install(self):
    self.install_license("Copyright.txt")
    self.cp("Utilities/KWIML/Copyright.txt", "KWIML-Copyright.txt")
    self.install_license("KWIML-Copyright.txt")
