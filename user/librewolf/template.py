# mirrors firefox package; own patches as version may drift
# always incorporate changes from firefox commits to keep in sync
pkgname = "librewolf"
pkgver = "156.0.1"
pkgrel = 0
hostmakedepends = [
    "automake",
    "cage",
    "cargo",
    "cbindgen",
    "clang-devel",
    "dbus",
    "gettext",
    "gtar",
    "libtool",
    "llvm-devel",
    "nasm",
    "nodejs",
    "pkgconf",
    "python",
    "rust",
    "wasi-sdk",
    "wlr-randr",
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
    "libffi8-devel",
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
depends = [
    "ffmpeg-avcodec-libs",
    "speechd-meta",
]
pkgdesc = "LibreWolf web browser"
license = "GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND MPL-2.0"
url = "https://librewolf.net"
source = f"https://librewolf.dev/api/packages/librewolf/generic/librewolf-source/{pkgver}-1/librewolf-{pkgver}-1.source.tar.gz"
sha256 = "93b6d0189fa1171b9ce9ee42c95f8721f7f10df0c1214922ee965a4efbc64f46"
debug_level = 1  # defatten, especially with LTO
tool_flags = {
    "LDFLAGS": ["-Wl,-rpath=/usr/lib/librewolf", "-Wl,-z,stack-size=2097152"]
}
env = {
    "SHELL": "/usr/bin/sh",
    "BUILD_OFFICIAL": "1",
    "MOZILLA_OFFICIAL": "1",
    "USE_SHORT_LIBNAME": "1",
    "MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE": "system",
    "MOZ_APP_REMOTINGNAME": "librewolf",
    "MOZ_NOSPAM": "1",
    "MOZ_CRASHREPORTER": "0",
    "MOZ_DATA_REPORTING": "0",
    "MOZ_TELEMETRY_REPORTING": "",
    "MOZ_REQUIRE_SIGNING": "",
    # librewolf checks for it by calling --help
    "CBUILD_BYPASS_STRIP_WRAPPER": "1",
}
# FIXME: youtube causes crashes in libxul after some seconds
hardening = ["!int"]
# XXX: maybe someday
options = ["!ci", "!cross", "!check"]

if self.profile.endian == "big":
    broken = "broken colors, needs patching, etc."

# crashes compiler in gl.c
if self.profile.arch == "riscv64":
    tool_flags["CXXFLAGS"] = ["-U_FORTIFY_SOURCE"]


def post_patch(self):
    from cbuild.util import cargo

    self.rm("lw/mozconfig.new")
    self.rm("mozconfig")

    for crate in ["audio_thread_priority"]:
        cargo.clear_vendor_checksums(self, crate, vendor_dir="third_party/rust")


def init_configure(self):
    from cbuild.util import cargo

    self.env["MOZBUILD_STATE_PATH"] = str(self.chroot_srcdir / ".mozbuild")
    self.env["AS"] = self.get_tool("CC")
    self.env["MOZ_MAKE_FLAGS"] = f"-j{self.make_jobs}"
    self.env["RUST_TARGET"] = self.profile.triplet
    # use all the cargo env vars we enforce
    self.env.update(cargo.get_environment(self))


def configure(self):
    conf_opts = [
        "--prefix=/usr",
        "--libdir=/usr/lib",
        "--host=" + self.profile.triplet,
        "--target=" + self.profile.triplet,
        "--disable-install-strip",
        "--disable-strip",
        "--enable-linker=lld",
        "--enable-optimize",
        "--enable-release",
        "--with-wasi-sysroot=/usr/wasm32-unknown-wasi",
        # we have our own flags and better
        "--disable-hardening",
        # system libs
        "--with-system-ffi",
        "--with-system-icu",
        "--with-system-jpeg",
        "--with-system-libevent",
        "--with-system-libvpx",
        "--with-system-nspr",
        "--with-system-nss",
        "--with-system-pixman",
        "--with-system-webp",
        "--with-system-zlib",
        # no apng support
        "--without-system-png",
        # features
        "--enable-audio-backends=pulseaudio",
        "--enable-dbus",
        "--enable-default-toolkit=cairo-gtk3-wayland",
        "--enable-jack",
        "--enable-necko-wifi",
        "--enable-pulseaudio",
        # disabled features
        "--disable-alsa",
        "--disable-default-browser-agent",
        "--disable-jemalloc",
        "--disable-profiling",
        "--disable-tests",
        "--disable-updater",
        "--disable-crashreporter",
        # browser options
        "--allow-addon-sideload",
        "--enable-application=browser",
        "--with-app-name=librewolf",
        "--with-branding=browser/branding/librewolf",
        f"--with-l10n-base={self.chroot_cwd}/lw/l10n",
        "--with-distribution-id=org.chimera-linux",
    ]

    match self.profile.arch:
        case "x86_64" | "aarch64":
            # broken with rust 1.78 as it enables packed_simd feature that uses removed platform_intrinsics
            # conf_opts += ["--enable-rust-simd"]
            pass

    if self.has_lto():
        conf_opts += ["--enable-lto=cross"]

    _use_pgo = self.has_lto()

    # aarch64: gets stuck busy-looping in profiling pass in ff140
    # ppc64le: takes long to link and generates a broken binary
    if self.profile.arch in ["aarch64", "ppc64le"]:
        _use_pgo = False

    if _use_pgo:
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
            self.do("./mach", "build", "--priority", "normal")
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
                ldp = self.chroot_cwd / d.name / "dist/librewolf"
            self.do(
                "dbus-run-session",
                "--",
                "cage",
                "sh",
                "-c",
                "wlr-randr --output HEADLESS-1 --custom-mode 1920x1080@60; ./mach python ./build/pgo/profileserver.py",
                env={
                    "HOME": str(self.chroot_cwd),
                    "JARLOG_FILE": str(self.chroot_cwd / "jarlog"),
                    "LD_LIBRARY_PATH": ldp,
                    "LIBGL_ALWAYS_SOFTWARE": "1",
                    "LLVM_PROFDATA": "llvm-profdata",
                    "XDG_RUNTIME_DIR": "/tmp",
                    "WLR_BACKENDS": "headless",
                },
            )
        # clean up build dir
        with self.stamp("profile_clobber") as s:
            s.check()
            self.log("cleaning up profile build...")
            self.do("./mach", "clobber", "objdir")
        # and finally make use of this for real configure
        conf_opts += [
            "--enable-profile-use=cross",
            f"--with-pgo-profile-path={self.chroot_cwd / 'merged.profdata'}",
            f"--with-pgo-jarlog={self.chroot_cwd / 'jarlog'}",
        ]

    self.log("configuring final librewolf...")
    self.do("./mach", "configure", *conf_opts)


def build(self):
    self.do("./mach", "build", "--priority", "normal")


def install(self):
    self.do(
        "./mach",
        "install",
        env={"DESTDIR": str(self.chroot_destdir)},
    )

    self.install_file(
        self.files_path / "vendor.js",
        "usr/lib/librewolf/browser/defaults/preferences",
    )
    self.install_file(
        self.files_path / "distribution.ini", "usr/lib/librewolf/distribution"
    )
    self.install_file(
        self.files_path / "librewolf.desktop", "usr/share/applications"
    )

    # icons
    for sz in [16, 22, 24, 32, 48, 128, 256]:
        self.install_file(
            f"browser/branding/librewolf/default{sz}.png",
            f"usr/share/icons/hicolor/{sz}x{sz}/apps",
            name="librewolf.png",
        )

    # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
    self.uninstall("usr/lib/librewolf/librewolf-bin")
    self.install_link("usr/lib/librewolf/librewolf-bin", "librewolf")
