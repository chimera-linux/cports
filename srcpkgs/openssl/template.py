pkgname = "openssl"
version = "1.1.1k"
revision = 1
bootstrap = True
build_style = "configure"
configure_script = "Configure"
configure_args = [
    "--prefix=/usr", "--openssldir=/etc/ssl", "--libdir=lib",
    "shared", "no-ssl3-method", "no-asm", "-Wa,--noexecstack"
]
make_check_target = "test"
make_install_args = ["MANSUFFIX=ssl"]
short_desc = "Toolkit for Secure Sockets Layer and Transport Layer Security"
maintainer = "John <johnz@posteo.net>"
license = "OpenSSL"
homepage = "https://www.openssl.org"
distfiles = [f"https://www.openssl.org/source/openssl-{version}.tar.gz"]
checksum = ["892a0875b9872acd04a9fde79b1f943075d5ea162415de3047c327df33fbaee5"]
conf_files = ["/etc/ssl/openssl.cnf"]

if not current.bootstrapping:
    hostmakedepends = ["perl"]

from cbuild import cpu

ecargs = cpu.match_target(
    "x86_64*", ["enable-ec_nistp_64_gcc_128", "linux-x86_64"],
    "aarch64*", ["linux-aarch64"],
    "ppc64le*", ["linux-ppc64le"],
    "ppc64*", ["linux-ppc64"],
    "*", None
)

if not ecargs:
    broken = f"Unknown CPU: {cpu.target()}"

configure_args += ecargs

def pre_configure(self):
    #self.configure_args += self.CPPFLAGS
    self.configure_args += self.CFLAGS
    self.configure_args += self.LDFLAGS

def do_build(self):
    self.make.invoke("depend")
    self.make.build(["MAKEDEPPROG=" + self.tools["CC"]])

@subpackage("libcrypto1.1")
def _libcrypto(self):
    self.short_desc = short_desc + " - crypto library"

    def install():
        self.take("usr/lib/libcrypto.so.*")
        self.take("usr/lib/engines-1.1")

    return install

@subpackage("libssl1.1")
def _libssl(self):
    self.short_desc = short_desc + " - SSL/TLS library"

    def install():
        self.take("usr/lib/libssl.so.*")

    return install

@subpackage("openssl-c_rehash")
def _crehash(self):
    self.short_desc = short_desc + " - c_rehash utility"
    self.depends = ["openssl"]

    if not self.bootstrapping:
        self.depends.append("perl")

    def install():
        self.take("usr/bin/c_rehash")

    return install

@subpackage("openssl-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [
        f"{pkgname}={version}-r{revision}",
        "libssl1.1={version}-r{revision}",
        "libcrypto1.1={version}-r{revision}"
    ]

    def install():
        self.take("usr/share/man/man3")
        self.take("usr/share/doc")
        self.take("usr/include")
        self.take("usr/lib/pkgconfig")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")

    return install
