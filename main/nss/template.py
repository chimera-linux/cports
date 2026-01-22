pkgname = "nss"
pkgver = "3.120"
pkgrel = 0
build_style = "makefile"
make_build_target = "all"
make_build_args = []
hostmakedepends = ["pkgconf", "perl"]
makedepends = [
    "linux-headers",
    "nspr-devel",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["bash"]
pkgdesc = "Mozilla Network Security Services"
license = "MPL-2.0"
url = "https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS"
source = f"$(MOZILLA_SITE)/security/nss/releases/NSS_{pkgver.replace('.', '_')}_RTM/src/nss-{pkgver}.tar.gz"
sha256 = "7ce5f5b3a172a41539ffc118d8ef4834974d0a6a782743e4a05a4e208dd6d22f"
tool_flags = {"CFLAGS": []}
env = {
    "LIBRUNPATH": "",
    "BUILD_OPT": "1",
    "NSS_USE_SYSTEM_SQLITE": "1",
    "NSS_ENABLE_WERROR": "0",
    "NSS_ENABLE_ECC": "1",
    "NSS_DISABLE_GTESTS": "1",
    "NSPR_INCLUDE_DIR": f"{self.profile().sysroot / 'usr/include/nspr'}",
    "NSPR_LIB_DIR": f"{self.profile().sysroot / 'usr/lib'}",
}


def post_patch(self):
    self.cp("^/install.sh", self.cwd)
    (self.cwd / "install.sh").chmod(0o755)


match self.profile().arch:
    case "x86_64":
        pass
    case "ppc64":
        env["NSS_DISABLE_CRYPTO_VSX"] = "1"
        env["NSS_DISABLE_AVX2"] = "1"
    case _:
        env["NSS_DISABLE_AVX2"] = "1"

if self.profile().wordsize == 64:
    env["USE_64"] = "1"
    make_build_args += ["USE_64=1"]
    tool_flags["CFLAGS"] += ["-DNS_PTR_GT_32"]

if self.profile().cross:
    make_build_args += ["CROSS_COMPILE=1"]

# because this may not match the cbuild arch name
match self.profile().arch:
    case (
        "x86_64"
        | "ppc64le"
        | "ppc64"
        | "ppc"
        | "aarch64"
        | "armv7"
        | "riscv64"
        | "loongarch64"
    ):
        _nssarch = self.profile().arch
    case _:
        broken = f"OS_TEST unknown for {self.profile().arch}"


def build(self):
    self.make.build(
        [
            "-C",
            "nss",
            f"-j{self.make_jobs}",
            f"OS_TEST={_nssarch}",
            "CCC=" + self.get_tool("CXX"),
            "NATIVE_CC=" + self.get_tool("CC", target="host"),
            "NATIVE_FLAGS=" + self.get_cflags(target="host", shell=True),
            "NATIVE_LDFLAGS=" + self.get_ldflags(target="host", shell=True),
        ],
        env={"XCFLAGS": self.get_cflags(shell=True)},
    )


def check(self):
    self.do(
        self.chroot_cwd / "nss/tests/all.sh",
        env={
            "HOST": "localhost",
            "DOMSUF": "localdomain",
            "XCFLAGS": self.get_cflags(shell=True),
            # full suite takes like >2 hours to complete
            "NSS_TESTS": "cipher libpkix",
            "NSS_CYCLES": "standard",
        },
        wrksrc="nss/tests",
    )


def install(self):
    self.do(
        self.chroot_cwd / "install.sh",
        env={
            "DESTDIR": str(self.chroot_destdir),
            "NSS_VERSION": pkgver,
        },
    )


@subpackage("nss-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
