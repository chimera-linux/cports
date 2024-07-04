pkgname = "thunderbird"
pkgver = "115.12.2"
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
    "python3.11",
    "rust",
    "wasi-sdk",
    "xserver-xorg-xvfb",
    "zip",
]
makedepends = [
    "alsa-lib-devel",
    "dbus-devel",
    # XXX: https://bugzilla.mozilla.org/show_bug.cgi?id=1532281
    "dbus-glib-devel",
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
    "zlib-ng-compat-devel",
]
depends = ["virtual:cmd:thunderbird!thunderbird-wayland"]
pkgdesc = "Thunderbird mail client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND MPL-2.0"
url = "https://www.thunderbird.net"
source = f"$(MOZILLA_SITE)/{pkgname}/releases/{pkgver.replace('_beta', 'b')}/source/{pkgname}-{pkgver.replace('_beta', 'b')}.source.tar.xz"
sha256 = "6378a0dbe8d785f58ab9778a507e36c33a5f869ae1a670638e27787b9864e638"
debug_level = 1  # defatten, especially with LTO
tool_flags = {
    "LDFLAGS": ["-Wl,-rpath=/usr/lib/thunderbird", "-Wl,-z,stack-size=2097152"]
}
env = {
    "MAKE": "/usr/bin/gmake",
    "PYTHON": "/usr/bin/python3.11",
    "SHELL": "/usr/bin/sh",
    "BUILD_OFFICIAL": "1",
    "MOZILLA_OFFICIAL": "1",
    "USE_SHORT_LIBNAME": "1",
    "MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE": "system",
    "MOZ_APP_REMOTINGNAME": "Thunderbird",
    "MOZ_NOSPAM": "1",
    # thunderbird checks for it by calling --help
    "CBUILD_BYPASS_STRIP_WRAPPER": "1",
}
# FIXME: see firefox
hardening = ["!int"]
options = ["!cross"]

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

    for crate in ["audio_thread_priority", "bindgen"]:
        cargo.clear_vendor_checksums(self, crate, vendor_dir="third_party/rust")


def init_configure(self):
    from cbuild.util import cargo

    self.env["MOZBUILD_STATE_PATH"] = str(self.chroot_srcdir / ".mozbuild")
    self.env["AS"] = self.get_tool("CC")
    self.env["MOZ_MAKE_FLAGS"] = f"-j{self.make_jobs}"
    self.env["RUST_TARGET"] = self.profile().triplet
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
        "--disable-crashreporter",
        "--disable-profiling",
        "--disable-jemalloc",
        "--disable-tests",
        "--disable-updater",
        "--disable-alsa",
        # mail options
        "--enable-official-branding",
        "--enable-application=comm/mail",
        "--allow-addon-sideload",
    ]

    match self.profile().arch:
        case "x86_64" | "aarch64":
            conf_opts += ["--disable-elf-hack"]

    if self.has_lto():
        conf_opts += ["--enable-lto=cross"]

    # PGO; tries to connect to the network, but maybe someday?
    if False:
        # configure for profiling
        self.log("bootstrapping profile...")
        with self.stamp("profile_configure") as s:
            s.check()
            self.log("configuring profile build...")
            self.do(
                "python3.11",
                "./mach",
                "configure",
                *conf_opts,
                "--enable-profile-generate=cross",
            )
        # do the profiling build
        with self.stamp("profile_build") as s:
            s.check()
            self.log("building profile build...")
            self.do("python3.11", "./mach", "build")
        # package it
        with self.stamp("profile_package") as s:
            s.check()
            self.log("packaging profile build...")
            self.do("python3.11", "./mach", "package")
        # generate the profile data
        with self.stamp("profile_generate") as s:
            s.check()
            self.log("generating profile...")
            for d in self.cwd.glob("obj-*"):
                ldp = self.chroot_cwd / d.name / "dist/thunderbird"
            self.do(
                "xvfb-run",
                "-w",
                "10",
                "-s",
                "-screen 0 1920x1080x24",
                "python3.11",
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
            self.do("python3.11", "./mach", "clobber")
        # and finally make use of this for real configure
        conf_opts += [
            "--enable-profile-use=cross",
            f"--with-pgo-profile-path={self.chroot_cwd / 'merged.profdata'}",
            f"--with-pgo-jarlog={self.chroot_cwd / 'jarlog'}",
        ]

    self.log("configuring final thunderbird...")
    self.do("python3.11", "./mach", "configure", *conf_opts)


def do_build(self):
    self.do("python3.11", "./mach", "build")


def do_install(self):
    self.do(
        "python3.11",
        "./mach",
        "install",
        env={"DESTDIR": str(self.chroot_destdir)},
    )

    self.install_file(
        self.files_path / "vendor.js",
        "usr/lib/thunderbird/defaults/preferences",
    )
    self.install_file(
        self.files_path / "thunderbird.desktop", "usr/share/applications"
    )

    # icons
    for sz in [16, 22, 24, 32, 48, 128, 256]:
        self.install_file(
            f"comm/mail/branding/thunderbird/default{sz}.png",
            f"usr/share/icons/hicolor/{sz}x{sz}/apps",
            name="thunderbird.png",
        )

    # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
    self.uninstall("usr/lib/thunderbird/thunderbird-bin")
    self.install_link("usr/lib/thunderbird/thunderbird-bin", "thunderbird")
    # to be provided
    self.uninstall("usr/bin/thunderbird")
    # default launcher
    self.install_link(
        "usr/bin/thunderbird-default", "../lib/thunderbird/thunderbird"
    )
    # wayland launcher
    self.install_file(
        self.files_path / "thunderbird-wayland",
        "usr/lib/thunderbird",
        mode=0o755,
    )
    self.install_link(
        "usr/bin/thunderbird-wayland",
        "../lib/thunderbird/thunderbird-wayland",
    )


def do_check(self):
    # XXX: maybe someday
    pass


@subpackage("thunderbird-wayland")
def _wl(self):
    self.pkgdesc = f"{pkgdesc} (prefer Wayland)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]  # prefer

    return ["@usr/bin/thunderbird=>thunderbird-wayland"]


@subpackage("thunderbird-default")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (no display server preference)"

    return ["@usr/bin/thunderbird=>thunderbird-default"]
