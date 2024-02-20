pkgname = "firefox"
pkgver = "123.0"
pkgrel = 0
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "cargo",
    "cbindgen",
    "clang-devel",
    "gettext",
    "gmake",
    "libtool",
    "llvm-devel",
    "nasm",
    "nodejs",
    "pkgconf",
    "python",
    "rust",
    "wasi-sdk",
    "xserver-xorg-xvfb",
    "zip",
]
makedepends = [
    "alsa-lib-devel",
    "dbus-devel",
    "ffmpeg-devel",
    "freetype-devel",
    "glib-devel",
    "gtk+3-devel",
    "icu-devel",
    "libevent-devel",
    "libffi-devel",
    "libjpeg-turbo-devel",
    "libnotify-devel",
    "libogg-devel",
    "libpng-devel",
    "libpulse-devel",
    "libtheora-devel",
    "libvorbis-devel",
    "libvpx-devel",
    "libwebp-devel",
    "libxcomposite-devel",
    "libxscrnsaver-devel",
    "libxt-devel",
    "mesa-devel",
    "nspr-devel",
    "nss-devel",
    "pipewire-jack-devel",
    "pixman-devel",
    "rust-std",
    "zlib-devel",
]
depends = [
    "libavcodec",
]
provides = [
    # backwards-compatibility with old subpackages
    f"firefox-default={pkgver}-r{pkgrel}",
    f"firefox-wayland={pkgver}-r{pkgrel}",
]
pkgdesc = "Mozilla Firefox web browser"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND MPL-2.0"
url = "https://www.mozilla.org/firefox"
source = f"$(MOZILLA_SITE)/firefox/releases/{pkgver}/source/firefox-{pkgver}.source.tar.xz"
sha256 = "9e885abdaddb14cd4f313c1575282fec6af5901f445e9744fe24e2ea837d4cb7"
debug_level = 1  # defatten, especially with LTO
tool_flags = {
    "LDFLAGS": ["-Wl,-rpath=/usr/lib/firefox", "-Wl,-z,stack-size=2097152"]
}
env = {
    "MAKE": "/usr/bin/gmake",
    "SHELL": "/usr/bin/sh",
    "BUILD_OFFICIAL": "1",
    "MOZILLA_OFFICIAL": "1",
    "USE_SHORT_LIBNAME": "1",
    "MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE": "system",
    "MOZ_APP_REMOTINGNAME": "Firefox",
    "MOZ_NOSPAM": "1",
    "MOZBUILD_STATE_PATH": f"/builddir/{pkgname}-{pkgver}/.mozbuild",
    # firefox checks for it by calling --help
    "CBUILD_BYPASS_STRIP_WRAPPER": "1",
}
# FIXME: youtube causes crashes in libxul after some seconds
hardening = ["!int"]
# XXX: maybe someday
options = ["!cross", "!check"]

if self.profile().endian == "big":
    broken = "broken colors, needs patching, etc."

# crashes compiler in gl.c
if self.profile().arch == "riscv64":
    tool_flags["CXXFLAGS"] = ["-U_FORTIFY_SOURCE"]


def post_extract(self):
    self.cp(
        self.files_path / "stab.h", "toolkit/crashreporter/google-breakpad/src"
    )


def post_patch(self):
    from cbuild.util import cargo

    for crate in []:
        cargo.clear_vendor_checksums(self, crate, vendor_dir="third_party/rust")


def init_configure(self):
    from cbuild.util import cargo

    self.env["AS"] = self.get_tool("CC")
    self.env["MOZ_MAKE_FLAGS"] = f"-j{self.make_jobs}"
    self.env["RUST_TARGET"] = self.profile().triplet
    self.env["RUSTFLAGS"] = ""
    # use all the cargo env vars we enforce
    self.env.update(cargo.get_environment(self))


def do_configure(self):
    conf_opts = [
        "--prefix=/usr",
        "--libdir=/usr/lib",
        "--host=" + self.profile().triplet,
        "--target=" + self.profile().triplet,
        "--enable-linker=lld",
        "--enable-release",
        "--enable-optimize",
        "--disable-install-strip",
        "--disable-strip",
        "--with-wasi-sysroot=/usr/wasm32-unknown-wasi",
        # we have our own flags and better
        "--disable-hardening",
        # system libs
        "--with-system-pixman",
        "--with-system-ffi",
        "--with-system-nspr",
        "--with-system-nss",
        "--with-system-jpeg",
        "--with-system-webp",
        "--with-system-zlib",
        "--with-system-libevent",
        "--with-system-libvpx",
        "--with-system-icu",
        # no apng support
        "--without-system-png",
        # features
        "--enable-dbus",
        "--enable-jack",
        "--enable-ffmpeg",
        "--enable-pulseaudio",
        "--enable-necko-wifi",
        "--enable-default-toolkit=cairo-gtk3-wayland",
        "--enable-audio-backends=pulseaudio",
        # disabled features
        "--disable-profiling",
        "--disable-jemalloc",
        "--disable-tests",
        "--disable-updater",
        "--disable-alsa",
        # browser options
        "--enable-official-branding",
        "--enable-application=browser",
        "--allow-addon-sideload",
    ]

    match self.profile().arch:
        case "x86_64" | "aarch64":
            conf_opts += ["--enable-rust-simd"]

    if self.has_lto():
        conf_opts += ["--enable-lto=cross"]
        # configure for profiling
        self.log("bootstrapping profile...")
        with self.stamp("profile_configure") as s:
            s.check()
            self.log("configuring profile build...")
            self.do(
                "./mach",
                "configure",
                *conf_opts,
                "--enable-profile-generate=cross",
            )
        # do the profiling build
        with self.stamp("profile_build") as s:
            s.check()
            self.log("building profile build...")
            self.do("./mach", "build")
        # package it
        with self.stamp("profile_package") as s:
            s.check()
            self.log("packaging profile build...")
            self.do("./mach", "package")
        # generate the profile data
        with self.stamp("profile_generate") as s:
            s.check()
            self.log("generating profile...")
            for d in self.cwd.glob("obj-*"):
                ldp = self.chroot_cwd / d.name / "dist/firefox"
            self.do(
                "xvfb-run",
                "-w",
                "10",
                "-s",
                "-screen 0 1920x1080x24",
                "./mach",
                "python",
                "./build/pgo/profileserver.py",
                env={
                    "HOME": str(self.chroot_cwd),
                    "LLVM_PROFDATA": "llvm-profdata",
                    "JARLOG_FILE": str(self.chroot_cwd / "jarlog"),
                    "LD_LIBRARY_PATH": ldp,
                },
            )
        # clean up build dir
        with self.stamp("profile_clobber") as s:
            s.check()
            self.log("cleaning up profile build...")
            self.do("./mach", "clobber")
        # and finally make use of this for real configure
        conf_opts += [
            "--enable-profile-use=cross",
            f"--with-pgo-profile-path={self.chroot_cwd / 'merged.profdata'}",
            f"--with-pgo-jarlog={self.chroot_cwd / 'jarlog'}",
        ]

    self.log("configuring final firefox...")
    self.do("./mach", "configure", *conf_opts)


def do_build(self):
    self.do("./mach", "build")


def do_install(self):
    self.do(
        "./mach",
        "install",
        env={"DESTDIR": str(self.chroot_destdir)},
    )

    self.install_file(
        self.files_path / "vendor.js",
        "usr/lib/firefox/browser/defaults/preferences",
    )
    self.install_file(
        "taskcluster/docker/firefox-snap/firefox.desktop",
        "usr/share/applications",
    )

    # icons
    for sz in [16, 22, 24, 32, 48, 128, 256]:
        self.install_file(
            f"browser/branding/official/default{sz}.png",
            f"usr/share/icons/hicolor/{sz}x{sz}/apps",
            name="firefox.png",
        )

    # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
    self.rm(self.destdir / "usr/lib/firefox/firefox-bin")
    self.install_link("firefox", "usr/lib/firefox/firefox-bin")
