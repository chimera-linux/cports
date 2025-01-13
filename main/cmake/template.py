pkgname = "cmake"
pkgver = "3.31.4"
pkgrel = 0
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
source = f"https://www.cmake.org/files/v{pkgver[:-2]}/cmake-{pkgver}.tar.gz"
sha256 = "a6130bfe75f5ba5c73e672e34359f7c0a1931521957e8393a5c2922c8b0f7f25"
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
        "curl-devel",
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


# if cross compiling, use host cmake outright
if self.profile().cross:
    build_style = "cmake"
    configure_args = [
        "-DCMAKE_MAN_DIR=/share/man",
        "-DCMAKE_DOC_DIR=/share/doc/cmake",
        "-DCMAKE_USE_SYSTEM_LIBARCHIVE=ON",
        "-DCMAKE_USE_SYSTEM_ZLIB=ON",
        "-DCMAKE_USE_SYSTEM_BZIP2=ON",
        "-DCMAKE_USE_SYSTEM_LIBLZMA=ON",
        "-DCMAKE_USE_SYSTEM_ZSTD=ON",
        "-DCMAKE_USE_SYSTEM_CURL=ON",
        "-DCMAKE_USE_SYSTEM_NGHTTP2=ON",
        "-DCMAKE_USE_SYSTEM_EXPAT=ON",
        "-DCMAKE_USE_SYSTEM_LIBUV=ON",
        "-DCMAKE_USE_SYSTEM_LIBRHASH=ON",
    ]
    hostmakedepends += ["cmake"]


def post_install(self):
    self.install_license("Copyright.txt")
    self.cp("Utilities/KWIML/Copyright.txt", "KWIML-Copyright.txt")
    self.install_license("KWIML-Copyright.txt")
