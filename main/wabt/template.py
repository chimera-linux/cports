pkgname = "wabt"
pkgver = "1.0.36"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/WebAssembly/wabt"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    "https://github.com/WebAssembly/wasm-c-api/archive/b6dd1fb658a282c64b029867845bc50ae59e1497.tar.gz",
    "https://github.com/okdshin/PicoSHA2/archive/27fcf6979298949e8a462e16d09a0351c18fcaf2.tar.gz",
    # test deps
    "https://github.com/simd-everywhere/simde/archive/71fd833d9666141edcd1d3c109a80e228303d8d7.tar.gz",
    "https://github.com/WebAssembly/testsuite/archive/f3f048661dc1686d556a27d522df901cb747ab4a.tar.gz",
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
    "e07ceeecfc682c12157ff2738b8a4633d7d19da18c1ecf16daae700397ecce2c",
    "2f2cca48d7c093a680461fc80e7ef812f383cdf6e421a718a5292fd42438960b",
    "18d82bb79c021ccf4ce58125b64691accef54237ba5194462740bacf8b39d8a9",
    "72b2c14a487560b7eb203795f2c2fead5c7499662e639944cca2a9bb19f09029",
    "052dbb79eeaedbaa7af068b7b85e1125d187719b597e2242fb2cfabf51226e73",
    "34010745593cfb395fd483a0f65688dcd61e3f16de574edb5d43ea2cfbd57131",
]


def check(self):
    self.do(
        "python",
        "test/run-tests.py",
        "--bindir",
        self.make_dir,
        "--timeout",
        "600",
        "--jobs",
        str(self.make_jobs),
        "--exclude-dir",
        # these fail on ppc64le due to differing output values from golder
        "spec",
    )


@subpackage("wabt-devel")
def _(self):
    return self.default_devel()
