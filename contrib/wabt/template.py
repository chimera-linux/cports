pkgname = "wabt"
pkgver = "1.0.35"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DBUILD_SHARED_LIBS=ON",
    "-DUSE_SYSTEM_GTEST=ON",
]
make_check_target = "run-tests"
hostmakedepends = [
    "cmake",
    "ninja",
    "python",
]
makedepends = ["gtest-devel"]
checkdepends = ["bash", "python-ply"]
pkgdesc = "WebAssembly binary toolkit"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/WebAssembly/wabt"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    "https://github.com/WebAssembly/wasm-c-api/archive/b6dd1fb658a282c64b029867845bc50ae59e1497.tar.gz",
    "https://github.com/okdshin/PicoSHA2/archive/27fcf6979298949e8a462e16d09a0351c18fcaf2.tar.gz",
    # test deps
    "https://github.com/simd-everywhere/simde/archive/54b8c8f83968dc30bd233e2b1050596eed7d8f7d.tar.gz",
    "https://github.com/WebAssembly/testsuite/archive/0a394e3cc9e08e0bcc3fc550916ccc9b1c71f981.tar.gz",
    "https://github.com/nodejs/uvwasi/archive/55eff19f4c7e69ec151424a037f951e0ad006ed6.tar.gz",
]
source_paths = [
    ".",
    "third_party/wasm-c-api",
    "third_party/picosha2",
    "third_party/simde",
    "third_party/testsuite",
    "third_party/uvwasi",
]
sha256 = [
    "c55bb2083de3afafa011ac1ab4aa14bab9fe51c2a90d24ba38f66f6b3bde0b09",
    "2f2cca48d7c093a680461fc80e7ef812f383cdf6e421a718a5292fd42438960b",
    "18d82bb79c021ccf4ce58125b64691accef54237ba5194462740bacf8b39d8a9",
    "a8e4289abf3a03ac6ea643525f8d126f06eab2cddaf799983b4e2381dd04d4f8",
    "28052e33f10ec462ea2993a9731bc65ed7e781ebece1694d94034f96374cc846",
    "34010745593cfb395fd483a0f65688dcd61e3f16de574edb5d43ea2cfbd57131",
]


def do_check(self):
    self.do(
        "python",
        "test/run-tests.py",
        "--bindir",
        f"{self.chroot_cwd}/{self.make_dir}",
        "--timeout",
        "600",
        "--jobs",
        f"{self.make_jobs}",
        "--exclude-dir",
        # these fail on ppc64le due to differing output values from golder
        "spec",
    )


@subpackage("wabt-devel")
def _devel(self):
    return self.default_devel()
