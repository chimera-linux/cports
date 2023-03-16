pkgname = "cmake"
pkgver = "3.26.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr", "--mandir=/share/man", "--docdir=/share/doc/cmake",
    "--system-libarchive", "--system-zlib", "--system-bzip2",
    "--system-liblzma", "--system-zstd",
    f"--parallel={self.conf_jobs}"
]
makedepends = ["libarchive-devel", "ncurses-devel", "linux-headers"]
pkgdesc = "Cross-platform, open source build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://cmake.org"
source = f"https://www.cmake.org/files/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.gz"
sha256 = "4256613188857e95700621f7cdaaeb954f3546a9249e942bc2f9b3c26e381365"
# prevent cmake self-bootstrap false positive nonsense
tool_flags = {
    "CXXFLAGS": ["-Wno-unused-command-line-argument"],
}
hardening = ["vis", "cfi"]
# checkdepends are missing
options = ["!check"]

# need to use bundled jsoncpp (i.e. --system-jsoncpp is not possible) as
# the two build systems that offers are meson and cmake - cmake cannot be
# used for obvious reasons, meson can't either as during stage 2 at the
# point cmake is built, meson is not yet available, but no big deal
if self.stage >= 2:
    makedepends += [
        "libcurl-devel", "nghttp2-devel", "libexpat-devel", "libuv-devel",
        "rhash-devel",
    ]
    configure_args += [
        "--system-curl", "--system-nghttp2", "--system-expat",
        "--system-libuv", "--system-librhash", "--",
        # need these for correct linking
        "-DCMAKE_AR=/usr/bin/llvm-ar", "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
        "-DCMAKE_NM=/usr/bin/llvm-nm",
    ]

def post_install(self):
    self.install_license("Copyright.txt")
    self.cp("Utilities/KWIML/Copyright.txt", "KWIML-Copyright.txt")
    self.install_license("KWIML-Copyright.txt")
