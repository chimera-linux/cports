pkgname = "xed"
pkgver = "2026.08.23"
pkgrel = 0
hostmakedepends = ["python"]
pkgdesc = "Intel x86 encoder/decoder library"
license = "Apache-2.0"
url = "https://intelxed.github.io"
source = [
    f"https://github.com/intelxed/xed/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/intelxed/mbuild/archive/refs/tags/v{pkgver}.tar.gz>mbuild-v{pkgver}.tar.gz",
]
source_paths = ["xed", "mbuild"]
sha256 = [
    "4638942b38dabb7825e6340c1804c97e732837739dae375a0ad74314ecac1ffa",
    "1e4c9202488904e6fe4aca888daa937c69daf27cca55bc7a18d5a233309c6667",
]


def init_build(self):
    self._mbuild_args = [
        f"--jobs={self.make_jobs}",
        "--compiler=clang",
        "--shared",
        f"--extra-cxxflags={self.get_cxxflags(shell=True)}",
        f"--extra-ccflags={self.get_cflags(shell=True)}",
        f"--extra-linkflags={self.get_ldflags(shell=True)}",
        f"--cc={self.get_tool('CC')}",
        f"--cxx={self.get_tool('CXX')}",
        f"--linker={self.get_tool('LD')}",
        f"--ar={self.get_tool('AR')}",
        f"--as={self.get_tool('AS')}",
        f"--host-cpu={self.profile.arch}",
    ]


def build(self):
    self.mkdir("build", parents=True)
    self.do(
        "../xed/mfile.py",
        *self._mbuild_args,
        "examples",
        "install",
        wrksrc="build",
    )


def pre_check(self):
    # yank tests that rely on xed-dec-control (see xed-dec-control.patch)
    self.rm("xed/tests/tests-base/test-00184", recursive=True)
    self.rm("xed/tests/tests-base/test-00185", recursive=True)
    self.rm("xed/tests/tests-base/test-00186", recursive=True)
    self.rm("xed/tests/tests-base/test-00499", recursive=True)
    self.rm("xed/tests/tests-base/test-00500", recursive=True)
    # these check timing info that is stubbed out in non-x86
    if self.profile.arch != "x86_64":
        self.rm("xed/tests/tests-apx/test-00000", recursive=True)
        self.rm("xed/tests/tests-apx/test-00001", recursive=True)
        self.rm("xed/tests/tests-apx/test-00029", recursive=True)
        self.rm("xed/tests/tests-apx/test-00064", recursive=True)


def check(self):
    self.do(
        "../xed/mfile.py",
        *self._mbuild_args,
        "test",
        wrksrc="build",
    )


def install(self):
    self.install_bin("build/kits/*/bin/*", glob=True)
    self.install_lib("build/kits/*/lib/*", glob=True)
    self.install_dir("usr/include/xed")
    self.install_file(
        "build/kits/*/include/xed/*", "usr/include/xed", glob=True
    )


@subpackage("xed-devel")
def _(self):
    return ["usr/include"]
