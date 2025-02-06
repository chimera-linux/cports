pkgname = "openjdk17"
pkgver = "17.0.14_p7"
pkgrel = 1
_majver = pkgver.split(".")[0]
_fver = pkgver.split("_")[0]
_bver = pkgver.split("_p")[-1]
# we don't attempt zero, it's a waste of time
archs = ["x86_64", "aarch64", "ppc64le", "ppc64"]
build_style = "gnu_configure"
configure_args = [
    "--disable-warnings-as-errors",
    "--disable-precompiled-headers",
    "--enable-dtrace=no",
    "--with-jvm-variants=server",
    "--with-zlib=system",
    "--with-libjpeg=system",
    "--with-libpng=system",
    "--with-giflib=system",
    "--with-lcms=system",
    "--with-jtreg=no",
    "--with-debug-level=release",
    "--with-native-debug-symbols=none",
    "--with-toolchain-type=clang",
    "--with-version-pre=",
    "--with-version-build=" + _bver,
    "--with-version-opt=chimera-r" + str(pkgrel),
    "--with-vendor-name=Chimera",
    "--with-vendor-url=https://chimera-linux.org",
    "--with-vendor-bug-url=https://github.com/chimera-linux/cports/issues",
    "--with-vendor-vm-bug-url=https://github.com/chimera-linux/cports/issues",
]
configure_gen = []
make_build_args = ["jdk-image"]
hostmakedepends = [
    "automake",
    "bash",
    "file",
    "libtool",
    "linux-headers",
    "openssl3",
    "pkgconf",
    "zip",
    "zlib-ng-compat-devel",
]
makedepends = [
    "alsa-lib-devel",
    "cups-devel",
    "fontconfig-devel",
    "freetype-devel",
    "giflib-devel",
    "lcms2-devel",
    "libjpeg-turbo-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "libxt-devel",
    "libxtst-devel",
    "linux-headers",
]
depends = [
    self.with_pkgver(f"{pkgname}-jdk"),
    self.with_pkgver(f"{pkgname}-demos"),
]
pkgdesc = f"Oracle OpenJDK {_majver}"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only WITH Classpath-exception-2.0"
url = "https://openjdk.org"
source = f"https://github.com/openjdk/jdk{_majver}u/archive/jdk-{_fver}+{_bver}.tar.gz"
sha256 = "98a6eb04bf7067ea040c0e1fa068845db822bf3f9ca686436327a834fa796f30"
# FIXME: SIGILL in jvm
hardening = ["!int"]
# TODO later
options = ["!parallel", "!check", "linkundefver", "empty"]

_java_base = "usr/lib/jvm"
_java_name = "java-17-openjdk"
_java_home = f"{_java_base}/{_java_name}"
env = {
    "LD_LIBRARY_PATH": f"/{_java_home}/lib:/{_java_home}/lib/server",
    "CBUILD_BYPASS_STRIP_WRAPPER": "1",
}

# we want this on BE too, and on LE the buildsystem skips it for clang
# skipping it means generating code for ELFv1 ABI and that does not work
if self.profile().arch == "ppc64" or self.profile().arch == "ppc64le":
    tool_flags = {"CFLAGS": ["-DABI_ELFv2"], "CXXFLAGS": ["-DABI_ELFv2"]}

if self.profile().cross:
    hostmakedepends += ["openjdk17"]
else:
    hostmakedepends += ["openjdk17-bootstrap"]


def init_configure(self):
    self.configure_args += [
        "--prefix=/" + _java_home,
        "--with-boot-jdk=/" + _java_home,
        "--with-jobs=" + str(self.conf_jobs),
        "--with-extra-cflags=" + self.get_cflags(shell=True),
        "--with-extra-cxxflags=" + self.get_cxxflags(shell=True),
        "--with-extra-ldflags=" + self.get_ldflags(shell=True),
    ]
    if self.profile().cross:
        self.configure_args += [
            "BUILD_CC=/usr/bin/cc",
            "BUILD_CXX=/usr/bin/c++",
        ]
    if self.use_ccache:
        if self.profile().cross:
            self.configure_args += [
                "--with-sysroot=" + str(self.profile().sysroot)
            ]
        self.configure_args += ["--enable-ccache"]
        self.env["CC"] = "/usr/bin/" + self.get_tool("CC")
        self.env["CXX"] = "/usr/bin/" + self.get_tool("CXX")


def configure(self):
    from cbuild.util import gnu_configure

    gnu_configure.replace_guess(self)
    gnu_configure.configure(self, sysroot=False)


@custom_target("bootstrap", "build")
def _(self):
    # first make a copy
    bdirn = f"openjdk-bootstrap-{pkgver}-{self.profile().arch}"
    self.mkdir(bdirn)
    for f in (self.cwd / "build/images/jdk").iterdir():
        self.cp(f, bdirn, recursive=True)
    # remove src, we don't need it
    self.rm(self.cwd / bdirn / "lib/src.zip")
    # strip libs
    for f in (self.cwd / bdirn).rglob("*.so"):
        print("STRIP", f.relative_to(self.cwd))
        self.do("llvm-strip", f.relative_to(self.cwd))
    # make an archive
    self.do(
        "tar",
        "cvf",
        f"{bdirn}.tar.zst",
        "--zstd",
        "--options",
        f"zstd:compression-level=19,zstd:threads={self.make_jobs}",
        bdirn,
    )
    self.log_green("SUCCESS: build done, collect your tarball in builddir")


def install(self):
    # install the stuff
    for f in (self.cwd / "build/images/jdk").iterdir():
        self.install_files(f, _java_home)

    # extras
    self.install_file("ASSEMBLY_EXCEPTION", _java_home)
    self.install_file("LICENSE", _java_home)
    self.install_file("README.md", _java_home)

    # shared cacerts store
    _cacerts = f"{_java_home}/lib/security/cacerts"
    self.uninstall(_cacerts)
    self.install_link(_cacerts, "../../../../../../etc/ssl/certs/java/cacerts")

    # system links

    self.install_dir("usr/bin")
    self.install_dir("usr/share/man/man1")
    self.install_link(f"{_java_base}/default", _java_name)

    for f in (self.destdir / _java_home / "bin").iterdir():
        self.install_link(
            f"usr/bin/{f.name}", f"../lib/jvm/{_java_name}/bin/{f.name}"
        )

    for f in (self.destdir / _java_home / "man/man1").iterdir():
        self.install_link(
            f"usr/share/man/man1/{f.name}",
            f"../../../lib/jvm/{_java_name}/man/man1/{f.name}",
        )


@subpackage(f"openjdk{_majver}-demos")
def _(self):
    self.subdesc = "demos"

    return [f"{_java_home}/demo"]


@subpackage(f"openjdk{_majver}-jmods")
def _(self):
    self.subdesc = "jmods"

    return [f"{_java_home}/jmods"]


@subpackage(f"openjdk{_majver}-src")
def _(self):
    self.subdesc = "sources"
    self.depends = [self.with_pkgver(f"openjdk{_majver}-jre-headless")]

    return [f"{_java_home}/lib/src.zip"]


@subpackage(f"openjdk{_majver}-jre")
def _(self):
    self.subdesc = "runtime"
    self.depends = [self.with_pkgver(f"openjdk{_majver}-jre-headless")]

    return [
        f"{_java_home}/lib/libawt_xawt.so",
        f"{_java_home}/lib/libfontmanager.so",
        f"{_java_home}/lib/libjavajpeg.so",
        f"{_java_home}/lib/libjawt.so",
        f"{_java_home}/lib/libjsound.so",
        f"{_java_home}/lib/liblcms.so",
        f"{_java_home}/lib/libsplashscreen.so",
    ]


@subpackage(f"openjdk{_majver}-jre-headless")
def _(self):
    self.subdesc = "headless runtime"
    self.depends = ["java-cacerts", "java-common"]
    self.options = ["brokenlinks"]

    return [
        f"{_java_home}/bin/java",
        f"{_java_home}/bin/jfr",
        f"{_java_home}/bin/jrunscript",
        f"{_java_home}/bin/keytool",
        f"{_java_home}/bin/rmiregistry",
        f"{_java_home}/conf",
        f"{_java_home}/legal",
        f"{_java_home}/lib/*.so",
        f"{_java_home}/lib/classlist",
        f"{_java_home}/lib/j*",
        f"{_java_home}/lib/modules",
        f"{_java_home}/lib/p*",
        f"{_java_home}/lib/s*",
        f"{_java_home}/lib/t*",
        f"{_java_home}/man/man1/java.1",
        f"{_java_home}/man/man1/jfr.1",
        f"{_java_home}/man/man1/jrunscript.1",
        f"{_java_home}/man/man1/keytool.1",
        f"{_java_home}/man/man1/rmiregistry.1",
        f"{_java_home}/release",
        # added by us
        f"{_java_home}/ASSEMBLY_EXCEPTION",
        f"{_java_home}/LICENSE",
        f"{_java_home}/README.md",
    ]


@subpackage(f"openjdk{_majver}-jdk")
def _(self):
    self.subdesc = "JDK"
    self.depends = [
        self.with_pkgver(f"openjdk{_majver}-jre"),
        self.with_pkgver(f"openjdk{_majver}-jmods"),
    ]

    return [
        f"{_java_home}/bin",
        f"{_java_home}/lib",
        f"{_java_home}/man",
        f"{_java_home}/include",
    ]


@subpackage(pkgname, alternative="java-jre-headless")
def _(self):
    # default version
    self.provider_priority = 100
    # compat
    self.provides = [
        self.with_pkgver(f"openjdk{_majver}-jre-headless-default"),
        "java-jre-headless",
    ]
    return [
        "usr/bin/java",
        "usr/bin/jfr",
        "usr/bin/jrunscript",
        "usr/bin/keytool",
        "usr/bin/rmiregistry",
        f"{_java_base}/default",
        "usr/share/man/man1/java.1",
        "usr/share/man/man1/jfr.1",
        "usr/share/man/man1/jrunscript.1",
        "usr/share/man/man1/keytool.1",
        "usr/share/man/man1/rmiregistry.1",
    ]


@subpackage(pkgname, alternative="java-jre")
def _(self):
    # default version
    self.provider_priority = 100
    # compat
    self.provides = [
        self.with_pkgver(f"openjdk{_majver}-jre-default"),
        "java-jre",
    ]
    # requires
    self.depends += [
        self.with_pkgver(f"java-jre-headless-openjdk{_majver}-default"),
        self.with_pkgver(f"openjdk{_majver}-jre"),
    ]
    # empty
    self.options = ["empty"]
    return []


@subpackage(pkgname, alternative="java-jdk")
def _(self):
    # default version
    self.provider_priority = 100
    # compat
    self.provides = [
        self.with_pkgver(f"openjdk{_majver}-jdk-default"),
        self.with_pkgver(f"openjdk{_majver}-default"),
        "java-jdk",
    ]
    # requires the stuff
    self.depends += [self.with_pkgver(f"java-jre-openjdk{_majver}-default")]
    return [
        "usr/bin",
        "usr/share/man",
    ]
