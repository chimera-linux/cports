pkgname = "openssl"
pkgver = "3.3.1"
pkgrel = 2
build_style = "configure"
configure_script = "Configure"
configure_args = [
    "--prefix=/usr",
    "--openssldir=/etc/ssl",
    "--libdir=lib",
    "enable-ktls",
    "shared",
    "-Wa,--noexecstack",
]
make_install_args = ["MANSUFFIX=ssl"]
make_check_target = "test"
make_check_args = [
    "TESTS="
    # XXX: with ktls enabled this fails if the running env can't utilise it
    + "-test_afalg"
    # FIXME: broken now for some reason and the test server hangs
    + " -test_quic*"
    # flaky on ppc64le
    + " -test_key_share"
    + " -test_sslrecords"
    + " -test_sslsigalgs"
]
hostmakedepends = ["pkgconf", "perl"]
pkgdesc = "Toolkit for Secure Sockets Layer and Transport Layer Security"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.openssl.org"
source = f"https://github.com/openssl/openssl/releases/download/openssl-{pkgver}/openssl-{pkgver}.tar.gz"
sha256 = "777cd596284c883375a2a7a11bf5d2786fc5413255efab20c50d6ffe6d020b7e"
compression = "deflate"
# the codebase is not LTO-ready:
# https://github.com/openssl/openssl/issues/18663
# https://github.com/openssl/openssl/issues/22854
options = ["bootstrap", "!lto"]

if self.stage > 0:
    makedepends = ["linux-headers"]
else:
    configure_args += ["no-asm"]

match self.profile().arch:
    case "x86_64":
        configure_args += ["enable-ec_nistp_64_gcc_128", "linux-x86_64"]
    case "aarch64" | "ppc64le" | "ppc64" | "ppc":
        configure_args += [f"linux-{self.profile().arch}"]
    case "riscv64":
        configure_args += ["linux64-riscv64"]
    case "armhf" | "armv7":
        configure_args += ["linux-armv4"]
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"


def pre_configure(self):
    self.configure_args += self.get_cflags()
    self.configure_args += self.get_ldflags()


def do_build(self):
    self.make.invoke("depend")
    self.make.build(["MAKEDEPPROG=" + self.get_tool("CC")])


def init_check(self):
    self.env["HARNESS_JOBS"] = str(self.make_jobs)


@subpackage("libcrypto3")
def _libcrypto(self):
    self.subdesc = "crypto library"

    return [
        "usr/lib/libcrypto.so.*",
        "usr/lib/engines-3",
        "usr/lib/ossl-modules",
    ]


@subpackage("libssl3")
def _libssl(self):
    self.subdesc = "SSL/TLS library"

    return ["usr/lib/libssl.so.*"]


@subpackage("openssl-c_rehash")
def _crehash(self):
    self.subdesc = "c_rehash utility"
    self.depends = ["openssl"]

    if self.stage > 0:
        self.depends.append("perl")

    return ["usr/bin/c_rehash"]


@subpackage("openssl-devel")
def _devel(self):
    self.depends = [
        self.parent,
    ]

    return self.default_devel()
